from main_screen import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from pathlib import Path
import resources
import sys
import os

studentdb = "student.csv"
collegedb = "college.csv"
programdb = "program.csv"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Student Information System")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setStylesheetfile()

        self.ui.icon_only_widget.hide()
        self.ui.widget_10.hide()
        self.ui.widget_11.hide()
        self.ui.widget_12.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.homeButton1.setChecked(True)
        self.ui.homeButton2.setChecked(True)

        self.ui.homeButton1.clicked.connect(lambda: self.changePage(0))
        self.ui.homeButton2.clicked.connect(lambda: self.changePage(0))
        self.ui.studentButton1.clicked.connect(lambda: self.changePage(1))
        self.ui.studentButton2.clicked.connect(lambda: self.changePage(1))
        self.ui.programButton1.clicked.connect(lambda: self.changePage(2))
        self.ui.programButton2.clicked.connect(lambda: self.changePage(2))
        self.ui.collegeButton1.clicked.connect(lambda: self.changePage(3))
        self.ui.collegeButton2.clicked.connect(lambda: self.changePage(3))


    def changePage(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)

    def setStylesheetfile(self):
        stylesheet_path = Path(__file__).parent / "navbar.qss"
        if stylesheet_path.exists():
            with open(stylesheet_path, "r") as file:
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)


if __name__ == '__main__':
    mainPage = QApplication(sys.argv)

    with open ("navbar.qss", "r") as style_file:
        style_str = style_file.read()
    mainPage.setStyleSheet

    window = MainWindow()
    window.show()

    sys.exit(mainPage.exec())
