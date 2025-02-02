from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QWidget, QLineEdit, QComboBox, QSpinBox
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('CCC151-SSIS')
        # self.setWindowIcon(QIcon("bla.png"))

        # main widget and layout
        centerWidget = QWidget()
        mainLayout = QGridLayout()


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

        #self.lineEdit = QLineEdit() <--- to get user info

        """ 
        self.spinBox = QSpinBox() <--- for int

        self.comboBox = QComboBox()
        self.comboBox.addItem("CCS")
        self.comboBox.addItem("COE")
        self.comboBox.addItem("CSM")
        self.comboBox.addItem("CHS")
        self.comboBox.addItem("CED")
        self.comboBox.addItem("CASS")

        mainLayout.addWidget(self.comboBox) <--- para ma add sa window
        """

    #def clickHandler(self): <--- some actions when button is clicked (can be used to get info from user)
        #print("Button clicked.")
        #print(self.lineEdit.text())
        #print(self.comboBox.currentText()) <--- to obtain info on what the user picked from the drop-down
        #can be optimized by adding currentText 


    #def showPassword(self):
        #toggle show password when box is ticked

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

main()
