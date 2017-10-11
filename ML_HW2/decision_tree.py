import pandas as pd
import numpy as np
from sklearn import tree
from  sklearn.datasets import load_iris
from sklearn.externals.six import StringIO
import pydotplus
iris = load_iris()
print(iris)
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df = pd.read_csv('iris.data.txt', header=None, names=names)
target_name = np.array(['setosa', 'versicolor', 'virginica'])
feature_name = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

print(df.loc[:, ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']])
model = tree.DecisionTreeClassifier()
model.fit(df.loc[:, ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values, df['class'].values)
print(model)
dot_data=tree.export_graphviz(model,out_file=None, class_names = target_name, feature_names= feature_name)
graph=pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf('iris_2.pdf')
