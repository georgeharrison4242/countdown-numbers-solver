from generator import Generator
import time

class CountdownNumbers:
    # n: n numbers provided in any instance of the problem
    def __init__(self):
        self.generator = Generator()

    # solve: [Int], Int, Int -> [(String,Int,Expression)]
    # returns sols closest expression-value pairs to solution
    # expressions can be converted to a convenient str representation with str(e) or pretty-printed
    def solve(self, ns, n, sols=10):
        choices = self.generator.genChoices(ns) # generate all number selections from ns
        closest = [] # sols closest results
        for c in choices:
            evs = self.generator.genExprs(c) # generate valid expr-value pairs
            for (e,v) in evs:
                delta = abs(v-n)

                if len(closest)<sols: # add first sols results to closest
                    closest.append((e,v))
                else: # update closest with new value
                    j=sols-1
                    while j>=0 and abs(closest[j][1]-n)>delta: j-=1
                    closest = (closest[:j+1]+[(e,v)]+closest[j+1:])[:sols]

        return closest

    # check: [String] , [Int], Int -> Bool
    # sol is a list of expressions in string form, i.e. sol=["5x4=20","20-1=19","19*25=475"]
    def check(self, sol, ns, n):
        pass
        #parser = Parser()

