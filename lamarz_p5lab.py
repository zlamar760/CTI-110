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

import random


def calcCashback():
    #Generate random float for amount owed
    owed=round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${owed:.2f}")
    
    #Get money value from user as a float
    cash=float(input("How much cash will you put in the self-checkout? $"))

    #Calculate change owed
    change=cash-owed
    return change
    

def disperseChange(money):
    #Convert money to whole number
    money=round(money*100)
    
    #If user puts 0.00
    if money==0:
        print("No change")

    #Consider debt
    if money<0:
        print("Not enough money!")

    if money>0:
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

    else:
        d=0
        q=0
        di=0
        n=0
        p=0

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


#Define main class
def main():
    change=calcCashback()
    print(f"Change is: ${change:.2f}")
    disperseChange(change)

#Call the main
if __name__=="__main__":
    main()
