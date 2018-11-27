# Learning Game

import random, tkinter, tkinter.ttk, sys
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
    newWindow.geometry("550x300")
    newWindow.title("Begin Game")

    label1 = tkinter.Label(newWindow, text= "\n\n\tAre you ready to play level " + str(currentLevel) + ', ' + str(player.name) + " ?",font=("Times New Roman", 20))
    label1.grid(column=1, row=2)


    startButton = tkinter.Button(newWindow, text="Start", bg="grey", fg="black", command=onClickStart)
    startButton.grid(column=1, row=10)


    newWindow.mainloop()
    #newWindow.protocol("WM_DELETE_WINDOW",sys.exit())

    for i in range(0,2):

        qWindow = tkinter.Tk()
        qWindow.geometry("700x700")
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
        #qWindow.protocol("WM_DELETE_WINDOW",sys.exit())
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

            #ansWindow.protocol("WM_DELETE_WINDOW",sys.exit())
            ansWindow.mainloop()
          
        else:

            ansWindow = tkinter.Tk()
            ansWindow.geometry("700x700")
            ansWindow.title("Result " + str(i+1))

            label1 = tkinter.Label(ansWindow, text= "\n\tYou are incorrect", font=("Times New Roman", 20))
            label1.grid(column=1, row=2)

            nextButton = tkinter.Button(ansWindow, text="Next Question", bg="grey", fg="black", command=onClickNext)
            nextButton.grid(column=1, row=5)

            questions.delQuestion(question,Correctanswer,answerChoices,idx)

            
            ansWindow.mainloop()
            #ansWindow.protocol("WM_DELETE_WINDOW",sys.exit())
        
def main():

    def onClickCombo():
        label.configure(text="input: " + combo.get())

    window = tkinter.Tk()
    window.geometry("700x700")
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
    #window.protocol("WM_DELETE_WINDOW",sys.exit())
    

    global userName
    

    #Game name
    #initate Player
    Student= Player(userName)
    level(1,Student)
    currentLevel=1
    keepPlaying = True
    while keepPlaying:
        if Student.score >=7.0:
            Scorewindow = tkinter.Tk()
            Scorewindow.geometry("700x700")
            Scorewindow.title("level " + str(currentLevel) + " Score")

            label1 = tkinter.Label(Scorewindow, text="\tScore:\t" + str(Student.score), font=("Times New Roman", 20))
            label1.grid(column=1, row=2)


            label2 = tkinter.Label(Scorewindow, text="\tYou Passed Level " + str(currentLevel) + "!\n\n", font=("Times New Roman", 20))
            label2.grid(column=1, row=5)

            quit = tkinter.Button(Scorewindow, text="Quit", bg="white", fg="red", command=sys.exit)
            quit.grid(column=1, row=8)

            Scorewindow.mainloop()

            currentLevel+=1
            keepPlaying = False
        else:

            Scorewindow = tkinter.Tk()
            Scorewindow.geometry("700x700")
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
    print("Have a nice day \n")
main()
