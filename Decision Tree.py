import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

columns = ["Sepal Length","Sepal Width","Petal Length","Petal Width","Class Labels"]
df = pd.read_csv("iris.data", names = columns)
print(df)

#Understanding the dataset

print(df.head())
print(df.tail())
print(df.describe())
print(df.info())
print(df.isnull().sum())
print(df.shape)

X_train = df.drop('Class Labels', axis=1)
print(X_train)
Y_train = df['Class Labels']

#Visulizing the dataset

count = df["Class Labels"].value_counts()
print(count.to_frame())

label = count.index.tolist()
val = count.values.tolist()

exp = (0.05,0.05,0.05)
fig,ax = plt.subplots()
ax.pie(val, explode = exp, labels = label, autopct="%1.1f%%", shadow=True, startangle =90)
plt.title("Different Class Labels of flower present int the dataset")
ax.axis("Equal")
plt.show()

sns.pairplot(data=df, hue="Class Labels")
plt.show()


data = df[["Sepal Length","Sepal Width","Petal Length","Petal Width"]]
correlation = data.corr()
print(correlation)
fig,ax = plt.subplots(figsize=(10,10))
sns.heatmap(correlation, annot=True, ax = ax)
plt.show()
# splitting data in training set(80%) and test set(20%).

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
X_train, X_test, y_train, y_test = train_test_split(X_train, Y_train, test_size=0.3, random_state=100)

from sklearn.tree import DecisionTreeClassifier,plot_tree
dt = DecisionTreeClassifier(criterion="entropy")
dt = dt.fit(X_train, y_train)
act = accuracy_score(y_train, dt.predict(X_train))
print('Training Accuracy is: ', (act * 100))

act = accuracy_score(y_test,dt.predict(X_test))
print('Test Accuracy is: ',(act*100))

plt.figure(figsize=(7,8))
plot_tree(dt,filled=True,feature_names=df.columns)
plt.show()