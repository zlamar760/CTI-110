#Zachary LaMar
#9/26/24
#P2Lab2
#Create dictionaries with cars and their gas mileage value then tell the user how many gallons of gas they need for the distance they will drive.

#Create a dictionary
cars_dict={
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26,
}

cars=cars_dict.keys()
print(cars)

#Prompt user for vehicle and display its mpg
select=input("Enter a vehicle to see its mpg: ")
print(f"The {select} gets {cars_dict[select]} mpg.")
print()

#Prompt user for amount of miles they will drive
miles=int(input(f"How many miles will you drive {select}?: "))

#Calculate amount of gallons needed and display it
mpg=miles/cars_dict[select]
print(float("%.2f"%mpg),"gallon(s) of gas are needed to drive the",select,miles)
