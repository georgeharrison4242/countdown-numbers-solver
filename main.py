from model import Model
from prettyprinter import ExprPrinter
from view import SimplePyQtView
from controller import Controller
from PyQt5.QtWidgets import *
import sys

if __name__=="__main__":   
    app = QApplication(sys.argv)
    view = SimplePyQtView()
    model = Model()
    controller = Controller(view,model)
    app.exec_()
    