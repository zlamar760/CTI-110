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

select=input("Enter a vehicle to see its mpg: ")
print(f"The {select} gets {cars_dict[select]} mpg.")


#Gives different output based on what the user inputs. First version, disabled
"""select=input("Enter a vehicle to see its mpg: ")
if select=="Camaro":
    print("The",select,"gets",cars_dict["Camaro"],"mpg.")
    miles=float(input("How many miles will you drive the Camaro?"))
    mpg=miles/cars_dict["Camaro"]
    print(float("%.2f"%mpg),"gallon(s) of gas are needed to drive the",select,miles)
elif select=="Prius":
    print("The",select,"gets",cars_dict["Prius"],"mpg.")
    miles=float(input("How many miles will you drive the Prius?"))
    mpg=miles/cars_dict["Prius"]
    print(float("%.2f"%mpg),"gallon(s) of gas are needed to drive the",select,miles)
elif select=="Model S":
    print("The",select,"gets",cars_dict["Model S"],"mpg.")
    miles=float(input("How many miles will you drive the Model S?"))
    mpg=miles/cars_dict["Model S"]
    print(float("%.2f"%mpg),"gallon(s) of gas are needed to drive the",select,miles)
elif select=="Silverado":
    print("The",select,"gets",cars_dict["Silverado"],"mpg.")
    miles=float(input("How many miles will you drive the Silverado?"))
    mpg=miles/cars_dict["Silverado"]
    print(float("%.2f"%mpg),"gallon(s) of gas are needed to drive the",select,miles)
else:
    print("Not an option.")"""
