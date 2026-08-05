# CSV -> comma separated Value
import csv
def WriteCSV():
    f = open("j.csv","w",newline='')
    writer = csv.writer(f)
    writer.writerow(["SNO","NAME","COURSE"])
    writer.writerow([1,"Anisha","MERN"])
    writer.writerow([2,"Anshul","PERN"])
    writer.writerow([3,"Akshay","MEAN"])
    writer.writerow([4,"Aman","Python"])


f = open("j.csv",'r')
r = csv.reader(f)
for i in r:
    print(i)