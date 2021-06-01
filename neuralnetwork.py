from PIL import Image
from torch.autograd import Variable
from torch.optim import Adam
from torch.utils.data import DataLoader
from torchvision.transforms import transforms
import glob
import os
import pathlib
import torch
import torch.nn as nn
import torchvision
transformer1 = transforms.Compose([transforms.Resize((150, 150)), transforms.ToTensor(), transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])])
class ConvNet(nn.Module):
    def __init__(self, num_classes=6):
        super(ConvNet, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=12, kernel_size=3, stride=1, padding=1)
        self.bn1 = nn.BatchNorm2d(num_features=12)
        self.relu1 = nn.ReLU()
        self.pool = nn.MaxPool2d(kernel_size=2)
        self.conv2 = nn.Conv2d(in_channels=12, out_channels=20, kernel_size=3, stride=1, padding=1)
        self.relu2 = nn.ReLU()
        self.conv3 = nn.Conv2d(in_channels=20, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.bn3 = nn.BatchNorm2d(num_features=32)
        self.relu3 = nn.ReLU()
        self.fc = nn.Linear(in_features=75 * 75 * 32, out_features=num_classes)
    def forward(self, input):
        output = self.conv1(input)
        output = self.bn1(output)
        output = self.relu1(output)
        output = self.pool(output)
        output = self.conv2(output)
        output = self.relu2(output)
        output = self.conv3(output)
        output = self.bn3(output)
        output = self.relu3(output)
        output = output.view(-1, 32 * 75 * 75)
        output = self.fc(output)
        return output
def create_neural_network(): #tworzenie sieci neuronowej
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu') #użyj cuda jeśli możliwe
    transformer = transforms.Compose([transforms.Resize((150, 150)), transforms.RandomHorizontalFlip(), transforms.ToTensor(), transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])])
    train_path = os.path.join('resources/neural_network/train/') #ścieżka do obrazków do treningu
    test_path = os.path.join('resources/neural_network/test/') #ścieżka do obrazków do testu
    train_loader = DataLoader(torchvision.datasets.ImageFolder(train_path, transform=transformer), batch_size=64, shuffle=True)
    test_loader = DataLoader(torchvision.datasets.ImageFolder(test_path, transform=transformer), batch_size=32, shuffle=True)
    root = pathlib.Path(train_path)
    classes = sorted([j.name.split('/')[-1] for j in root.iterdir()])
    if os.path.exists("resources/neural_network/checkpoint.model"): #jeżeli istnieje model to wczytaj
        checkpoint = torch.load(os.path.join('resources/neural_network', 'checkpoint.model'))
        model = ConvNet(num_classes=6)
        model.load_state_dict(checkpoint)
        model.eval()
    else: #w przeciwnym razie utwórz nowy model
        model = ConvNet(num_classes=6).to(device)
        optimizer = Adam(model.parameters(), lr=0.001, weight_decay=0.0001)
        loss_function = nn.CrossEntropyLoss()
        num_epochs = 10
        train_count = len(glob.glob(train_path + '/**/*.png')) #liczba obrazków treningowych
        test_count = len(glob.glob(test_path + '/**/*.png')) #liczba obrazków testowych
        best_accuracy = 0.0
        for epoch in range(num_epochs):
            model.train()
            train_accuracy = 0.0
            train_loss = 0.0
            for i, (images, labels) in enumerate(train_loader):
                if torch.cuda.is_available():
                    images = Variable(images.cuda())
                    labels = Variable(labels.cuda())
                optimizer.zero_grad()
                outputs = model(images)
                loss = loss_function(outputs, labels)
                loss.backward()
                optimizer.step()
                train_loss += loss.cpu().data * images.size(0)
                _, prediction = torch.max(outputs.data, 1)
                train_accuracy += int(torch.sum(prediction == labels.data))
            train_accuracy = train_accuracy / train_count
            train_loss = train_loss / train_count
            model.eval()
            test_accuracy = 0.0
            for i, (images, labels) in enumerate(test_loader):
                if torch.cuda.is_available():
                    images = Variable(images.cuda())
                    labels = Variable(labels.cuda())
                outputs = model(images)
                _, prediction = torch.max(outputs.data, 1)
                test_accuracy += int(torch.sum(prediction == labels.data))
            test_accuracy = test_accuracy / test_count
            print('Epoch: ' + str(epoch + 1) + ' Train Loss: ' + str(train_loss) + ' Train Accuracy: ' + str(train_accuracy) + ' Test Accuracy: ' + str(test_accuracy))
            if test_accuracy > best_accuracy:
                torch.save(model.state_dict(), 'resources/neural_network/checkpoint.model')
                best_accuracy = test_accuracy
        checkpoint = torch.load(os.path.join('resources/neural_network', 'checkpoint.model'))
        model = ConvNet(num_classes=6)
        model.load_state_dict(checkpoint)
        model.eval()
    return classes, model
def predfield(cart_direction, cart_x, cart_y, classes, model): #zwraca najbliższe miejsce pola z wyrośniętą rośliną na podstawie wykrywania obrazu
    pred_path = os.path.join('resources/neural_network/sliced/') #ścieżka do obrazków do sprawdzenia
    pred_dict = {}
    images_path = glob.glob(pred_path + '/*.png')
    cart_x = int(cart_x) #x'owa wózka
    cart_y = int(cart_y) #y'owa wózka
    additional_rotate_moves = 0
    x = None #x'owa pola
    y = None#y'kowa  pola
    min = None
    for i in images_path: #dodajemy pocięte obrazki do listy i ustawiamy im przewidywaną metkę
        pred_dict[i[i.rfind('/') + 1:]] = prediction1(classes, i, model, transformer1)
    for img_name, field in pred_dict.items():
        if field != "random": #jeżeli metka nie jest 'random' to przypisz do x'a i y'a miejsce wyrośniętej rośliny
            if x is None and y is None:
                x = img_name[18]
                y = img_name[15]
                x = int(x)
                y = int(y)
                if x == 0:
                    x = 9
                else:
                    x = x - 1
                if y == 0:
                    y = 9
                else:
                    y = y - 1
                min = abs(cart_x - x) + abs(cart_y - y) + additional_rotate_moves
            else:
                temp_x = img_name[18]
                temp_y = img_name[15]
                temp_x = int(temp_x)
                temp_y = int(temp_y)
                if temp_x == 0:
                    temp_x = 9
                else:
                    temp_x = temp_x - 1
                if temp_y == 0:
                    temp_y = 9
                else:
                    temp_y = temp_y - 1
                if abs(cart_x - temp_x) + abs(cart_y - temp_y) + additional_rotate_moves < min:
                    x = temp_x
                    y = temp_y
                    min = abs(cart_x - x) + abs(cart_y - y) + additional_rotate_moves
    if x == None and y == None: #jeżeli nie ma wyrośniętej rośliny to zwróć False
        return False
    else:
        print(x, y)
        print(min)
        return x, y
def prediction1(classes, img_path, model, transformer): #zwraca predykcję dla danego obrazka
    image = Image.open(img_path).convert('RGB')
    image_tensor = transformer(image).float()
    image_tensor = image_tensor.unsqueeze_(0)
    if torch.cuda.is_available():
        image_tensor.cuda()
    input = Variable(image_tensor)
    output = model(input)
    index = output.data.numpy().argmax()
    pred = classes[index]
    return pred