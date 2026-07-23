import pandas as pd
import numpy as np
coffee=pd.read_csv('coffee.csv')
bios=pd.read_csv('bios.csv')
#adding or removing rows and columns
print(coffee)
coffee['new_coffee']=20
print(coffee)
coffee['new_coffee']=np.where(coffee['Units Sold']==25,28,20)
print(coffee)
coffee.drop(1,inplace=True)
print(coffee)
gg=coffee.copy()#so we use copy to make that only change at gg even we modify gg without it we just copy whole
#values
gg['new_gg']=33
coffee.drop(columns={'new_coffee'},inplace=True)#so when we use column we use {} this bracket
print(coffee)
print(gg)
coffee['total']=coffee['Units Sold']*2
print(coffee)
coffee.rename(columns={'total':'sotal'},inplace=True)#without using inplace we need to use print to show temporary
print(coffee)
print(coffee.head())
print(bios)
bios_new=bios.copy()
bios_new['first_name']=bios['name'].str.split(' ').str[0]
print(bios_new.first_name)
#print(bios_new.'first_name')
bios_new['last_name']=bios_new['name'].str.split(' ').str[1]
print(bios_new.last_name)
bios_new.rename(columns={'last_name':'surname'},inplace=True)#it means change oermanently
print(bios_new.columns)
print(bios_new.query('first_name=="Keith"')[['name','first_name']])
print(bios_new.info())
print(bios_new.born_date)
bios_new['born']=pd.to_datetime(bios_new['born_date'],format="%Y-%m-%d")
bios_new['year']=bios_new['born'].dt.year
bios_new['month']=bios_new['born'].dt.month
print(bios_new['year'])
print(bios_new['month'])
#apply function to add columns it is function thats why we use ()
bios["height_category"]=bios['height_cm'].apply(lambda x: 'short' if x < 150 else 'Average' if x < 170 else 'tall' )
print(bios[['name','height_cm','height_category']])
#bios_new.to_csv('./PYTHONPROJECT/bios_new.csv',index=False)
#bios.drop(columns={"height_category"},inplace=True)
print(bios['height_category'])
def weight_class(row):
    if row['weight_kg']>70 and row['weight_kg']<80:
        return 'its a light weight'
    if row['weight_kg']>80 and row['weight_kg']<90:
        return 'its a middle weight'
    else:
        return 'its a heavy weight'
bios['weight_class']=bios.apply(weight_class,axis=1)#so we used axis=1 cause its a row not a column so it checks
#row wise and return value if condition mets
print(bios['weight_class'])
