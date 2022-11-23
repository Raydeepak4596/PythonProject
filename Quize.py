Quize={
    "QUESTION1":
    {
        'Question' : 'What is the capital of bihar ?',
        'Answer':'Patna'
    },
    "QUESTION2":
    
    {
        'Question' : 'What is the capital of Rajsthan ?',
        'Answer':'jaipur'
    },
    "QUESTION3":
    {
        'Question' : 'What is the capital of Uttar Pradesh ?',
        'Answer':'Lucknow'
    },
    "QUESTION4":
    {
        'Question' : 'What is the capital of Goa ?',
        'Answer':'Panji'
    },
    "QUESTION5":
    {
        'Question' : 'What is the capital of Jharkhand ?',
        'Answer':'Ranchi'
    },
    
}
score = 0
for key,i in Quize.items():
    
    
    print(i['Question'])
    answer= input('Answer ?')
    if(answer.lower()== i['Answer'].lower()):
        
        print("correct ")
        score= score + 1
        print(" Your Score is :" + str(score) + "\n")
        
    else:
        print("Wrong")
        print(" Answer is : " + i['Answer'])
print(" You got Score : " + str(score))