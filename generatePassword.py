import random
import string
import math
ss=list(string.ascii_letters + string.digits+'!@#$%^&*()' )

random.shuffle(ss)

l=[]



inp=int(input("Enter password length  :"))
for i in range(inp):
    l.append(random.choice(ss))
l="".join(l)
print(l)



