#Zachary LaMar
#10/17/24
#P3HW1
#Obtain grades for several modules and calculate the sum and average

#Obtain the grades from user and put them in list
grades=[
float(input("Enter the grade for Module 1: ")),
float(input("Enter the grade for Module 2: ")),
float(input("Enter the grade for Module 3: ")),
float(input("Enter the grade for Module 4: ")),
float(input("Enter the grade for Module 5: ")),
float(input("Enter the grade for Module 6: "))]
print()
avg=sum(grades)/len(grades)
#Print results using functions
print("------------Results------------")
print(f"{'Lowest Grade: ':<18}{min(grades):.1f}")
print(f"{'Highest Grade: ':<18}{max(grades):.1f}")
print(f"{'Sum of Grades: ':<18}{sum(grades):.1f}")
print(f"{'Average: ':<18}{avg:.2f}")
print("------------------------------------------")

#Branching to determine letter grade
letter=""
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

print(f"Your grade is: {letter}")
