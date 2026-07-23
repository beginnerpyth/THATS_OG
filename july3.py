import pandas as pd
import numpy as np
import requests
import dotenv
from fastapi import FastAPI
from sqlalchemy import create_engine,text,String,Integer

today='bios.csv'
pd_read=pd.read_csv(today)
print(pd_read)
print(pd_read.columns)
print(pd_read.head(6))
print(pd_read.tail(6))
filter=(pd_read[pd_read['born_country'].str.contains('FRA',na=False)])[['born_country','born_city']]
filter1=pd_read[pd_read['born_city'].str.contains('Bordeaux',na=False)][['born_country','born_city']]
print(filter)
pd_read['height_cm']=pd_read['height_cm'].ffill()
print(pd_read['height_cm'].rolling(window=3).mean())
merging=pd.merge(filter,filter1)
print(merging)

#numpy
arr=np.array([1,2,3,4,5,6])
print(arr)
mul=arr*3

print(mul)
res=mul.reshape(2,3)
print(res)
as_t=(res.astype('float32'))
print(as_t)
ran_in=np.random.randint(low=1,high=33,size=(3,2))
mat=np.matmul(ran_in,res)
print(mat)
