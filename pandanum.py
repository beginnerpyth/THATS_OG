import pandas as pd
import numpy as np
coffee=pd.read_csv("coffee.csv")
print(coffee.head())
coffee["price"]=np.where(coffee['Units Sold']==25,33,coffee["Units Sold"])
print(coffee)
coffee['new_price']=coffee['price'].apply(lambda x:22 if x>20 else 33 if x>30 else 50 )
print(coffee)
coffee['level']=coffee['new_price'].apply(lambda x:'low' if x < 23 else 'medium' if x < 34 else 'high')
print(coffee)
seperating=coffee.groupby(coffee['Day']).agg({'Units Sold':'sum','price':'sum'})
print(seperating)
sorting=coffee.sort_values(['Day','Coffee Type'],ascending=(0,1))#[['Day','Coffee Type']]#sorting the day by descending and coffe type wt ascending
print(sorting)
coffee['sum_over']=coffee['price'].expanding().sum()#sum by beginning to end in sql average over by current row to preceeding row
print(coffee)
coffee['mean']=coffee['new_price'].rolling(window=3).sum()#in get the sum of 3 days
print(coffee)
coffee['rank']=coffee['Units Sold'].rank(method='dense')#in sql we use dense_rank
print(coffee)
coffee['difference']=coffee['new_price'].shift(1)#in sql we use lag
print(coffee)
coffee['up_ward']=coffee["new_price"].shift(-1)#it gives you the value in upward -1 takes value from below an in mysql it is known as mlead 
print(coffee)

