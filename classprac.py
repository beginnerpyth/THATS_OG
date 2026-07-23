
import csv
#data=[[1,2,3],[4,5,6],[7,8,9]]
#with open('try.csv','a')as e:
#    file=csv.writer(e)
#    for x in data:
 #       file.writerow(x)
#k=input('enter a text')
#with open('try.csv','a')as new_file:
 #   new_file.write(k)#we use write to add singler string and same like txt file we use var ex new_file.write
                      #unlike othrcsv we need to do csv.writer(new_file)and do csv.writerow([23333,333])
                      #
with open('try.csv','r')as e:
    j=csv.reader(e)
    for x in j:
        print(x)
    
