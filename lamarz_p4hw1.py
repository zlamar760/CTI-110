#Zachary LaMar
#11/5/24
#P4HW1
#Ask user how many grades they would like to input then display information

grade_num=int(input("How many scores do you want to enter? "))
grades=[]
x=1

for grade in range(grade_num):
    grade=float(input(f"Enter score #{x}: "))
    while grade<0 or grade>100:
        print("INVALID Score entered!!!!")
        grade=float(input(f"Enter score #{x} again: "))
    grades.append(grade)
    x+=1

print(grades)

low=min(grades)
grades.remove(low)
avg=sum(grades)/len(grades)

if avg>=90:
    letter="A"
elif avg>=80:
    letter="B"
elif avg>=70:
    letter="C"
elif avg>=60:
    letter="D"
else:
    letter="F"
    
print("--------------Results--------------")
print(f"{'Lowest Score':<14}{':':<3}{low}")
print(f"{'Modified List':<14}{':':<3}{grades}")
print(f"{'Scores Average':<14}{':':<3}{sum(grades)/len(grades):.2f}")
print(f"{'Grade':<14}{':':<3}{letter}")
