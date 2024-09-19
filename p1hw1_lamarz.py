#Zachary LaMar
#9/17/24
#P1HW1
#Input and ouptut with mathematical expressions

print("----Calculating Exponents----")
print()
print()

#Get base value from user
base=int(input("Enter an integer as the base value: "))
#Get exponent from user
expo=int(input("Enter an integer as the exponent: "))
exvalue=base**expo
print()
print()
print(base,"raised to the power of",expo,"is",exvalue,"!!")
print()
print()

print("----Addition and Subtraction----")
print()
print()

#Get starting value
asStart=int(input("Enter a starting integer: "))
#Get value to add by
add=int(input("Enter an integer to add: "))
##Get value to subtract by
sub=int(input("Enter an integer to subtract: "))
total=asStart+add-sub
print()
print()
print(asStart,"+",add,"-",sub,"is equal to",total)
