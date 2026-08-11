#Menu driven program

import csv


def CreateTxt(x,y,z):
    f= open(filename,z)
    if z=="w" or z=="a":
        f.write(content)
        f.close()
        print("yaha pe create hori hain Text File")
    else:
        para = f.read()
        for i in para:
            print(i)

def CreateCsv(x,y,z):
    if z=="w"or z=="a":
        f=open(x,z,newline='')
        w=csv.writer(f)
        w.writerow([y])
        f.close()
        print("yaha pe create hori hain CSV File")
    else:
        f= open(x,'r')
        w= csv.reader(f)
        for i in w:
            print(i)
        
Flag = True
while Flag:
    print("1. Create Text File ?")
    print("2. Create CSV File ?")
    print("3. Exit")

    choice = int(input("Enter your Choice : "))
    if choice== 1:
        print("1. Create Text File ?")
        print("2. Update Text File ?")
        print("3. Read Text File ")
        print("4. Exit ")
        option = int(input("Enter your Choice : "))
        if(option==1):
            filename= input("Enter text file name(p.txt):")
            content= input("Enter your text file content:")
            CreateTxt(filename,content,"w")

        if option==2:
            filename= input("Enter text file name to update:")
            content= input("enter text file to append:")
            CreateTxt(filename,content,"a")

        if option==3:
            filename= input("Enter text file name to read:")
            content = ''
            CreateTxt(filename,content,"r")

        if option==4:
            print("Exting text file")

    if choice ==2:
        print("1. Create CSV File ?")
        print("2. Update CSV File ?")
        print("3. Read CSV File ")
        print("4. Exit ")
        option = int(input("Enter your choice:"))

        if option==1:
            filename= input("Enter CSV file name(j.csv):")
            content = input("Enter HEADER in the sequence of SNO , NAME, COURSE, DUE")
            CreateCsv(filename, content, "w")

        if option==2:
            filename= input("Enter CSV file name(j.csv):")
            content = input("Enter content in the sequence of SNO , NAME, COURSE, DUE")
            CreateCsv(filename, content,"a")

        if option==3:
            filename= input("Enter csv file name(j.csv):")
            CreateCsv(filename, "" ,"r")

        if option==4:
            print("Exting csv file")

            
    if choice ==3:
        flag = False


