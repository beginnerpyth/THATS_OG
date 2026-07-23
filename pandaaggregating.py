import pandas as pd
import numpy as np
bios=pd.read_csv('bios.csv')
coffee=pd.read_csv('coffee.csv')
print(bios)
print(bios.columns)
print(bios.head())
#print(bios['born_city'].value_counts())
print(coffee)
#print(coffee.sort_values(['Units Sold','Coffee Type'],ascending=(1,0)))#so we just sort values where 
#print cant take ascending if writter out of sort_values and 0 as false and 1 as true
print(coffee.value_counts(['Coffee Type']))#so it counts the coffee types with descending wise 

print(bios.sort_values(['born_city'])[['born_city','name']])#so we can sort and count values by .sort_values([])
#and .count_values([])
#print(bios.value_counts(['born_city']))# so this value_counts gives you the value in descending order 

print(bios.sort_values(['born_city','born_date'],ascending=(0,1))[['born_city','born_date']])
print(bios.value_counts(['born_city','born_date']))

