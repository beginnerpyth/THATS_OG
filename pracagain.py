import csv
with open('textallknowledge.txt','w')as e:
    #print(e.readlines())
    
    #print(e.readline())
    #print(e.read())
    e.write('just string we use .write() and we use"w" for removing whole text and adding new text' )
    e.writelines(["we use writelines to add list of text like when we do readlines and writeline is like readline"])
data_for_csv=['2,3,2,4,we put data into strings for csv adn we use w for deleteing and writig new data'
'while for adding new data we use a and we use .writer and .reader unlike text files readline and writelines '
'just like we read csv in loop we add data in loop'
]
dictforcsv={'1':('abhishek','amir','samir','vrataa and when we use dictwriter or dictreader unlike csv.writer/reader'
'we dont use loop when we write and we have to mention storedfile.writeheader() and we need to give fieldnames'
' and when we read we use loop and print(loop[''header''],loop["header])'),
            '2':('22','27','23','25')}
with open('fileallknowledge.csv','w')as csvs:
   dictwithcsv=csv.DictWriter(csvs,fieldnames=('1','2'))
   dictwithcsv.writeheader()
   dictwithcsv.writerow(dictforcsv)

    
    #csvs_write=csv.writer(csvs)
    #csvs_read=csv.reader(csvs)

    #for x in csvs_read:
     #print(x)
    #for x in data_for_csv:
     #  csvs_write.writerow(x)
with open('fileallknowledge.csv','r')as dicts:
   #dictwithcsv=csv.DictWriter(dicts,fieldnames=('1','2'))
   dictsforr=csv.DictReader(dicts)
   for j in dictsforr:
       print(j['1'],j['2'])

   
   #dictwithcsv.writerow(dictforcsv)
   


