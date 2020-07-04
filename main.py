from countdownnumbers import CountdownNumbers
from prettyprinter import ExprPrinter
import sys

if __name__=="__main__":

    numbers = sys.argv[1:]

    try:
        numbers = list(map(lambda x: int(x), numbers))


        target = numbers[0]
        workingNumbers = numbers[1:]

        solver = CountdownNumbers()
        solutions = solver.solve(workingNumbers,target,3)

        pprinter = ExprPrinter()
        for (e,v) in solutions:
            pprinter.pprint(e)

    except:
        raise ValueError("must provide >=2 integers: targetNum, num1, num2, etc.")
    