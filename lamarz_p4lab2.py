#Zachary LaMar
#P4Lab2
#10/31/24
#Asks user for integer and display multiplication table


#While loop to control program running continuously
cont="y"

while cont=="y":
    num=int(input("Enter an integer: "))
    print()
    
    if num>=0:
        #Increment x by 1 where x is the number num is being multiplied by (1-12)
        for x in range(1,13):
            #Print multiplication table
            print(f"{num} * {x} = {num*x}")
    else:
        print("This program does not handle negative numbers")
        
    print()
    cont=input("Would you like to run the program again? ").lower()[0]
    
    #Validating user input
    '''valid_inputs=["yes", "y", "no", "n"]
    while cont not in valid_inputs:
        cont=input("Please enter yes or no: ")
    '''
    while cont!="y" and cont!="n":
        cont=input("Please enter yes or no: ").lower()[0]
    print()
    
#Loop breaks
print("Exiting program...")
