import random
while True:
    GCN=random.randrange(1,101)

    UGN=int(input("Enter your Guasing Number :"))
    if(GCN == UGN):
        print("You Won , Your Gausing number is {} and computer Guasing Number is {} Match ".format(UGN,GCN))
    else:
        print("You Failed , Your Gausing number is {} and computer Guasing Number is {} Match ".format(UGN,GCN))
   
