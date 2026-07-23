import csv
b='try.csv'
with open(b,'r')as e:
    d=csv.reader(e)#so anythihg read or write we use loop because it is stored in object in list dtypes
    #next(d)
    #next(d)#it skips
#with open('gaga.csv','w')as k:
#    new=csv.writer(k,delimiter='-')
    for x in d:
        print(x)
data=[['rabi',33,'m'],
      ['kpoli',55,'m'],
      ['kulman',44,'m']]
with open('kaka.csv','w')as new:
    csv_write=csv.writer(new)#writer garera ani writerow garney memo

    for x in data:
        csv_write.writerow(x)   #we use writerow for adding data in csv
with open('ps.csv','w')as files:
    new_file=csv.writer(files)
    for x in data:
        new_file.writerow(x)
        