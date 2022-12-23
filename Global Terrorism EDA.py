import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import warnings
warnings.filterwarnings('ignore')

dataset= pd.read_csv("globalterrorismdb_0718dist.csv",encoding= "latin1")
df=pd.DataFrame(dataset)
print("The whole dataset")
print(df)
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

#Finding the null values

print(df.isnull().sum())

#cleaning the data



df.rename(columns={"iyear": "Year", "imonth": "Month", "iday": "Day", "country_txt": "Country",
                   "region_txt": "Region", "provstate": "Province/State", "city": "City",
                   "latitude": "Latitude", "longitude": "Longitude", "location": "Location",
                   "summary": "Summary", "attacktype1_txt": "Attack Type", "targtype1_txt": "Target Type",
                   "gname": "Group Name", "motive": "Motive", "weaptype1_txt": "Weapon Type",
                   "nkill": "Killed", "nwound": "Wounded", "addnotes": "Add Notes",'target1':'Target'}, inplace=True)

df = df[["Year","Month","Day","Country","Province/State","Region","City","Latitude","Longitude","Attack Type","Killed","Wounded","Summary","Group Name","Target Type","Motive","Weapon Type"]]




df["Killed"]=df["Killed"].fillna(0)
df["Wounded"]=df["Wounded"].fillna(0)





#Visualizing the data
attacks=df["Year"].value_counts(dropna=False).sort_index().to_frame().reset_index().rename(columns={"index":"Year","Year":"Attacks"}).set_index("Year")
attacks.head()
attacks.plot(kind="bar",color="cornflowerblue",figsize=(15,6),fontsize=13)
plt.title("Timeline of Attacks",fontsize=15)
plt.xlabel("Years",fontsize=15)
plt.ylabel("Number of Attacks",fontsize=15)
plt.show()

year = df["Year"].unique()
years_count = df["Year"].value_counts(dropna = False).sort_index()
plt.figure(figsize = (18,10))
sns.barplot(x = year, y = years_count,palette= "tab10")
plt.xticks(rotation= 90)
plt.xlabel("Year",fontsize = 20)
plt.ylabel("No. of attacks each year", fontsize= 20)
plt.title("Attacks over years", fontsize= 30)
plt.show()

pd.crosstab(df.Year,df.Region).plot(kind="area", stacked = False,figsize=(20,10))
plt.title("Terrorism by region over years",fontsize = 25)
plt.xticks(rotation=90)
plt.ylabel("No of attacks",fontsize= 20)
plt.xlabel("Year",fontsize = 20)
plt.show()

data = df[["Year","Killed"]].groupby(["Year"]).sum()
fig, ax4 = plt.subplots(figsize=(20,10))
data.plot(kind="bar",alpha = 0.7,ax = ax4,color = "brown")
plt.xticks(rotation = 90)
plt.title("Deaths due to attack",fontsize=25)
plt.ylabel("No. of death", fontsize=20)
plt.xlabel("Year", fontsize= 20)
top_side = ax4.spines["top"]
top_side.set_visible(False)
right_side = ax4.spines["right"]
right_side.set_visible(False)
plt.show()

df["City"].value_counts().to_frame().sort_values("City",axis = 0,ascending=False).head(10).plot(kind = "bar", figsize=(20,10),color="seagreen")
plt.xticks(rotation = 90)
plt.xlabel("City",fontsize=20)
plt.ylabel("No. of attacks", fontsize=20)
plt.title("10 most affected cities", fontsize = 25)
plt.show()

df[["Attack Type", "Killed"]].groupby(["Attack Type"],axis = 0).sum().plot(kind="bar",figsize=(20,10),color=["steelblue"])
plt.xticks(rotation=90)
plt.title("Count of people killed",fontsize=25)
plt.ylabel("Death Count",fontsize=20)
plt.xlabel("Attack Type",fontsize= 20)
plt.show()

df[["Attack Type", "Wounded"]].groupby(["Attack Type"],axis = 0).sum().plot(kind="bar",figsize=(20,10),color=["plum"])
plt.xticks(rotation=90)
plt.title("Count of people escaped with injury",fontsize=25)
plt.ylabel("Injury Count",fontsize=20)
plt.xlabel("Attack Type",fontsize= 20)
plt.show()

df["Group Name"].value_counts().to_frame().drop("Unknown").head(10).plot(kind="bar",color="Indianred",figsize=(20,10))
plt.title("Top 10 Terrorist Groups",fontsize = 25)
plt.xticks(rotation = 90)
plt.xlabel("Terrorist Organisation Name",fontsize=20)
plt.ylabel("Attack Numbers",fontsize= 20)
plt.show()

df[["Group Name","Killed"]].groupby(["Group Name"],axis=0).sum().drop("Unknown").sort_values("Killed",ascending= False).head(10).plot(kind="bar",color="slategray",figsize=(20,10))
plt.title("Top 10 Organisations With Most Kills", fontsize = 25)
plt.xlabel("Organisation Name",fontsize=20)
plt.ylabel("No. of People Killed",fontsize=20)
plt.show()


plt.subplots(figsize=(20,10))
sns.barplot(x =df["Country"].value_counts()[:10].index, y =df["Country"].value_counts()[:10].values ,palette="YlGnBu_r")
plt.title("Top Countries Affected", fontsize = 25)
plt.xlabel("Countries",fontsize= 20)
plt.ylabel("No. of attacks", fontsize = 20)
plt.xticks(rotation=90)
plt.show()



