from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from functools import partial
import time

class SimplePyQtView(QWidget):

    def __init__(self):
        super().__init__()

        # ui widgets
        self.title = QLabel("Countdown numbers game")
        self.generateNumbersButton = QPushButton("Random numbers")
        self.numberLabels = [QLabel("Number "+str(i+1)) for i in range(6)]
        self.numberEntries = [QLineEdit() for i in range(6)]
        self.generateTargetButton = QPushButton("Generate Target")
        self.target = QLabel('Target: ')
        self.userSolutionPrompt = QLabel("Type solution here:")
        self.userSolutionBox = QPlainTextEdit()
        self.correctSolutionPrompt = QLabel("A correct answer:")
        self.correctSolutionBox = QPlainTextEdit()
        self.checkUserSolutionButton = QPushButton("Check")
        self.displaySolutionButton = QPushButton("Solve")

        # connect buttons to handler function
        self.handlerFunction = None
        self.buttons = [ self.generateNumbersButton,
                         self.generateTargetButton,
                         self.checkUserSolutionButton,
                         self.displaySolutionButton ]

        self.generateNumbersButton.pressed.connect(partial(self.buttonClicked, "genNumbers"))
        self.generateTargetButton.pressed.connect(partial(self.buttonClicked, "genTarget"))
        self.checkUserSolutionButton.pressed.connect(partial(self.buttonClicked, "check"))
        self.displaySolutionButton.pressed.connect(partial(self.buttonClicked, "solve"))


        # grid system
        self.grid = QGridLayout()

        self.grid.addWidget(self.title, 0, 0, 1, 2)

        self.grid.addWidget(self.generateTargetButton, 1, 0, 1, 1)
        self.grid.addWidget(self.target, 1, 1, 1, 1)

        for i,(label,entry) in enumerate(list(zip(self.numberLabels,self.numberEntries))):
            self.grid.addWidget(label, 2+i, 0, 1, 1)
            self.grid.addWidget(entry, 2+i, 1, 1, 1)

        self.grid.addWidget(self.generateNumbersButton, 8,0,1,2)
        
        self.grid.addWidget(self.userSolutionPrompt, 1, 2, 1, 1)
        self.grid.addWidget(self.userSolutionBox, 2, 2, 6, 1)
        self.grid.addWidget(self.correctSolutionPrompt, 1, 3, 1, 1)
        self.grid.addWidget(self.correctSolutionBox, 2, 3, 6, 1)
        self.grid.addWidget(self.checkUserSolutionButton, 8, 2, 1, 1)
        self.grid.addWidget(self.displaySolutionButton, 8, 3, 1, 1)

        # housekeeping
        self.setWindowTitle("Countdown Numbers Round")
        self.setLayout(self.grid)
        self.show()

        self.threadpool = QThreadPool()


    def buttonClicked(self, buttonType):
        try:
            worker = WorkerThread(self.handlerFunction, buttonType)
            worker.signals.result.connect(self.updateView)

            self.threadpool.start(worker)
            #self.handlerFunction(buttonType)
        except:
            raise NotImplementedError("must specify a handler function with passEvents function")

    def passEvents(self, controllerFunction):
        self.handlerFunction = controllerFunction


    def showNumbers(self, numbers):
        assert(len(numbers)==6)

        for i,n in enumerate(numbers):
            self.numberEntries[i].setText(str(n))

    def showTarget(self, target):
        self.target.setText("Target: " + str(target))

    def displayError(self, error):
        self.correctSolutionBox.clear()
        self.correctSolutionBox.insertPlainText(error)

    def showCorrect(self, correct):
        correctStr = "Correct" if correct else "Incorrect"

        currentText = self.userSolutionBox.toPlainText()
        if currentText == '':
            self.userSolutionBox.insertPlainText(correctStr)
        else:
            self.userSolutionBox.insertPlainText("\n"+correctStr)

    def displaySolution(self, solution):
        self.correctSolutionBox.clear()
        self.correctSolutionBox.insertPlainText(solution)

    def updateView(self, changeObject):
        changeType = changeObject.type
        data = changeObject.data
        if changeType == 'showNumbers':
            self.showNumbers(data)
        elif changeType == 'showTarget':
            self.showTarget(data)
        elif changeType == 'checkSolution':
            self.showCorrect(data)
        elif changeType == 'displaySolution':
            self.displaySolution(data)
        else:
            print(changeType)
            raise ValueError("view can handle one change type of: showNumbers, genTarget, checkSolution, displaySolution")


class WorkerThread(QRunnable):

    def __init__(self, handler, arg):
        super(WorkerThread, self).__init__()
        self.handler = handler
        self.arg = arg
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        changeObject = self.handler(self.arg)
        self.signals.result.emit(changeObject)
        self.signals.finished.emit()

class WorkerSignals(QObject):
    result = pyqtSignal(object)
    finished = pyqtSignal()