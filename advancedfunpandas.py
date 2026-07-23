import pandas as pd
import numpy as np
bios=pd.read_csv('bios.csv')
coffee=pd.read_csv('coffee.csv')
print(bios)
print(coffee)
#advanced function
coffee['Previous day revenue']=coffee['Units Sold'].shift()
coffee['ranking']=coffee['Previous day revenue'].rank()
coffee['cumsum']=coffee['Units Sold'].cumsum()#so it adds upt one by one
coffee['3 days average Units sold']=coffee['Units Sold'].rolling(window=3).mean()
print(coffee)
print(coffee.dropna(subset={'ranking'}))
print(bios['name'])
bios['first_name']=bios['name'].str.split(' ').str[0]
print(bios[(bios['name'].str.contains('yamada|yamazaki|murata',case=False))&(bios['born_country'].isin(['JPN']))])
