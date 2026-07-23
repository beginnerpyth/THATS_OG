import requests
import pandas as pd
import numpy as np
from fastapi import FastAPI
from sqlalchemy import Integer,String,Column,create_engine,text,MetaData
from sqlalchemy.orm import declarative_base,sessionmaker,Session
sava=requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,weather_code,pressure_msl,dew_point_2m,rain,showers,snowfall')

baba=sava.json()#we use this sava.json to decode the json into ditionary or list
print(baba.keys())
hoho=pd.DataFrame(baba)#so we used pandas to transform the dict into dataframe so we could transform anytime we want
print(hoho)
b=hoho.columns
mes=b.to_list()#used to convert the dataframe into list
print(mes,'columns')
print(hoho[['latitude','longitude','elevation','hourly_units','timezone']])

a=hoho.index

ses=a.to_list()
#print(ses,'indexes')
#print(hoho.head(5)[['latitude','longitude','elevation','hourly_units','timezone']],'yeta hai yeta')
aap=FastAPI()
engine=create_engine('mysql+pymysql://root:password123@localhost/CORK')
conn=engine.connect()

conn.execute(text('DROP TABLE IF EXISTS WEATHER'))
conn.commit()
conn.execute(text('CREATE TABLE WEATHER(NAME VARCHAR(555),LATITUDE DEC,LONGITUDE DEC,ELEVATION DEC)'))
#conn.execute(text('CREATE TABLE WEATHER (NAME INT,LATITUDE INT,LONGITUDE INT)'))
conn.commit()
#specify_col=hoho.reset_index()[['index','latitude','longitude','elevation']]
specify_data=list(hoho.itertuples())
#specify_data_lists=specify_data.tolist()
session=Session(engine)
conn.execute(text('INSERT INTO WEATHER(NAME,LATITUDE,LONGITUDE,ELEVATION) VALUES(:name,:lat,:lon,:ele)'),[{"name":x[0],"lat":x[1],"lon":x[2],"ele":x[3]} for x in specify_data])
conn.commit()


#gg=conn.execute(text('SELECT * FROM WEATHER'))
#for x in gg.fetchall():
#        print(x)

@aap.get('/weather/')
def get():
    gg=conn.execute(text('SELECT * FROM WEATHER'))
    conn.commit()
    return[dict(x._mapping) for x in gg.fetchall()]


        


    
    


























