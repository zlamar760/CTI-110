#Zachary LaMar
#10/1/24
#P2HW2
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

#Print results using functions
print("------------Results------------")
print(f"Lowest Grade: {min(grades):.1f}")
print(f"Highest Grade: {max(grades):.1f}")
print(f"Sum of Grades: {sum(grades):.1f}")
print(f"Average: {sum(grades)/len(grades):.2f}")
