import csv
with open('try.csv','r')as e:
    file=csv.reader(e)
    for x in file:
        print(x)

d={'name':['prateek','kalesh'],
    'age':[12,13]}
with open('jj.csv','w')as w:
  mew_file=csv.DictWriter(w,fieldnames=('name','age'))
  mew_file.writeheader()
  mew_file.writerow(d)

  
  
with open('jj.csv','r')as b:
     new_file=csv.DictReader(b)
     for j in new_file:
        print(j)

#read(),readlines(),readline(),write(),writelines(),reader(),writer(),DictWriter(),DictReader(),writerow(),fieldnames,writeheader()
#doesnt need loop to write in dictionary unlike normal csv and csv
#we use writerow to write for dictionary and normal csv
