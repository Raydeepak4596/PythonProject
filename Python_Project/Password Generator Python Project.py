import random
import string
uin=int(input("how many length do you want to generate the password : ?"))
ss=list(string.ascii_letters + string.digits + '!@#$%^&*()')
random.shuffle(ss)
li=[]
for i in range(uin):
    li.append(random.choice(ss))
li="".join(li)
print(li)