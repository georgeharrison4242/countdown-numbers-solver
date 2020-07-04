from generator import Generator
import time

class CountdownNumbers:
    # n: n numbers provided in any instance of the problem
    def __init__(self):
        self.generator = Generator()

    # solve: [Int], Int, Int -> [(String,Int)]
    # returns sols closest expression-value pairs to the solution
    def solve(self, ns, n, sols=10):
        choices = self.generator.genChoices(ns) # generate all number selections from ns
        closest = [] # sols closest results
        for c in choices:
            evs = self.generator.genExprs(c) # generate valid expr-value pairs
            for (e,v) in evs:
                delta = abs(v-n)
                if len(closest)<sols: # add first 10 results to closest
                    closest.append((str(e),v))
                else: # update closest with new value
                    j=sols-1
                    while j>=0 and abs(closest[j][1]-n)>delta: j-=1
                    closest = (closest[:j+1]+[(str(e),v)]+closest[j+1:])[:sols]

        return closest
