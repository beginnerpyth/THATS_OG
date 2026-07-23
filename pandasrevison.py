import pandas as pd
import numpy as np
df=pd.DataFrame([[1,2,3,4,4,5,6,6],[3,4,5,5,7,7,5]],columns=('a','b','c','d','e','f','g','h'),index=('z','x'))
print(df)
print(df.shape)
print(df.size)
print(df.describe())
bios=pd.read_csv('bios.csv')
print(bios.head(3))
coffee=pd.read_csv('coffee.csv')
print(coffee.tail(3))
#results=pd.read_parquet('results.parquet')
#print(results)
print(coffee.shape)
print(coffee.sample(10))
print(coffee.sample(10,random_state=1))#it gives you var.sample(number,random_state=1)
print(coffee.loc[:0,'Units Sold'])
print(coffee.loc[0:4,'Units Sold'])# in loc we use rows and columns but unlike iloc we dont use index in 
#columns and rows
print(coffee.loc[[0,1,2]])
print(coffee.head(3))
coffee.loc[0,'Units Sold']=33
print(coffee.head(5))
print(coffee.columns)#.columns gives the all column name
print(coffee['Units Sold'])#and when we want to get the certain the value we use var[column name]
print(coffee.sort_values(['Units Sold','Coffee Type'],ascending = (0,1)))#so using sort means sorting the vlaue 
# and for ascending we use =(0,1) where 0 means false and 1 means true
for a,b in coffee.iterrows():# the magic is iterrows which gives us the index and columns which 
    print(a)#a is index and b is colimn 
    print(b['Units Sold'])
print(bios.info())
print(bios.columns)
print(bios.head(6))
print(bios.iloc[0:5,0:7])
#filtering 
print(bios[(bios['height_cm']>220)&(bios['born_country']=='USA')][['athlete_id','name','height_cm']])
print(bios[bios['name'].str.contains('keith|patrick',case=False)])#case=false means find the data that contans
#keith whether it is upper or lower or anything that contains name keith
#while regex =false means find the data where keith|patrick including the same computer doesnt undewrstand |
#as or and it is hard
print(bios[bios['name'].str.contains('Robert',case=False)])
print(bios[bios['name'].isin(['Robert Oramas'])])
print(bios[bios['born_country'].isin(['USA','GBR','FRA'])&(bios['weight_kg']>60)][['born_country','name','weight_kg']])
print(bios[(bios['born_country'].isin(['USA','GBR','FRA']))&(bios['name'].str.startswith('Keith'))])#why cant
#we use case 
coffee.loc[0,'Units Sold']=22
print(coffee.head(5))
#method 2 of filteriing data
print(bios.query('born_country == "USA"')[['born_country','name']])
print(bios.query('born_country==("USA","GBR","FRA") and born_city=="Washington"')[['name','born_country','born_city']])
print(coffee)
