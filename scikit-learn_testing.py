import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn
import sklearn.datasets as datasets

from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn import metrics

def print_data_params(dataset):
    print('data type:', type(dataset))
    print('descr:', dataset.DESCR)
    print('features:', dataset.feature_names)
    print('targets', dataset.target_names)

''' Investigating iris dataset '''
iris = datasets.load_iris()

target_shape = iris.target.shape
data_shape = iris.data.shape

# print_data_params(iris)

''' Supervised learning (regression)
    Load the data
    Split to 80/20 training/test set
    Fit to model
    Run predictive model
    Determine accuracy
    Plot the data '''

# Get the data
X = iris.data # data convention: capital X
y = iris.target # target convention: lowercase y
print('Data shape:', X.shape)

# Split the data
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)

print('\n===Linear regression===')
# Choose the model
model = LinearRegression()
# Fit the model
model.fit(X_train,y_train)
# Run prediction
y_predict = model.predict(X_test)

# Evaluate and score
print('Test score (best is 1):', model.score(X_test, y_predict)) # This will give 1 because y_predict comes from X_test!!! 
print('r2 score:', metrics.r2_score(y_test, y_predict))
print('MSE:', metrics.mean_squared_error(y_test,y_predict))

''' Naive Bayes classification '''
print('\n===Naive Bayes classification===')
classifier = GaussianNB()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
print('Naive Bayes classification:', )
print('Accuracy:', metrics.accuracy_score(y_test,y_pred))

cm = metrics.confusion_matrix(y_pred,y_test)
print('Confusion matrix:\n', cm)
print('Confusion matrix heatmap:\n')
sn.heatmap(cm, annot = True)

''' k nearest neighbours '''
model = neighbors.KNeighborsClassifier(n_neighbors=7)
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print('Classification report:\n', metrics.classification_report(y_test,y_pred))

print('Accuracy:', metrics.accuracy_score(y_test,y_pred))

cm = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
print('cm', cm)

cm = metrics.confusion_matrix(y_pred,y_test)
diagonals = sum([cm[n][n] for n, i in enumerate(cm)])
nondiagonals = sum([cm[n][m] for n, i in enumerate(cm) for m, j in enumerate(i) if n != m])
accuracy = diagonals - nondiagonals # Sum of diagonals minus sum of non-diagonals... dunno how good a metric this is?
print('Accuracy:', accuracy)
print(cm)
sn.heatmap(cm, annot=True, cmap='Blues')

''' Investigating diabetes dataset '''

# diabetes = datasets.load_diabetes()

# print_data_params(diabetes)

# print(diabetes.keys())
# print(diabetes.feature_names)

# print(diabetes.target[:])

''' Investigating breast cancer dataset '''
breast_cancer = datasets.load_breast_cancer()

# print_data_params(breast_cancer)

# X = breast_cancer.data
# y = breast_cancer.target

# print(X.shape, y.shape)

# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)

# model = LinearRegression()
# model.fit(X_train,y_train)
# y_predict = model.predict(X_test)

# print('Test score (best is 1):', model.score(X_test, y_predict)) # This will give 1 because y_predict comes from X_test!!! 
# print('r2 score:', metrics.r2_score(y_test, y_predict))
# print('MSE:', metrics.mean_squared_error(y_test,y_predict))