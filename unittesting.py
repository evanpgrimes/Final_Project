import unittest
import Game

x=Game.Questions()
Game.readQuestions(x,"unittester.txt")

class Mytest(unittest.TestCase):
    def testFiles(self):
        self.assertEqual(x.numofQuestions(),1)
    
if __name__ == '__main__':
    unittest.main()
