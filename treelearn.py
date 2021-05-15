import matplotlib.image as pltimg
import matplotlib.pyplot as plt
import os
import pandas
import pydotplus
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
def treelearn():
    df = pandas.read_csv(os.path.join('resources', 'data.csv'))
    features = ['amount of seeds', 'collected plants', 'fertilizer', 'fuel', 'water level']
    x = df[features]
    y = df['back to station']
    dtree = DecisionTreeClassifier()
    dtree = dtree.fit(x, y)
    data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
    graph = pydotplus.graph_from_dot_data(data)
    graph.write_png(os.path.join('resources', 'mydecisiontree.png'))
    img = pltimg.imread('mydecisiontree.png')
    imgplot = plt.imshow(img)
    plt.show()