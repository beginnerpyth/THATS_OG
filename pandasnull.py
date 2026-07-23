import pandas as pd
import numpy as np
bios=pd.read_csv('bios.csv')
noc=pd.read_csv('noc_regions.csv')
coffee=pd.read_csv('coffee.csv')
print(bios.head())
print(bios.isna())#it gives you boolean value
print(bios.isna().sum())#it gives you  na value in like table
#to convert into nan
coffee.loc[2:3,'Units Sold']=np.nan
print(coffee)
#magic part is np.nan
#fillnan
#print(coffee.fillna(1000))#it means just the temporary solution 
#coffee.fillna(1000,inplace=True)#to make permanent you have to use inplace =true
#coffee=coffee.fillna(999)#to make permanent change another method 
#print(coffee.fillna(coffee['Units Sold'].mean()))#this is temporary and makes the na  value excluding 'units sold'
#coffee['Units Sold']=coffee['Units Sold'].fillna(coffee['Units Sold'].mean())
#print(coffee)
#print(coffee.fillna(coffee['Units Sold'].interpolate()))
#print(coffee.fillna(coffee['Units Sold']))
#print(coffee)#to fill nan values
#print(coffee.isna().sum())
#print(coffee)
#coffee['Units Sold']=np.where(coffee['Units Sold']==33,22,15)#so it changes the value you want 
#coffee['Units Sold']=coffee['Units Sold'].fillna(100)#so we used coffee['Units Sold]＝ because to 
#permanently change the value and instead of doing the inplace=true
print(coffee)
#coffee['Units Sold']=coffee['Units Sold'].fillna(coffee['Units Sold'].interpolate())#so it gives you the interpolate
#value and magic is i did coffee['Units Sold']
#coffee=coffee.dropna()#so it drops the null value with whole row
#coffee=coffee.dropna(subset={'Units Sold'}) #it means that only on subset 'Units Sold' we drop na specific columns
print(coffee)
#print(coffee.isna())#it gives you the boolean value
#print(coffee.isna().sum())#so the total sum of null will be shown
# to filter the null value
print(coffee[coffee['Units Sold'].isna()])#so we use filterinhg for  na value by .isna()
print(coffee[coffee['Units Sold'].notna()])#so we can filter the values notna() and get the results

 









