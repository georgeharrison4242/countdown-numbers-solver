from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, 
    QLabel, QPushButton, QComboBox, QSlider, QFrame, QDesktopWidget, QGraphicsScene,
    QGraphicsView, QGraphicsRectItem, QMainWindow, QLineEdit, QCheckBox)
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QPoint, QTimer
import sys

class GUI(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Countdown Numbers Game")
        self.initInterface()
        self.show()

    def initInterface(self):

        # layout used by whole program
        grid = QGridLayout()
        self.setLayout(grid)


        """

        # on-screen text elements
        title = QLabel('Welcome to the browser companion!')
        searchText = QLabel('Search term')

        # interactive components
        searchBox = QLineEdit()
        topResultsCB = QCheckBox('Open top google results')
        googleSearchCB = QCheckBox('Search Google')
        fbSearchCB = QCheckBox('Search Facebook')
        amSearchCB = QCheckBox('Search Amazon')
        submitButton = QPushButton('Search',self)

        # add components to window using grid system
        grid.addWidget(title, 0, 0, 1, 2)
        grid.addWidget(searchText, 1, 0, 1, 1)
        grid.addWidget(searchBox, 1, 1, 1, 1)
        grid.addWidget(topResultsCB, 2, 0, 1, 2)
        grid.addWidget(googleSearchCB, 3, 0, 1, 2)
        grid.addWidget(fbSearchCB, 4, 0, 1, 2)
        grid.addWidget(amSearchCB, 5, 0, 1, 2)
        grid.addWidget(submitButton, 6, 0, 1, 2)
        """

app = QApplication(sys.argv)
gui = GUI()
app.exec_()
