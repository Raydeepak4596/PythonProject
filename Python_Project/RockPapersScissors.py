import random
l=['Rock','Scissors','Paper']
print("Choose Any one : [ Paper  , Rock  , Scissors ]")
un=input("Enter Here Your choice :")
cn=random.choice(l)
if(un == cn):
    print("your Guasing Match")
    print("Your Gusing is {}".format(un))

    print("Computer Gusing Word : {}".format(cn))
else:
    print("your Guasingnot  Match")
    print("Your Gusing is {}".format(un))

    print("Computer Gusing Word : {}".format(cn))
