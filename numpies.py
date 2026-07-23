import pandas as pd
import csv
import numpy as np
#with open('jj.csv','r')as e:
#    b=csv.reader(e)
#    for x in b:
#        print(x)

#d={1:'naga',
#   2:'saga',
#   3:'vaga'}
#with open('gaga.csv','w')as file:
#    csvs=csv.DictWriter(file,fieldnames=[1,2,3])
#    csvs.writeheader()
#    csvs.writerow(d)

#with open('gaga.csv','r')as files:
#    csvr=csv.DictReader(files)
#    for x in csvr:
#        print(x)
#reading arrays
a=np.array([1,2,3])
print(a)
b=np.array([[1,2,3,4,5,6,7,8],[3,4,5,5,6,7,8,4]],dtype='float')
print(b)
print(b.shape)
print(a.dtype)
print('this is data type',b.dtype)
print('this is size',b.size)
print("this is shape",b.shape)
print('this is item size',b.itemsize)

print("this is nbytes",b.nbytes)
print('this is item',b.item)
print(b[0,1:2])
print(b[:,:])
print(b[:,2:5])
ones=np.ones((2),dtype='int')
print(ones)
zeros=np.zeros((3,2))
print(zeros)
#same values you define the shape
sames=np.full((2,2),99,dtype='int')
print('this gives you same array',sames)
#copy the shape of another array
same_like=np.full_like(b,22)
print('this will give you values in same shape you define the array',same_like)

#for random decimals numbers
なんでも=np.random.rand(2,3)#so you see it gives you random decimal numbers no need to give shape in tuples
print('これはなんでも',なんでも)
#for to get the random but same shape of some array
copyninja=np.random.random_sample(b.shape)
print('so you need to specify the array.shape',copyninja)
#random integers values
integersdrand=np.random.randint(low=1,high=5,size=(2,3))
print('this will give you random integers',integersdrand)
#for repeating the values


#it will give you identity matrix
determenant=np.identity(2)
print('this will give you identity matrix',determenant)
d=np.random.random_sample(b.shape)
print(d)
#mathematics
number=np.array([[[3,4,5,6]],[[4,5,6,7]]])
print(number)
print(number+1)
print(number/2)
print(number*2)
print(number-1)
print(number**2)
print(np.cos(number))
print(np.sin(number))
#broadcasting#linalg
#for multiplying the array you need the array to be column of one array and row of another array to be same
mat=np.ones((2,3))
mul=np.zeros((3,2))
b=np.matmul(mat,mul)
print(b)
#linalg
lin=np.identity(3)
g=np.linalg.det(lin)
print(g)
#to repeat
re=np.array([[2,3,4,5],[4,5,6,7]])
re1=np.repeat(re,3,axis=1)#axis 1 means horix¥zontal and axis 0 means vertical
print(re1)
#statisctics
stat=[[[2,3,4,5],[5,6,7,8]]]
go=np.max(stat,axis=1)#axis 1 rows
#axis 0 is column
gow=np.min(stat,axis=1)
sum=np.sum(stat)
print(gow)
print(go)
print(sum)
#copying
copy=np.array([[3,4,5,6],[6,7,8,9]])
f=copy.copy()#so copy lets you have same but differenet location same like pandas
f[0,3]=33
print(copy)
#vstack and hstack
v1=np.array([[2,3,4,5],[5,6,7,8]])
v2=np.array([[3,4,5,6],[6,7,8,9]])
ver=np.vstack((v1,v2))
hor=np.hstack((v1,v2))
print(ver)
print(hor)
#reshaping the array
res=np.array([[3,4,5,6,],[5,6,7,8]])
rest=res.reshape((4,2))
print(rest)#reshaping the array
#loading the data into numpy
load=np.genfromtxt('nptext.txt',delimiter=',')
print(load)
#change the datatype
dty=load.astype('int32')
load=load.astype('int32')#same like we used to do in pandas
print(dty)
print(load)
print(load[load>2])#filtering data
#axis 0 is column and axis 1 is row
print(np.any(load>1,axis=0))
print(np.all(load>2,axis=0))
print(((load>2)&(load<12)))
print(load[(load>2)&(load<45)])
g=np.where(load==0,'none','everything fine')
print(g)

