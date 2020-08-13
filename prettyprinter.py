from expression import *

class ExprPrinter:
    
    def prettyString(self, e):
        steps = self.addSteps(e, [])[::-1]
        return '\n'.join(steps)


    def pprint(self, e):
        steps =  self.addSteps(e, [])[::-1]

        print("-----Solution-----")
        for step in steps:
            print(step)
        print("------------------")

    def addSteps(self, e, ss):

        if e.isLeaf():
            return ss
        else:
            (op,l,r) = e.myInfo()
            lValue, rValue, myValue = l.eval(), r.eval(), e.eval()

            # must be a valid expression
            if len(lValue+rValue+myValue)!=3:
                raise ValueError("Must provide a coundown-valid expression for pprinting")

            lValue, rValue, myValue = lValue[0], rValue[0], myValue[0]
            step = str(lValue)+" "+str(op)+" "+str(rValue)+" = "+str(myValue)

            withLeft = self.addSteps(l, ss+[step])
            return self.addSteps(r, withLeft)
