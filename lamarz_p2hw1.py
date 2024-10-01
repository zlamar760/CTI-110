#Zachary LaMar
#9/19/24
#p1hw1
#Calculate travel expenses

print("This program calculates and displays travel expenses")
print()

#Obtain information
budget=float(input("Enter Budget: "))
print()
location=input("Enter your travel destination: ")
print()
gas=float(input("How much do you think you will spend on gas? "))
print()
hotel=float(input("Approximately, how much will you need for accomodations/hotel? "))
print()
food=float(input("Last, how much do you need for food? "))
print()

#Calculate remaining balance
balance=budget-(gas+hotel+food)

#Display information
print("------------Travel Expenses------------")
print(f"Location: {location}")
print(f"Initial Budget: ${budget:.2f}")
print()

print(f"Fuel: ${gas:.2f}")
print(f"Accomodation: ${hotel:.2f}")
print(f"Food: ${food:.2f}")
print("---------------------------------------")
print()

print(f"Remaining Balance: ${balance:.2f}")
