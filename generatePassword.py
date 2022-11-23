import random
import string
import math
ss=list(string.ascii_letters + string.digits+'!@#$%^&*()' )

random.shuffle(ss)

l=[]

while True:
    

    inp=int(input('''
    1  enter  password length
    2  exit'''))

    if(inp == 1):
        inn=int(input("enter password length :"))

        for i in range(inn):
            l.append(random.choice(ss))
        l="".join(l)
        print(l)
    elif(inp == 2):
        print("successfully exit")
        break
    else:
        print("invalid number")
       



