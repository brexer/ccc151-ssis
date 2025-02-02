from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QWidget
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('CCC151-SSIS')
        # self.setWindowIcon(QIcon("bla.png"))

        # Set main widget and layout
        centerWidget = QWidget()
        mainLayout = QGridLayout()

        # Title label
        mainTitle = QLabel("CCC151 Student Information System")
        mainTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        mainLayout.addWidget(mainTitle, 0, 0)
        
        # font
        font = QFont("Arial", 20)
        font.setBold = True
        mainTitle.setFont(font)

        
        centerWidget.setLayout(mainLayout)
        self.setCentralWidget(centerWidget)

        self.resize(1280, 720)  # to avoid chaos when minimized
        self.showMaximized() 

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

main()
