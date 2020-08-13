from countdownnumbers import CountdownNumbers
from prettyprinter import ExprPrinter
import random

class Model:
    def __init__(self):
        self.solver = CountdownNumbers()
        self.currentNums = None
        self.target = None

    def setCurrentNumbers(self, numbers):
        assert(len(numbers)==6)
        self.currentNums = numbers

    def setRandomNumbers(self, returnSorted=True):
        selection = [1,2,3,4,5,6,7,8,9,10,25,50,75,100]
        self.currentNums = [random.choice(selection) for i in range(6)]
        if returnSorted:
            self.currentNums.sort(reverse=True)
        return self.currentNums


    def pickTarget(self):
        self.target = random.randrange(100,1000)
        return self.target

    def solve(self):
        if self.currentNums is None or self.target is None:
            return "Must have a target and numbers to solve"

        solution = self.solver.solve(self.currentNums, self.target, 1)[0]

        pprinter = ExprPrinter()
        return pprinter.prettyString(solution[0])

    def check(self):
        return False