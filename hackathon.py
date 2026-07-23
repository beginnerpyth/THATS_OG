from sqlalchemy import text,create_engine
from sqlalchemy.orm import Session
from fastapi import FastAPI
import pandas as pd
import numpy as np
from datetime import datetime
import requests
import os
from dotenv import load_dotenv
load_dotenv()
engine=create_engine(os.getenv('database'))

kession=Session(engine)
dekka=requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,weather_code,pressure_msl,dew_point_2m,rain,showers,snowfall')
kaeru=dekka.json()
print(kaeru)
df=pd.DataFrame(kaeru)
print(df)
print(df.columns)
print(df.index)
print(df['hourly'],'here')

lat=kaeru['latitude']
lon=kaeru['longitude']
gen=kaeru['generationtime_ms']
ele=kaeru['elevation']
#drop table incase 
kession.execute(text('drop table if exists hack'))
kession.commit()
#creating the table and database
kession.execute(text("create table hack(latitude numeric,longitude numeric,generationtime_ms numeric,elevation numeric,hourly timestamp)"))
kession.commit()
#just converting the horuly
one=pd.DataFrame(kaeru['hourly'])

to_itertup=list(one.itertuples())
print(to_itertup)
#insert into table
try:
    kession.execute(text('insert into hack values(:lats,:lons,:gens,:eles,:hor)'),[{'lats':lat,'lons':lon,'gens':gen,'eles':ele,'hor':x.time}for x in to_itertup])
    kession.commit()
except Exception as e:
    print('this is wrong')
    kession.rollback()

bap=FastAPI()
@bap.get('/get-weather-info/')
def dasite():
    select_stat=kession.execute(text('select * from hack'))
    #when we do fetchall it fetch values
    result=[dict(x._mapping)for x in select_stat.fetchall()]#so when we do ._mapping then it add the column names to data
    kession.commit()#we used loop inside result to fetch all data so it doesnt fetch first row and return only one row so first
    #we fetched the all rows and then we return
    return result#we use list cause without it doesnt send remaining row and only sends first row if not used list[]
    #and we do dict to change into plain python dict 
    

@bap.post('/情報を変えたい/')
def puttin(lat:float,lon:float,generationtime_ms:float,elevation:float,hourly:datetime):
    kession.execute(text('select * from hack'))
    fetch_data=kession.execute(text('select hourly from hack'))
    if hourly in list(x[0] for x in fetch_data):
        return 'its already here'
    kession.execute(text('insert into hack values(:lats,:lon,:generationtime_ms,:elevation,:hourly)'),{'lats':lat,'lon':lon,'generationtime_ms':generationtime_ms,'elevation':elevation,'hourly':hourly})
    kession.commit()

#@bap.put('/to-update/')
#def updating(lat:float,lon:float,generationtime_ms:float,elevation:float,hourly:datetime):
#    letch_data=kession.execute(text('select hourly from hack'))
#    if hourly in list(letch_data):
#        kession.execute(text('update hack set '))









