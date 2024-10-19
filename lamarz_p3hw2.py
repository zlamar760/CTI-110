#Zachary LaMar
#10/17/24
#P3HW2
#Get employ name and calculate their pay

name=input("Enter employee's name: ")
hours=float(input("Enter number of hours worked: "))
rate=float(input("Enter employee's pay rate: "))
print("-------------------------------------")
print(f"Employee name: {name}")
print()

if hours>40:
    over=hours-40
    over_pay=rate*1.5*over
    pay=(hours-over)*rate
else:
    over=0
    over_pay=0
    pay=rate*hours
gross=pay+over_pay
print(f"{'Hours Worked':<14} {'Pay Rate':<14} {'OverTime':<14} {'OverTime Pay':<19} {'RegHour Pay':<19} {'Gross Pay'}")
print("---------------------------------------------------------------------------------------------------------------")
print(f"{hours:<14} ${rate:<13} {over:<14} ${over_pay:<18,.2f} ${pay:<18,.2f} ${gross:.2f}")
