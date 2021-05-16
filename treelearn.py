import matplotlib.image as pltimg
import matplotlib.pyplot as plt
import os
import pandas
import pydotplus
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
def treelearn(): #zwraca utworzone drzewo decyzyjne
    df = pandas.read_csv(os.path.join('resources', 'data.csv')) #czytanie danych do nauki drzewa z pliku .csv
    features = ['amount of seeds', 'collected plants', 'fertilizer', 'fuel', 'water level']
    x = df[features] #wczytanie atrybutów, z których ma się uczyć drzewo
    y = df['back to station'] #podjęte decyzje
    dtree = DecisionTreeClassifier() #tworzy obiekt drzewa
    dtree = dtree.fit(x, y) #uczy drzewo
    data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
    graph = pydotplus.graph_from_dot_data(data)
    graph.write_png(os.path.join('resources', 'mydecisiontree.png'))
    img = pltimg.imread(os.path.join('resources', 'mydecisiontree.png'))
    imgplot = plt.imshow(img)
    plt.show() #wyświetl drzewo decyzyjne
    return dtree
def make_decision(tree, amount_of_seeds, collected_plants, fertilizer, fuel, water_level): #zwraca decyzję o powrocie do stacji (0 : NIE, 1 : TAK)
    decision = tree.predict([[amount_of_seeds, collected_plants, fertilizer, fuel, water_level]]) #podejmij decyzję na podstawie aktualnych parametrów traktora o powrocie do stacji lub nie
    return decision