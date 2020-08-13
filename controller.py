class Controller:

    def __init__(self, view, model):
        self.view = view
        self.model = model

        self.view.passEvents(self.eventHandler)

    def eventHandler(self, eventType):

        if eventType == "genNumbers":
            numbers = self.model.setRandomNumbers()
            #self.view.showNumbers(numbers)
            return ViewChange("showNumbers", numbers)

        elif eventType == "genTarget":
            target = self.model.pickTarget()
            #self.view.showTarget(target)
            return ViewChange("showTarget", target)

        elif eventType == "check":
            correct = self.model.check()
            #self.view.displayError("Feature not implemented yet")
            return ViewChange("checkSolution", correct)

        elif eventType == "solve":
            solutionText = self.model.solve()
            #self.view.displaySolution(solutionText)
            return ViewChange("displaySolution", solutionText)

        else:
            raise ValueError("buttons must call handler with one argument (str) from: genNumbers, genTarget, check, solve")


class ViewChange:
    def __init__(self, typeOfChange, data):
        self.type = typeOfChange
        self.data = data

