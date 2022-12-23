#Import the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Reading the CSV file and giving column names
columns = ["Sepal Length","Sepal Width","Petal Length","Petal Width","Class Labels"]
df = pd.read_csv("iris.data", names = columns)
print(df)
#Understanding the data
print(df.head())

print(df.tail())

print(df.describe())
print(df.shape)
print(df.columns)
print(df.info())

#Cleaning the data

print(df.isnull().sum())

#Visulization of Dataset
sns.pairplot(df,hue="Class Labels")
plt.show()

#Analyse Correlations
data = df[["Sepal Length","Sepal Width","Petal Length","Petal Width"]]
correlation = data.corr()
print(correlation)

heatmap = sns.heatmap(correlation, xticklabels=correlation.columns, yticklabels=correlation.columns, annot = True)
plt.show()


#Separating input columns and the  output columns

data2 = df.values
x = data2[:,0:4]
y = data2[:,4]
print(x)
print(y)

#Splitting the dataset into train and test dataset

from sklearn.model_selection import train_test_split
X_train,X_test, y_train, y_test= train_test_split(x,y, test_size= 0.3)
print(X_train)
print(y_test)

#Model

#Logistic Regression
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)

model.fit(X_train,y_train)

prediction = model.predict(X_test)
#Calculating the accuracy
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,prediction)*100)



