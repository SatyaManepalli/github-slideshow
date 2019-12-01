# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:11:11 2019

@author: Satya Manepalli
"""

import pandas as pd
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)

pd.set_option('display.max_columns', 100)
print(dataset)
print(dataset.shape)
print(dataset.head(20))

#Statistical summary
print(dataset.describe())
print (dataset.groupby(['class']).size())

#Box and whisker plots
dataset.plot(kind='box',subplots = True, layout=(2,2), sharex=False, sharey=False)
plt.show()

dataset.hist()
plt.show()

#Multivariate plots
#scatter plot matrix
scatter_matrix(dataset)
plt.show()

array = dataset.values
X = array[:,0:4]         #all rows, first four columns (0-3)
Y = array[:,4]           #all rows, column 4 – the class
validation_size = 0.20   #Keep 20% of data for testing
seed = 7
X_train, X_validation, Y_train, Y_validation = \
(model_selection.train_test_split(X, Y, \
test_size=validation_size, random_state=seed))

scoring = 'accuracy'
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))

results = []
names = []
print("\nShow results for each of the methods\nName\t   Mean\t\t   STD")
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, 
			cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s:\t %f \t(%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)

knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print("=======KNN Accuracy=========")
print(accuracy_score(Y_validation, predictions))
print('\n==== KNN Confusion Matrix=====')
print(confusion_matrix(Y_validation, predictions))
print("\n======= KNN Classification Report=========")
print(classification_report(Y_validation, predictions))



