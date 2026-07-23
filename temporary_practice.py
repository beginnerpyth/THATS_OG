import csv
lis=[9,10,4,5,5,3]
lis.sort()
print(lis)
def fun():
    print(lis[len(lis)-2])
fun()


nums=[1,2,3,4,5,6]
for x in nums:
  if x%2==0:
     print(f'its a even number i.e {x}')
stringz='pasta'
#print(stringz[1:4:2])#start:stop:step means which directionn if negatve from backward
b=len(stringz)
print(b)
c=''
for x in range(1,b+1):
   
    c+=stringz[b-(x)]
print(c)
text='data engineering is fun data is powerful'
c=text.split()
print(c.count('data'))
print('data',text.count('data'))
print('engineering',text.count('engineering'))
#q6
#def pp():
#   count=0
#   a=int(input('enter a number'))
#   for o in range(1,a+1):
#      if a%o==0:
#       count=count+1
      
#   if count==2:
#     print('its  prime number')
#   else:
#     print('its not prime number')
#pp()
#q7

def rr():
   c=1
   n=int(input('enter a number'))
   for x in range(1,n+1):
      c=c*(x)
   print(c)
rr()

with open('try.csv','r')as e:
   file=csv.reader(e)
   for x in file(5):
      print(x)

           
