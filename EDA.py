#Load the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#Load the data
df = pd.read_csv('SampleSuperstore.csv')
print("The whole dataset")
print(df)

#Understanding the data
print("The first five rows ")
print(df.head())
print("The last five rows")
print(df.tail())
print("The number of rows and columns")
print(df.shape)
print("Column names")
print(df.columns)

#Basic information

print(df.info())

#Describe the data

print(df.describe())

#Find the duplicates

print(df.nunique())

print(df.duplicated().sum())
print(df['Country'].unique())
print(df["Ship Mode"].unique())
print(df["Segment"].unique())
print(df["City"].unique())
print(df["State"].unique())
print(df["Postal Code"].unique())
print(df["Region"].unique())
print(df["Category"].unique())
print(df["Sub-Category"].unique())
print(df["Sales"].unique())
print(df["Quantity"].unique())
print(df["Discount"].unique())
print(df["Profit"].unique())

col = df["Sales"].max()
max_x = df.loc[df["Sales"].idxmax()]
print ("Maximum of value coulumn Sales ", col, " and its corresponding row values:\n", max_x)

col2 = df["Sales"].min()
min_x = df.loc[df["Sales"].idxmin()]
print ("Minimum of value column Sales ", col2, " and its corresponding row values:\n", min_x)

p1 = df["Profit"].max()
max_x = df.loc[df["Profit"].idxmax()]
print ("Maximum value of column Profit ", p1, " and its corresponding row values:\n", max_x)

p2 = df["Profit"].min()
min_x = df.loc[df["Profit"].idxmin()]
print ("Minimum value of column Profit ", p2, " and its corresponding row values:\n", min_x)

print(df.groupby(["Ship Mode"])['Sales'].sum())
print(df.groupby(["Segment"])['Sales'].sum())
print(df.groupby(["State"])['Sales'].sum())
print(df.groupby(["City"])['Sales'].sum())
print(df.groupby(["Region"])['Sales'].sum())
print(df.groupby(["Category"])['Sales'].sum())
print(df.groupby(["Sub-Category"])['Sales'].sum())

print(df.groupby(["Ship Mode"])['Profit'].sum())
print(df.groupby(["Segment"])['Profit'].sum())
print(df.groupby(["State"])['Profit'].sum())
print(df.groupby(["City"])['Profit'].sum())
print(df.groupby(["Region"])['Profit'].sum())
print(df.groupby(["Category"])['Profit'].sum())
print(df.groupby(["Sub-Category"])['Profit'].sum())

#Cleaning the data

print(df.isnull().sum())


#Relationship Analysis
#Correlation Matrix

data = df[["Sales","Quantity","Discount","Profit"]]
correlation = data.corr()
print(correlation)

heatmap = sns.heatmap(correlation, xticklabels=correlation.columns, yticklabels=correlation.columns, annot = True)
plt.show()
sns.pairplot(data)
plt.show()

sns.relplot(x = "Sales", y ="Profit",hue = "Category",data = df)
plt.show()
sns.displot(df["Sales"])
plt.show()
sns.catplot(x= "Profit", kind= "box", data = df)
plt.show()


