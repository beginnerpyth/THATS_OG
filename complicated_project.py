import requests
import pandas as pd
import numpy as np
from sqlalchemy import create_engine,MetaData,String,Integer,text,Float
from sqlalchemy.orm import Session,sessionmaker
from fastapi import FastAPI
from dotenv import load_dotenv
import os
load_dotenv()
#extraction
print("BABA =", os.getenv("baba"))
req=requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,weather_code,pressure_msl,dew_point_2m,rain,showers,snowfall')
#decoding from json to dicitonary
dec_oding=req.json()
#going to change into dataframe from dicitonary for transforming from raw to useful
jjk=pd.DataFrame(dec_oding)
print(jjk.head(6))

#creating the tables for insering data and shwing data to fastapi
try:
  engine=create_engine(os.getenv("baba"))
  session=Session(engine)
  session.execute(text("DROP TABLE IF EXISTS WEATHER_CAST"))
  session.commit()
  session.execute(text("CREATE TABLE WEATHER_CAST(LATITUDE DECIMAL,LONGITUDE DECIMAL,ELEVATION DECIMAL,TIME DATETIME)" ))
  session.commit()
  lat=dec_oding["latitude"]
  lon=dec_oding["longitude"]
  ele=dec_oding["elevation"]
  raw_data=pd.DataFrame(dec_oding["hourly"])
  ext_data=list(raw_data.itertuples())#it gives you every row in form of tuples
#in here sqlalchemy only can insert values in form of diciotanry and x.access values is how we access hybrid tuples
#cause its type of tuple where there is key and yu can access with column_name
  session.execute(text("INSERT INTO WEATHER_CAST(LATITUDE,LONGITUDE,ELEVATION,TIME) VALUES(:LAT,:LON,:ELE,:TIME)"),[{"LAT":lat,"LON":lon,"ELE":ele,"TIME":x.time}for x in ext_data])
  session.commit()
  session.execute(text("DROP TABLE IF EXISTS TEMPERATURE"))
  session.commit()
  session.execute(text("CREATE TABLE TEMPERATURE(VIEW_TEMPERATURE DECIMAL,VIEW_TIME DATETIME,RAIN DECIMAL,DEW_PONT DECIMAL)"))
  session.commit()
  session.execute(text("INSERT INTO TEMPERATURE(VIEW_TEMPERATURE,VIEW_TIME,RAIN,DEW_PONT) VALUES(:TEMP,:TIME,:RAIN,:DEW)"),[{"TEMP":x.temperature_2m,"TIME":x.time,"RAIN":x.rain,"DEW":x.dew_point_2m}for x in ext_data])
  session.commit()
except Exception as e:
  print("SOMETHIG WENT WRONG",e)
  session.rollback()
  




visual=FastAPI()
@visual.get("/get-live-weather/")
def weather():
    see_weather=session.execute(text("SELECT * FROM WEATHER_CAST "))
    session.commit()
    #when we do fetchall its in rowobject of sql and we extract each row object and convert into hybrid dict i.e x.-mapping but
    #we need to convert into proper dicitioanry so w eonclosed with dict()
    return[dict(x._mapping)for x in see_weather.fetchall()]

@visual.get("/wetaher_with_temperature/")
def temperature():
   see=session.execute(text("SELECT * FROM TEMPERATURE "))
   session.commit()
   return [dict(x._mapping)for x in see.fetchall()]









