from PIL import Image
from torch.autograd import Variable
from torch.optim import Adam
from torch.utils.data import DataLoader
from torchvision.transforms import transforms
import glob
import numpy as np
import os
import pathlib
import torch
import torch.nn as nn
import torchvision
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
def create_neural_network():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    transformer = transforms.Compose([transforms.Resize((150, 150)), transforms.RandomHorizontalFlip(), transforms.ToTensor(), transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])])
    train_path = os.path.join('resources/neural_network/train/')
    test_path = os.path.join('resources/neural_network/test/')
    pred_path = os.path.join('resources/neural_network/pred/')
    train_loader = DataLoader(torchvision.datasets.ImageFolder(train_path, transform=transformer), batch_size=64, shuffle=True)
    test_loader = DataLoader(torchvision.datasets.ImageFolder(test_path, transform=transformer), batch_size=32, shuffle=True)
    root = pathlib.Path(train_path)
    classes = sorted([j.name.split('/')[-1] for j in root.iterdir()])
    if os.path.exists("resources/neural_network/checkpoint.model"):
        checkpoint = torch.load(os.path.join('resources/neural_network', 'checkpoint.model'))
        model = ConvNet(num_classes=6)
        model.load_state_dict(checkpoint)
        model.eval()
        transformer1 = transforms.Compose([transforms.Resize((150, 150)), transforms.ToTensor(), transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])])
        images_path = glob.glob(pred_path+'/*.jpg')
        pred_dict = {}
        for i in images_path:
            pred_dict[i[i.rfind('/') + 1:]] = prediction1(classes, i, model, transformer1)
        print(pred_dict)
    else:
        model = ConvNet(num_classes=6).to(device)
        optimizer = Adam(model.parameters(), lr=0.001, weight_decay=0.0001)
        loss_function = nn.CrossEntropyLoss()
        num_epochs = 10
        train_count = len(glob.glob(train_path + '/**/*.jpg'))
        test_count = len(glob.glob(test_path + '/**/*.jpg'))
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
def prediction1(classes, img_path, model, transformer):
    image = Image.open(img_path)
    image_tensor = transformer(image).float()
    image_tensor = image_tensor.unsqueeze_(0)
    if torch.cuda.is_available():
        image_tensor.cuda()
    input = Variable(image_tensor)
    output = model(input)
    index = output.data.numpy().argmax()
    pred = classes[index]
    return pred