year=int(input("Enter any year"))
if(year %4==0):
    if(year%100):
        if(year%400):
            print("Leap Year")
        else:
            print(" not leap year")
    else:
        print("leap year")
else:
    print("not leap year")