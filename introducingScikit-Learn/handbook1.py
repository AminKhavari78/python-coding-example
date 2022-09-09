# working and train iris dataset with sklearn models

import matplotlib as plt
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

iris = sns.load_dataset('iris')

X_iris = iris.drop('species', axis=1)
y_iris = iris['species']


Xtrain, Xtest, ytrain, ytest = train_test_split(X_iris, y_iris, random_state=1)

model = GaussianNB()
model.fit(Xtrain, ytrain)
y_model = model.predict(Xtest)

print(accuracy_score(ytest, y_model))
