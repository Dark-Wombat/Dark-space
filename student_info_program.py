'''
This is a program tha stores names and marks of students
in a dictioanry.

created by - @sumitjadhav
Thank you
'''

# a funciton to add name and marks to a dictionary
def new(dic, name, marks):
    x = int(marks)
    str1 = str(name)
    dic[str1] = x

#the dicitonary to store name and marks
dic1 = {}

#program code 
con = True
while con:
    print("---------------------")
    print("1.Input/Update data ")
    print("2.Show data and exit")
    print("3.exit")
    print("---------------------")

    #input for main menu
    input_1 = int(input("enter a choice : "))

    if input_1 == 1:
        y = str(input("student name : "))
        z = int(input("enter marks : "))
        new(dic1, y, z)
        
    elif input_1 == 2:
        print("---------------------")
        print("_STUDENT MARKS_")
        for key, value in dic1.items():
            print("-", key, "got", value , "marks")
        print("---------------------")

    elif input_1 == 3:
        print("exiting")
        break

    else:
        print("Invalid input")
        break



