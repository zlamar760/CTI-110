#Zachary LaMar
#9/19/24
#p1hw1
#Calculate travel expenses

print("This program calculates and displays travel expenses")
print()

#Obtain information
budget=int(input("Enter Budget: "))
print()
location=input("Enter your travel destination: ")
print()
gas=int(input("How much do you think you will spend on gas? "))
print()
hotel=int(input("Approximately, how much will you need for accomodations/hotel? "))
print()
food=int(input("Last, how much do you need for food? "))
print()

#Calculate remaining balance
balance=budget-(gas+hotel+food)

#Display information
print("------------Travel Expenses------------")
print("Location:",location)
print("Initial Budget:",budget)
print()

print("Fuel:",gas)
print("Accomodation:",hotel)
print("Food:",food)
print()

print("Remaining Balance:",balance)
