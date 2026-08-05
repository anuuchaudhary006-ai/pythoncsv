# CSV -> comma separated Value
import csv
f = open("j.csv","w",newline='')
writer = csv.writer(f)
writer.writerow(["SNO","NAME","COURSE"])
writer.writerow([1,"Anisha","MERN"])