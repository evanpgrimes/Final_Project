# Learning Game

import random, tkinter, tkinter.ttk
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

def level(currentLevel,questions,player):
    player.resetScore()
    print(player.name + "'s Turn: \n")
    for i in range(0,10):
        question, Correctanswer, answerChoices, idx =questions.askQuestion()
        print(question + "\n")
        for i in range(0, len(answerChoices)):
            print(answerChoices[i])
        playerAnswer = input("\nWhat is your answer? \n")
        playerAnswer = playerAnswer.upper()
        if playerAnswer== Correctanswer:
            print("\nYou are correct \n")
            player.updateScore(1)
            questions.delQuestion(question,Correctanswer,answerChoices,idx)
        else:
            print("\nYou are incorrect \n")



def main():
    #Game name
    print("Eductation Game \n")
    name= input("What is your name? \n")
    #initate Player
    Student= Player(name)
    #Question reader
    #
    QA = Questions()
    readQuestions(QA,"test")
    print(QA.questions)
    print(QA.answerChoices)
    print(QA.answers)
    #
    level(1,QA,Student)
    keepPlaying = True
    while keepPlaying:
        if Student.score >=7.5:
            print("Congratulations, You passed the currentLevel \n")
        else:
            print("Sorry, you failed")
            replayLevel=input("Would you like to play the same level again? (y/n) \n")
            if replayLevel=="y":
                level(1,QA,Student)
                keepPlaying = False
    print("Have a nice day \n")
main()
