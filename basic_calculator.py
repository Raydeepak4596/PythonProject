
def addition(a,b):
    strnum = a + b
    print(str(a) + " + " + str(b) + " = ", strnum + "\n")

def mul(a,b):
    strnum = a * b
    print(str(a) + "* " + str(b) + " = ", strnum + "\n")

def Div(a,b):
    strnum = a / b
    print(str(a) + " /" + str(b) + " = ", strnum + "\n")

def sub(a,b):
    strnum = a - b
    print(str(a) + " -" + str(b) + " = ", str(strnum) + "\n")


while True:
    print("A - Addition")
    print("B - Division")
    print("C - Multyplication")
    print("D - subtract")
    print("E - Exit")
    le=input("Enter Your choice")
    if(le=='a' or le=='A'):
        num1=int(input("Enter first number"))
        num2=int(input("Enter second number"))
        addition(num1,num2)
    elif(le=='b' or le=='B'):
        num1=int(input("Enter first number"))
        num2=int(input("Enter second number"))
        Div(num1,num2)
    elif(le=='c' or le=='C'):
        num1=int(input("Enter first number"))
        num2=int(input("Enter second number"))
        mul(num1,num2)
    elif(le=='d' or le=='D'):
        num1=int(input("Enter first number"))
        num2=int(input("Enter second number"))
        sub(num1,num2)
    elif(le=='e' or le=='E'):
        print("Program ended")
        quit()






