import random
print("rock " + " scissors " + " paper ")
li=['rock','scissors','paper']
ini=input(" Enter any above choice ")
ran=random.choice(li)
if(ini.lower()=="rock"):
    if(ran.lower()=="rock"):
        print("Your input is rock")
        print("computer input is also rock")
        print(" it Is Tie Game")
    elif(ran.lower()=="scissors"):
        print("Your input is rock")
        print("computer input is also scissors")
        print(" Computer won the Game")
    elif(ran.lower()=="paper"):
        print("Your input is rock")
        print("computer input is also paper")
        print(" Computer won theGame")
        
elif(ini.lower()=='scissors'):
    if(ran.lower()=='rock'):
        print("Your input is scissors")
        print("computer input is also rock")
        print(" computer won Game")
    elif(ran.lower()=='scissors'):
        print("Your input is scissors")
        print("computer input is also scissors")
        print(" Tie Game")
    elif(ran.lower()=='paper'):
        print("Your input is scissors")
        print("computer input is also paper")
        print(" Computer won theGame")
elif(ini.lower()=='paper'):
    if(ran.lower()=='rock'):
        print("Your input is paper")
        print("computer input is also rock")
        print(" computer won Game")
    elif(ran.lower()=='scissors'):
        print("Your input is paper")
        print("computer input is also scissors")
        print(" Computer won the Game")
    elif(ran.lower()=='paper'):
        print("Your input is paper")
        print("computer input is also paper")
        print(" Tie Game")
elif(ini.lower()=='exit'):
    print("Game ended")
    quit()
        

        
