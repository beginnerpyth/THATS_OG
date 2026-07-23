import pandas as pd
import numpy as np
bios=pd.read_csv('bios.csv')
coffee=pd.read_csv('coffee.csv')
print(bios.columns)
print(coffee.columns)
#Q2
print(bios.head(10))
print(bios[['born_country','name']])
print(bios.loc[5,'height_cm'])
print(bios[bios['height_cm']>200]['name'])
bios['borndates']=pd.to_datetime(bios['born_date'])
bios['year']=bios['borndates'].dt.year
bios['month']=bios['borndates'].dt.month
print(bios['born_date'].head(6))
print(bios['NOC'])

print(bios[(bios['NOC']=='USA')&(bios['year']>1990)][['name','year']])
print(bios[bios['name'].str.contains('James')])

#level 3
coffee['Revenue']=coffee['Units Sold']*5
print(coffee)
print("this is total number of null value in died_date",bios['died_date'].isna().sum())
bios['born_region']=np.where(bios['born_region']=='Nan','Unknown',bios['born_region'])
print("this is null value in born region",bios['born_region'].isna().sum())
bios['born_region']=bios['born_region'].fillna('unknown')
print('there is not null value in born_region',bios['born_region'].isna().sum())
bios.rename(columns={'weight_kg':'Weight'},inplace=True)
print(bios['Weight'])
#level 4
print(bios['NOC'].value_counts())
print(bios.groupby('born_country').agg({'height_cm':'mean'}))
print(coffee.groupby('Coffee Type')['Units Sold'].agg({'mean','sum'}))
#coffee.loc[0,'Units Sold']=np.nan
#print(coffee)
#coffee['Units Sold']=coffee['Units Sold'].fillna('Unknown')
#print(coffee)
#print(coffee.isna().sum()
#advanced functionality
print(bios)
print(coffee)
coffee['yesterday revenue']=coffee['Revenue'].shift()#it is like giving you past data and you can even pass the value
coffee['total sum']=coffee['Revenue'].cumsum()#it adds up from row by row
coffee['Rank']=coffee['Revenue'].rank()#it ranks the revenue
print(coffee.sort_values(['Rank'],ascending=False))
coffee.drop(columns={'yesterday revenue'},inplace=True)

coffee["Previous Day Revenue"]=coffee['Revenue'].shift()
coffee['3Average']=coffee['Units Sold'].rolling(window=3).mean()#so it works like a cumsum  and rank 
coffee['3daysrevenuesum']=coffee['Revenue'].rolling(window=3).sum()

print(coffee)


