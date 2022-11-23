import math
principal_Amount=int(input("enter Principal Amount :"))
Interest_rate=float(input("Enter interest rate :"))
Time=int(input("Enter Duration :"))
cal=principal_Amount * (1 + Interest_rate/100)**Time
s=math.floor(cal)
print("Total amount of :" + str(s))