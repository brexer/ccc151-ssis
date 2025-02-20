from main_screen import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QTableWidget, QHeaderView, QTableWidgetItem, QMessageBox
from PyQt6.QtGui import QIntValidator
from pathlib import Path
import resources
import sys
import os
import csv

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

        self.students = []
        self.colleges = []
        self.programs = []

        # changing pages
        self.ui.homeButton1.clicked.connect(lambda: self.changePage(0))
        self.ui.homeButton2.clicked.connect(lambda: self.changePage(0))
        self.ui.studentButton1.clicked.connect(lambda: self.changePage(1))
        self.ui.studentButton2.clicked.connect(lambda: self.changePage(1))
        self.ui.programButton1.clicked.connect(lambda: self.changePage(2))
        self.ui.programButton2.clicked.connect(lambda: self.changePage(2))
        self.ui.collegeButton1.clicked.connect(lambda: self.changePage(3))
        self.ui.collegeButton2.clicked.connect(lambda: self.changePage(3))

        # initializing student data
        self.ui.student_id = self.ui.lineEdit_12
        self.ui.student_id.setValidator(QIntValidator()) # only accepts integer
        self.ui.student_Fname = self.ui.lineEdit_11
        self.ui.student_Lname = self.ui.lineEdit_10
        self.ui.student_gender = self.ui.comboBox_18
        self.ui.student_yearlevel = self.ui.comboBox_17
        self.ui.student_program = self.ui.comboBox_16

        # initializing program data
        self.ui.program_code = self.ui.lineEdit_21
        self.ui.program_name = self.ui.lineEdit_18
        self.ui.program_college = self.ui.comboBox_26

        # initializing college data
        self.ui.college_code = self.ui.lineEdit_16
        self.ui.college_name = self.ui.lineEdit_15

        # connecting add buttons to functions
        self.ui.addStudentButton.clicked.connect(self.addStudent)
        self.ui.addProgramButton.clicked.connect(self.addProgram)
        self.ui.addCollegeButton.clicked.connect(self.addCollege)



    def changePage(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)

# start of STUDENT PAGE

    def addStudent(self):
        student_id = self.ui.student_id.text().strip()
        student_Fname = self.ui.student_Fname.text().strip().title()
        student_Lname = self.ui.student_Lname.text().strip().title()
        student_gender = self.ui.student_gender.currentText()
        student_yearlevel = self.ui.student_yearlevel.currentText()
        student_program = self.ui.student_program.currentText().upper()

        # check if all fields are filled out
        if not student_id or not student_Fname or not student_Lname or not student_gender or not student_yearlevel or not student_program:
            QMessageBox.warning(self, "All fields are required.", "Please fill out all fields.")
            return
        else:
            new_student = [student_id, student_Fname, student_Lname, student_gender, student_yearlevel, student_program]
            self.students.append(new_student)
            self.saveStudentData()
            self.updateStudentTable()
            QMessageBox.information(self, "Student Added", "Student has been added successfully.")

    def saveStudentData(self):
        with open(studentdb, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["ID", "First Name", "Last Name", "Gender", "Year Level", "Program"])
            writer.writerows(self.students)

    def loadStudentData(self):
        with open(studentdb, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            next(reader)
            self.students = [[row["ID"], row["First Name"], row["Last Name"], row["Gender"], row["Year Level"], row["Program"]] for row in reader]
            
            return self.students
            self.updateStudentTable()   
        
    def updateStudentTable(self):
        self.ui.studentTable.setRowCount(len(self.students))
        self.ui.studentTable.setColumnCount(6)
        for row, student in enumerate(self.students):
            for col, data in enumerate(student):
                self.ui.studentTable.setItem(row, col, QTableWidgetItem(data))

# end of STUDENT PAGE

# start of PROGRAM PAGE

    def addProgram(self):
        program_code = self.ui.program_code.text().strip()
        program_name = self.ui.program_name.text().strip().title()
        program_college = self.ui.program_college.currentText().upper()

        # check if all fields are filled out
        if not program_code or not program_name or not program_college:
            QMessageBox.warning(self, "All fields are required.", "Please fill out all fields.")
            return
        else:
            new_program = [program_code, program_name, program_college]
            self.programs.append(new_program)
            self.saveProgramData()
            self.updateProgramTable()
            QMessageBox.information(self, "Program Added", "Program has been added successfully.")

    def saveProgramData(self):
        with open(programdb, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Code", "Name", "College"])
            writer.writerows(self.programs)

    def loadProgramData(self):
        with open(programdb, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            next(reader)
            self.programs = [[row["Code"], row["Name"], row["College"]] for row in reader]

            return self.programs
            self.updateProgramTable()

    def updateProgramTable(self):
        self.ui.programTable.setRowCount(len(self.programs))
        self.ui.programTable.setColumnCount(3)
        for row, program in enumerate(self.programs):
            for col, data in enumerate(program):
                self.ui.programTable.setItem(row, col, QTableWidgetItem(data))

# end of PROGRAM PAGE

# start of COLLEGE PAGE

    def addCollege(self):
        college_code = self.ui.college_code.text().strip()
        college_name = self.ui.college_name.text().strip().title()

        # check if all fields are filled out
        if not college_code or not college_name:
            QMessageBox.warning(self, "All fields are required.", "Please fill out all fields.")
            return
        else:
            new_college = [college_code, college_name]
            self.colleges.append(new_college)
            self.saveCollegeData()
            self.updateCollegeTable()
            QMessageBox.information(self, "College Added", "College has been added successfully.")

    def saveCollegeData(self):
        with open(collegedb, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Code", "Name"])
            writer.writerows(self.colleges)

    def loadCollegeData(self):
        with open(collegedb, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            next(reader)
            self.colleges = [[row["Code"], row["Name"]] for row in reader]

            return self.colleges
            self.updateCollegeTable()

    def updateCollegeTable(self):
        self.ui.collegeTable.setRowCount(len(self.colleges))
        self.ui.collegeTable.setColumnCount(2)
        for row, college in enumerate(self.colleges):
            for col, data in enumerate(college):
                self.ui.collegeTable.setItem(row, col, QTableWidgetItem(data))

# end of COLLEGE PAGE

    def setStylesheetfile(self):
        stylesheet_path = Path(__file__).parent / "navbar.qss"
        if stylesheet_path.exists():
            with open(stylesheet_path, "r") as file:
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)


if __name__ == '__main__':
    mainPage = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(mainPage.exec())
