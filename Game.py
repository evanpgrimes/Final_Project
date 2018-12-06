# Learning Game

import random, tkinter, tkinter.ttk, sys, turtle, os


class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.level = 1
        self.HighScore = 1

    def getScore(self):
        return (self.score)

    def getLevel(self):
        return (self.level)

    def getHighScore(self):
        return (self.HighScore)

    def updateScore(self, points):
        self.score += points

    def resetScore(self):
        self.score =0

    def __str__(self):
        return '{}\'s score is {}'.format(self.name, self.score)


class Questions:
    def __init__(self):
        self.questions = []
        self.answers = []
        self.answerChoices = []

    def numofQuestions(self):
        return(len(self.questions))

    def askQuestion(self):
        idx = random.randint(0,len(self.questions)-1)
        question = self.questions[idx]
        answer = self.answers[idx]
        choices = self.answerChoices[idx]

        return question, answer, choices, idx

    def delQuestion(self, question, answer, choices,idx):
        del self.questions[idx]
        del self.answers[idx]
        del self.answerChoices[idx]



def readQuestions(QA,file):
    file = open(file,'r')
    lines = [line.rstrip('\n') for line in file]

    for line in lines:
        questions = []
        answerChoices = []

        count = 0

        line = line.split("~")

        QA.questions.append(line[0])
        QA.answers.append(line[-1])
        choices = []

        # Get answer choices
        for i in range(1,len(line)-1):
            choices.append(line[i])

        QA.answerChoices.append(choices)

def level(currentLevel,player):
    
    def onClickStart():
        newWindow.destroy()

    def onClickEnter():
        global playerAnswer
        playerAnswer = str(Answer.get())
        qWindow.destroy()
    
    def onClickNext():
        ansWindow.destroy()

    player.resetScore()
    #Question reader
    #
    questions = Questions()
    readQuestions(questions,str("Questions_Level_"+str(currentLevel)+".txt"))
    
    

    newWindow = tkinter.Tk()
    newWindow.geometry("3000x2000")
    newWindow.title("Begin Game")

    label1 = tkinter.Label(newWindow, text= "\n\n\tAre you ready to play level " + str(currentLevel) + ', ' + str(player.name) + " ?",font=("Times New Roman", 20))
    label1.grid(column=1, row=2)

    startButton = tkinter.Button(newWindow, text="Start", bg="grey", fg="black", command=onClickStart)
    startButton.grid(column=1, row=10)

    newWindow.mainloop()
    # newWindow.protocol("WM_DELETE_WINDOW",sys.exit())

    for i in range(0,2):

        qWindow = tkinter.Tk()
        qWindow.geometry("2000x2000")
        qWindow.title("Question " + str(i+1))

        question, Correctanswer, answerChoices, idx =questions.askQuestion()

        qString = ''
        qString = qString + question + "\n"
        for i in range(0, len(answerChoices)):
            qString = qString + "\n" + answerChoices[i]

        labelTxt = qString
        label2 = tkinter.Label(qWindow, text=str(labelTxt), font=("Times New Roman", 20))
        label2.grid(column=1, row=6)
        Answer = tkinter.Entry(qWindow, width=10)
        Answer.grid(column=1, row=7)

        EnterButton = tkinter.Button(qWindow, text="Enter", bg="grey", fg="black", command=onClickEnter)
        EnterButton.grid(column=1, row=18)

        qWindow.mainloop()
        # qWindow.protocol("WM_DELETE_WINDOW",sys.exit())
        global playerAnswer

        playerAnswer = playerAnswer.upper()

        if playerAnswer== Correctanswer:

            ansWindow = tkinter.Tk()
            ansWindow.geometry("700x700")
            ansWindow.title("Result " + str(i+1))

            label1 = tkinter.Label(ansWindow, text= "\n\tYou are correct!!", font=("Times New Roman", 20))
            label1.grid(column=1, row=2)

            nextButton = tkinter.Button(ansWindow, text="Next Question", bg="grey", fg="black", command=onClickNext)
            nextButton.grid(column=1, row=5)

            player.updateScore(1)
            questions.delQuestion(question,Correctanswer,answerChoices,idx)

            # ansWindow.protocol("WM_DELETE_WINDOW",sys.exit())
            ansWindow.mainloop()
          
        else:

            ansWindow = tkinter.Tk()
            ansWindow.geometry("2000x2000")
            ansWindow.title("Result " + str(i+1))

            label1 = tkinter.Label(ansWindow, text= "\n\tYou are incorrect", font=("Times New Roman", 20))
            label1.grid(column=1, row=2)

            nextButton = tkinter.Button(ansWindow, text="Next Question", bg="grey", fg="black", command=onClickNext)
            nextButton.grid(column=1, row=5)

            questions.delQuestion(question,Correctanswer,answerChoices,idx)

            ansWindow.mainloop()
            # ansWindow.protocol("WM_DELETE_WINDOW",sys.exit())


# Note: a perfect score reads in 10 but any other new score besides 0 resets
# high score to that number
def level_high_score(level, score):
    file_1 = open("High Scores.txt", "r+")
    scoreList = []
    for line in file_1:
        x = line.rstrip('\n')
        scoreList.append(x)

    file_1 = open("High Scores.txt", "w")
    count = 1
    line = 0
    while count <= 3:
        x = int(scoreList[line][-1])
        if count == level:
            if score > x:
                file_1.write(scoreList[line][0:9] + str(score) + "\n")
            else:
                file_1.write(scoreList[line] + "\n")
        else:
            file_1.write(scoreList[line] + "\n")
        count += 1
        line += 1



def pong_game():
    wn = turtle.Screen()
    wn.title("Pong")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    wn.tracer(0)

    # Score
    score_a = 0
    score_b = 0

    # Paddle A
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=5,stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350, 0)

    # Paddle B
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=5,stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)

    # Ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 2
    ball.dy = 2

    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

    # Functions
    def paddle_a_up():
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)

    def paddle_a_down():
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)

    def paddle_b_up():
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

    def paddle_b_down():
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)

    # Keyboard bindings
    wn.listen()
    wn.onkeypress(paddle_a_up, "w")
    wn.onkeypress(paddle_a_down, "s")
    wn.onkeypress(paddle_b_up, "Up")
    wn.onkeypress(paddle_b_down, "Down")
    flag = True
    # Main game loop
    while flag == True:
        
            wn.update()

            # Move the ball
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

            # Border checking

            # Top and bottom
            if ball.ycor() > 290:
                ball.sety(290)
                ball.dy *= -1
                os.system("afplay bounce.wav&")

            elif ball.ycor() < -290:
                ball.sety(-290)
                ball.dy *= -1
                os.system("afplay bounce.wav&")

            # Left and right
            if ball.xcor() > 350:
                score_a += 1
                pen.clear()
                pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
                ball.goto(0, 0)
                ball.dx *= -1

                if score_a >= 3:
                    flag = False

            elif ball.xcor() < -350:
                score_b += 1
                pen.clear()
                pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
                ball.goto(0, 0)
                ball.dx *= -1

                if score_b >= 3:
                    flag = False
            # Paddle and ball collisions
            if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
                ball.dx *= -1
                os.system("afplay bounce.wav&")

            elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
                ball.dx *= -1
                os.system("afplay bounce.wav&")

    wd.exitonclick()

def main():
    

    def onClickCombo():
        label.configure(text="input: " + combo.get())

    window = tkinter.Tk()
    window.geometry("2000x2000")
    window.title("Learning is Fun!")

    # Switch frames
    def raiseFrame(frame):
        frame.tkraise()

    # when quitButton is clicked, the GUI window will close and the application will be aborted
    def closeWindow(wndw):
        wndw.destroy()
        exit() # comment this out to use command line

    def onClickSubmit():
        global userName   
        userName = str(text.get())
        window.destroy()

    def onClickRepeat():
        global replayLevel
        replayLevel = str(replay.get())
        Scorewindow.destroy()

    def onClickPong():
        pong_game()

    def onClickNext():
        Scorewindow.destroy()
        level(currentLevel+1,Student)


    label1 = tkinter.Label(window, text="\tWelcome to our Education Game!\n\n", font=("Times New Roman", 20))
    label1.grid(column=1, row=2)

    labelTxt = "User Name (one word): "
    label2 = tkinter.Label(window, text=str(labelTxt), font=("Times New Roman", 20))
    label2.grid(column=1, row=6)
    text = tkinter.Entry(window, width=10)
    text.grid(column=1, row=7)

    label3 = tkinter.Label(window, text="\n\n\tYou will begin on Level 1 with 0 Game Credits\n\n", font=("Times New Roman", 20))
    label3.grid(column=1, row=10)

    quitButton = tkinter.Button(window, text="Quit", bg="white", fg="red", command=lambda:closeWindow(window))
    quitButton.grid(column=2, row=0)

    submitButton = tkinter.Button(window, text="Submit", bg="grey", fg="black", command=onClickSubmit)
    submitButton.grid(column=1, row=18)

    window.mainloop()
    # window.protocol("WM_DELETE_WINDOW",sys.exit())

    global userName

    # Game name
    # initate Player
    Student= Player(userName)
    level(1,Student)
    currentLevel=1
    keepPlaying = True
    level_high_score(currentLevel,Student.score)
    while keepPlaying:
        if Student.score >=1.0:
            Scorewindow = tkinter.Tk()
            Scorewindow.geometry("2000x2000")
            Scorewindow.title("level " + str(currentLevel) + " Score")

            label1 = tkinter.Label(Scorewindow, text="\tScore:\t" + str(Student.score), font=("Times New Roman", 20))
            label1.grid(column=1, row=2)


            label2 = tkinter.Label(Scorewindow, text="\tYou Passed Level " + str(currentLevel) + "!\n\n", font=("Times New Roman", 20))
            label2.grid(column=1, row=5)

            quit = tkinter.Button(Scorewindow, text="Quit", bg="white", fg="red", command=sys.exit)
            quit.grid(column=2, row=15)

            PlayPong = tkinter.Button(Scorewindow, text="Play Pong?", bg="grey", fg="black", command=onClickPong)
            PlayPong.grid(column=1, row=8 )


            NextLevel = tkinter.Button(Scorewindow, text="Next Level", bg="grey", fg="black", command=onClickNext)
            NextLevel.grid(column=3, row=8 )


            Scorewindow.mainloop()

            currentLevel+=1
    
        else:

            Scorewindow = tkinter.Tk()
            Scorewindow.geometry("2000x2000")
            Scorewindow.title("level " + str(currentLevel) + " Score")

            label1 = tkinter.Label(Scorewindow, text="\tScore:\t" + str(Student.score), font=("Times New Roman", 20))
            label1.grid(column=1, row=2)

            label2 = tkinter.Label(Scorewindow, text="\tYou Failed Level " + str(currentLevel) + "\n\n", font=("Times New Roman", 20))
            label2.grid(column=1, row=5)

            labelTxt = "Would you like to play the same level again? (y/n) \n"
            label3 = tkinter.Label(Scorewindow, text=str(labelTxt), font=("Times New Roman", 20))
            label3.grid(column=1, row=10)
            replay = tkinter.Entry(Scorewindow, width=10)
            replay.grid(column=1, row=12)

            RepeatButton = tkinter.Button(Scorewindow, text="Enter", bg="grey", fg="black", command=onClickRepeat)
            RepeatButton.grid(column=1, row=18)


            Scorewindow.mainloop()

            global replayLevel

            if replayLevel=="y":
                level(1,Student)
            else:
                keepPlaying = False
                sys.exit()
    


main()
