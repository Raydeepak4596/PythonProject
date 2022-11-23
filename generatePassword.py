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

        for i in range(inp):
            l.append(random.choice(ss))
        l="".join(l)
        print(l)
    elif(inp == 2):
        break
    else:
        print("invalid number")
       



