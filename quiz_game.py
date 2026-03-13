#Quiz game
questions = ["*What is capital of india?","*Which animal is called the king of the jungle?","*How many days are there in a week?"]
answers = [1,2,3]
options = [["1.Delhi","2.Mumbai","3.Chennai"],["1.Tiger","2.Lion","3.Elephant","4.Dog"],["1.5","2.6","3.7","4.8"]]
score = 0
def quiz():
    global score
    for i in range(len(questions)):
        print(questions[i])
        for opt in options[i]:
            print(opt)
        user = int(input("Enter your answer:"))
        if user == answers[i]:
            print("Correct answer")
            score+=1
        else :
            print("Wrong answer")
def result():
    print("Quiz Finished")
    print("Score:",score,"/",len(questions))
    percentage = (score/len(questions))*100
    print("Percentage:",percentage)
quiz()
result()