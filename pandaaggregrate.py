import pandas as pd
import numpy as np
bios=pd.read_csv('bios.csv')
coffee=pd.read_csv('coffee.csv')
print(bios.head(55)[['born_city','born_region']])
print(bios.value_counts('born_city'))#we can do bios['born_city'].value_counts
print(bios.sort_values(['born_city','born_date'])[['name','born_city']])#so i want to sortify my values according
#to filter
print(bios[bios['born_country']=='USA']['born_city'].value_counts())#so i want to filter the data of specific 
#city of specific country
print(bios.groupby(['born_country'])['born_city'].value_counts(50))
print(coffee.groupby(['Coffee Type'])['Units Sold'].sum())
#just little practice
#print(coffee[coffee['Coffee Type']=='Espresso'][['Units Sold','Coffee Type']])
#new_coffee=coffee.copy()
#new_coffee.rename(columns={'Day':'gatey'},inplace=True)
#print(new_coffee)
print(bios.groupby(['born_country'])['born_city'].value_counts())#we use value_counts to sum the total by desc
print('it just got printed')
print(coffee.groupby(['Coffee Type'])['Units Sold'].mean())#so i want every coffe type mean
print(coffee.value_counts('Coffee Type'))#so it only counts the value doesnt aggregrate
print(coffee.groupby(['Coffee Type'])['Units Sold'].sum())#it sum the value by types
print(coffee.groupby(['Day'])['Coffee Type'].value_counts())
coffee['price']=22
coffee['new_price']=np.where(coffee['Coffee Type']=='Espresso',20,30)
coffee.drop(columns={'price'},inplace=True)
print(coffee)
print(coffee.groupby(['Coffee Type']).agg({'Units Sold':'sum','new_price':'mean'}))

print(bios)
print(bios.columns)
print(bios.groupby(['born_city']).agg({'height_cm':'sum','weight_kg':'mean'}))
print(bios.value_counts(['born_country']))
print(bios.columns)
print(bios.groupby(['born_country']).agg({'height_cm':'sum','weight_kg':'mean'}))
print(bios.sort_values(['born_country'])[['born_country']],'here')
print(bios.value_counts(['born_country']))
print(bios.groupby(['born_country'])['born_city'].value_counts())
print(bios.groupby(['born_country'])[['born_city']].nunique())
