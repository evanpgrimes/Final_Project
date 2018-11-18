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

        for i in range(1,len(line)-1):
            choices.append(line[i])

        QA.answerChoices.append(choices)





def main():
    QA = Questions()
    readQuestions(QA,"test")
    print(QA.questions)
    print(QA.answerChoices)
    print(QA.answers)

main()
