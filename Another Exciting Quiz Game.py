print("--------------Welcome In My Quiz Game*----------------")
x=input("To start the game, enter YES otherwise EXIT  ").lower()
if x=="yes":
    print("Some information and rules about the game are given below:      \n1.All questions carry 2 marks each. \n2.There is no negative marking")
    print("3.Answer should be given as true & false OR t&f \n4.Answering all the questions is mandatory \n5.Score display at last")
    score=0
    q1=input("Ques 1. There are 206 to 213 bones in adult human body.   ").lower()
    if q1=="true" or q1=="t":
        print("The answer is correct.")
        score+=2
    else:
        print("Better luck next time.")
    q2=input("Ques 1. Zero is invented by Aryabhatta.   ").lower()
    if q2=="true" or q2=="t":
        print("The answer is correct.")
        score+=2
    else:
        print("Better luck next time.")
    q3=input("Ques 3. Independence Day is celebrated on 26th January.   ").lower()
    if q3=="false" or q3=="f":
        print("The answer is correct.")
        score+=2
    else:
        print("Better luck next time.")
    q4=input("Ques 4. 3-2(2+1)+4*5=23   ").lower()
    if q4=="true" or q4=="t":
        print("The answer is correct.")
        score+=2
    else:
        print("Better luck next time.")
    q5=input("Ques 5. PYTHON is an english language used to communicate between people.   ").lower()
    if q5=="false" or q5=="f":
        print("The answer is correct.")
        score+=2
    else:
        print("Better luck next time.")
else:
    print("Okay bye")
print("Score obtained is:",score)
