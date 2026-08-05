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


def ReadCSV():
    f = open("j.csv",'r')
    r = csv.reader(f)
    for i in r:
        print(i)


def AppendCSV():
    f = open("j.csv","a",newline='')
    d = csv.writer(f)
    d.writerow([5,"Anurag","Java"])

choice = True
while choice:
    print("1. Write CSV")
    print("2. Read CSV")
    print("3. Append CSV")
    print("4. EXIT")

    choice1= int(input("enter your choice:"))
    
    if choice1 ==1:
        WriteCSV()
    elif choice1 ==2:
        ReadCSV()
    elif choice1 ==3:
        AppendCSV()
    elif choice1 ==4:
        choice = False
    else:

        print("Invalid Choice, please enter a number between 1 and 3.")

    