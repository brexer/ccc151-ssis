from main_screen import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
import resources
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Student Information System")


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        with open("navbar.qss", "r") as style_file:
            style_str = style_file.read()
        app.setStyleSheet(style_str)

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)

        self.ui.studentButton1.clicked.connect(lambda: self.change_page(1))
        self.ui.studentButton2.clicked.connect(lambda: self.change_page(1))
        self.ui.programButton1.clicked.connect(lambda: self.change_page(2))
        self.ui.programButton2.clicked.connect(lambda: self.change_page(2))
        self.ui.collegeButton1.clicked.connect(lambda: self.change_page(3))
        self.ui.collegeButton2.clicked.connect(lambda: self.change_page(3))



    def change_page(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
