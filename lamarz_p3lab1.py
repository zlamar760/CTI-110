#Zachary LaMar
#10/17/24
#P3LAB1
#Calculate coin combinations for given value

'''#Regular Division
print(100/3)

#Floor Division
print(100//3)

#Modulus Division
print(100%3)
'''

#Get money value from user as a float
money=float(input("Enter the amount of money as a float: $"))

#Convert money to whole number
money=round(money*100)
if money==0:
    print("No change")
#Calculate the amount of dollars in money variable
d=money//100

#Remove number of dollars from money
money=money-(d*100)

#Calculate quarters
q=money//25
money=money-(q*25)

#Calculate dimes
di=money//10
money=money-(di*10)

#Calculate nickels
n=money//5
money=money-(n*5)

#Calculate pennies
p=money

#Begin statements. If any currency is one print singular word. Else print plural.
if d>0:
    if d==1:
        print(f"{d} Dollar")
    else:
        print(f"{d:,} Dollars")
if q>0:
    if q==1:
        print(f"{q} Quarter")
    else:
        print(f"{q} Quarters")
if di>0:
    if di==1:
        print(f"{di} Dime")
    else:
        print(f"{di} Dimes")
if n>0:
    if n==1:
        print(f"{n} Nickel")
    else:
        print(f"{n} Nickels")
if p>0:
    if p==1:
        print(f"{p} Penny")
    else:
        print(f"{p} Pennies")
