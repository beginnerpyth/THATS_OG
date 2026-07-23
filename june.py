import csv
with open('jj.csv','r')as e:
    csv_reader=csv.reader(e)
    for x in csv_reader:
        print(x)
with open('jj.csv','a')as e:
    csv_writer=csv.writer(e)
    csv_writer.writerow('\n hello man')
