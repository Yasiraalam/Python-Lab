import random
total_Students ={}
def addStudent():
    studnetname  = input("Enter name :")
    studentmarks = int(input("Enter marks:"))
    total_Students[studnetname] = studnetname
    total_Students[studnetname] = studentmarks 

while True:
    choice = int(input("1:Enroll\n2:Show Students\n3:exit\n"))
    if choice==1:
        addStudent()
    elif choice ==2:
        print(total_Students)
        print("\n\n")
    elif choice ==3:
        print("Exit successfully")
        exit()
    else:
        print("Wrong choice")


    