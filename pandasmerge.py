import pandas as pd
import numpy as np
bios=pd.read_csv('bios.csv')
mocs=pd.read_csv('noc_regions.csv')
print(mocs.columns)
print(bios.head()['born_country'])
print(mocs.head()['NOC'])
# so we are merging the data and concatenating
bios_new=pd.merge(bios,mocs,left_on='born_country',right_on='NOC',how='left')# so what we are doing is like sql
#we use left on means bios and right means mocs and how is refereneces i.e make sure to get all from left
print(bios_new)
bios_new.rename(columns={'region':'wherecountry'},inplace=True)
print(bios_new)
bios_new['check']=np.where(bios_new['wherecountry']=='France','milxa','namilney')
print(bios_new['born_country'])
#so we are concatenating the dataframe like into two rows first index becomes upper and second becomes lower
fra=bios[bios['born_country']=='FRA'].copy()
gbr=bios[bios['born_country']=='GBR'].copy()
con=pd.concat((fra,gbr))
print(con.tail()[['born_country','name']])#so you can see we used filtering the data
