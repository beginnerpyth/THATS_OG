#import sqlite3
import pandas as pd
import numpy as np
from fastapi import FastAPI
import mysql.connector
from pydantic import BaseModel

new=FastAPI()

class up(BaseModel):
    product_id:int
    product_name:str
    category:str
    price:int

class up1(BaseModel):
   sales_id:int
   product_id:int
   quantity:int
   sales_price:int
   customer_region:str

class up2(BaseModel):
   product_id:int
   stock_quantity:int
   reorder_level:int
   
@new.get('/get-data/{TABLE}')
def retrieve(TABLE:str):
    conn=mysql.connector.connect(host='localhost',user='root',password='password@123',database='PROJECT', unix_socket='/tmp/mysql.sock')
    cur=conn.cursor()
    cur.execute(f'SELECT * FROM {TABLE}')
    rows=cur.fetchall()
    for x in rows:
        print(x)
    conn.commit()
    return rows
    
@new.post('/get-the-data-of-sales-products/')

def productuploading(product:up):
    conn=mysql.connector.connect(host='localhost',user='root',password='password@123',database='PROJECT', unix_socket='/tmp/mysql.sock')
    cur=conn.cursor()
    values=[product.product_id,product.product_name,product.category,product.price]
    cur.execute('SELECT PRODUCT_ID FROM PRODUCT')#it fetch data
    rows=cur.fetchall()#to check the data
    check=[row[0] for row in rows]

    if product.product_id in check:
     return 'its printed'
    cur.execute('INSERT INTO PRODUCT(PRODUCT_ID,PRODUCT_NAME,CATEGORY,PRICE,CREATED_AT) VALUES(%s,%s,%s,%s,NOW())',values)
    conn.commit()
    


@new.post('/FOR-SALES/')
def salesupload(sale:up1):
   conn=mysql.connector.connect(host='localhost',user='root',password='password@123',database='PROJECT', unix_socket='/tmp/mysql.sock')
   print('its connected')
   cur=conn.cursor()
   values1=[sale.sales_id,sale.product_id,sale.quantity,sale.sales_price,sale.customer_region]
   cur.execute('SELECT SALES_ID FROM SALES')
   row1=cur.fetchall()
   check1=[row[0] for row in row1]
   if sale.sales_id  in check1:
      return 'its already here'
   
   cur.execute('INSERT INTO SALES(SALES_ID,PRODUCT_ID,QUANTITY,SALES_PRICE,SALES_DATE,CUSTOMER_REGION)VALUES(%s,%s,%s,%s,NOW(),%s)',values1)
   print('its before commit')
   conn.commit()


@new.post('/uploading-invenotry/')
def inventoryupload(inv:up2):
    conn=mysql.connector.connect(host='localhost',user='root',password='password@123',database='PROJECT', unix_socket='/tmp/mysql.sock')
    cur=conn.cursor()
    values2=[inv.product_id,inv.stock_quantity,inv.reorder_level]
    cur.execute('SELECT PRODUCT_ID FROM INVENTORY')
    row2=cur.fetchall()
    check2=[row[0] for row in row2]
    if inv.product_id in check2: 
       return 'its already printed'
    cur.execute('INSERT INTO INVENTORY(PRODUCT_ID,stock_quantity,REORDER_LEVEL,LAST_UPDATED) VALUES(%s,%s,%s,NOW())',values2)
    conn.commit()
@new.get('/rolling-avg-of-sales/{TABLE}')
def rollavg(TABLE:str,WHICH_COLUMN:str,):
      
 conn=mysql.connector.connect(host='localhost',user='root',password='password@123',database='PROJECT', unix_socket='/tmp/mysql.sock')
 cur=conn.cursor()
 cur.close()
 conn.commit()
 #df=pd.read_sql(f'SELECT * FROM {TABLE}',conn)#WE DONT NEED TO EXECUTE WHEN USING PANDAS
 df1=pd.read_sql(f'SELECT * FROM {TABLE}',conn)#IF WE DO THIS THEN WE DONT NEED TO DO CUR.FETCHALL
  



 df1['ROLLING_AVERAGE']=df1[WHICH_COLUMN].rolling(window=1).mean()#HERE I DID WHICH_COLUMN TO SEE SPECIFIC COLUMN
 #I ADDED THE 'ROLLING AVERAGE TO MEAN OF SPECIIFC COLUMN 
 return df1.to_dict(orient='records')#ORIENT=RECORDS E MEANS GIVE ME DATA OF ALL BUT IN DICITONARY CAUSE FASTPI READS AS JSON


@new.get('/totalrevenueofsales/')
def sales_summary():
  conn=mysql.connector.connect(host='localhost',user='root',password='password@123',database='PROJECT',unix_socket='/tmp/mysql.sock')
  cur=conn.cursor()
  
  ext=pd.read_sql('SELECT * FROM SALES',conn)
  
  
  val=ext.groupby('PRODUCT_ID',as_index=False).agg({'SALES_PRICE':'sum'})#it gives the sql columns inform of dataframe columns
  val1=val.to_records(index=False)#when we say index=false it means exclude index in form of numpydi gsal
  vals=val1.tolist()# we use .tolist instead of to_list(pandas) because we converted into numpy so we need numpy list function
  cur.execute("DELETE FROM SALES_SUMMARY")



  cur.executemany('INSERT INTO SALES_SUMMARY VALUES(%s,%s)',vals)
  
  
  
  conn.commit()

  ext2=pd.read_sql('SELECT * FROM SALES_SUMMARY',conn)
  cur.close
  conn.close()
  
  return ext2.to_dict(orient='records')

  
   
  
  
  

  
  

  
  
  
  




 




