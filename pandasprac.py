import pandas as pd
import mysql.connector
import csv
data={'1':['a','b','c'],
      '2':['d','e','f']}
df=pd.DataFrame(data,index=['a','b','c'])#so with data frame we can chaneg the index 
print(df)
#with orient in default the key is column but you ccan change into index but you need to do DataFrame.from_dict
df1=pd.DataFrame.from_dict(data,orient='index',columns=[1,2,3])#normally orient is column and orient means key
print(df1)
bios=pd.read_csv('bios.csv')
coffee=pd.read_csv('coffee.csv')
tr=pd.read_csv('try.csv')
print(bios.head(4))
print(coffee.head(5))
#with open('try.csv','w')as e:
##    files=csv.reader(e)
    #files.rea(['total_revenue','product_id'])
coffee['price']=13
print(coffee)
print(coffee[['Units Sold','price']])
g=coffee[['Units Sold','price']]
#see=list(g)
#print(see)
see=list(g.to_dict(orient='records'))
print(see)
conn=mysql.connector.connect(host='localhost',user='root',password='password@123',database='PROJECT', unix_socket='/tmp/mysql.sock')
cur=conn.cursor()
jus=pd.read_sql('SELECT * FROM SALES',conn)
print(jus)
pand_t=jus.groupby(['PRODUCT_ID']).agg({'SALES_PRICE':'sum'}).reset_index()
pasro=pand_t.to_records(index=False)#it only works in pandas and giove values stripping the indext because index = false and 
#to_records removes the olumn head by defaukrt
val=pasro.tolist()#we use tolist because when we do list() databaase refusre to read those 
#we use tolist() i.e numpyfun instead of pandas own to_list because to_records is numpy own function so
#we use tolist instead of to_list is because 


#pasro.remove('SALES_PRICE')

cur.executemany('INSERT INTO TRY VALUES(%s,%s)',val)
cur.close()
conn.commit()
print(coffee)
coffee1=coffee.groupby('Day').agg({'price':'sum','total_r':'Units Sold'*'price'})
print(coffee1)



    #print(files['total_revenue'])




    