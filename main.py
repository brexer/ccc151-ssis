from main_screen import Ui_MainWindow
from edit_student_dialog import Ui_editStudentDialog
from edit_program_dialog import Ui_editProgramDialog
from edit_college_dialog import Ui_editCollegeDialog
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QTableWidget, QHeaderView, QTableWidgetItem, QMessageBox, QDialog
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

        self.ui.pushButton_43.clicked.connect(self.editStudent)
        self.ui.pushButton_46.clicked.connect(self.editProgram)
        self.ui.pushButton_49.clicked.connect(self.editCollege)



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

    def editStudent(self):
        selectedRow = self.ui.studentTable.currentRow()

        if selectedRow == -1:
            QMessageBox.warning(self, "No student selected", "Please select a student to edit.")
            return
        
        student_id = self.ui.studentTable.item(selectedRow, 0).text()
        student_Fname = self.ui.studentTable.item(selectedRow, 1).text()
        student_Lname = self.ui.studentTable.item(selectedRow, 2).text()
        student_gender = self.ui.studentTable.item(selectedRow, 3).text()
        student_yearlevel = self.ui.studentTable.item(selectedRow, 4).text()
        student_program = self.ui.studentTable.item(selectedRow, 5).text()

        self.editStudentDialog = QDialog()
        self.editStudentDialog_ui = Ui_editStudentDialog()
        self.editStudentDialog_ui.setupUi(self.editStudentDialog)

        self.editStudentDialog_ui.dialog_lineEdit_1.setText(student_id)
        self.editStudentDialog_ui.dialog_lineEdit_2.setText(student_Fname)
        self.editStudentDialog_ui.dialog_lineEdit_3.setText(student_Lname)
        self.editStudentDialog_ui.dialog_comboBox_1.setCurrentText(student_gender)
        self.editStudentDialog_ui.dialog_comboBox_2.setCurrentText(student_yearlevel)
        self.editStudentDialog_ui.dialog_comboBox_3.setCurrentText(student_program)

        self.editStudentDialog_ui.editStudentButton.clicked.connect(lambda: self.updateCurrentStudent(selectedRow))

        self.editStudentDialog.exec()
        QMessageBox.information(self, "Student Updated", "Student has been updated successfully.")

    def updateCurrentStudent(self, selectedRow):
        student_id = self.editStudentDialog_ui.dialog_lineEdit_1.text().strip()
        student_Fname = self.editStudentDialog_ui.dialog_lineEdit_2.text().strip().title()
        student_Lname = self.editStudentDialog_ui.dialog_lineEdit_3.text().strip().title()
        student_gender = self.editStudentDialog_ui.dialog_comboBox_1.currentText()
        student_yearlevel = self.editStudentDialog_ui.dialog_comboBox_2.currentText()
        student_program = self.editStudentDialog_ui.dialog_comboBox_3.currentText().upper()

        self.ui.studentTable.setItem(selectedRow, 0, QTableWidgetItem(student_id))
        self.ui.studentTable.setItem(selectedRow, 1, QTableWidgetItem(student_Fname))
        self.ui.studentTable.setItem(selectedRow, 2, QTableWidgetItem(student_Lname))
        self.ui.studentTable.setItem(selectedRow, 3, QTableWidgetItem(student_gender))
        self.ui.studentTable.setItem(selectedRow, 4, QTableWidgetItem(student_yearlevel))
        self.ui.studentTable.setItem(selectedRow, 5, QTableWidgetItem(student_program))

        self.students[selectedRow] = [student_id, student_Fname, student_Lname, student_gender, student_yearlevel, student_program]
        self.saveStudentData()

        self.editStudentDialog.close()

# end of STUDENT PAGE

# start of PROGRAM PAGE

    def addProgram(self):
        program_code = self.ui.program_code.text().strip().upper()
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

            self.ui.comboBox_16.addItem(program_code)
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

    def editProgram(self):
        selectedRow = self.ui.programTable.currentRow()

        if selectedRow == -1:
            QMessageBox.warning(self, "No program selected", "Please select a program to edit.")
            return
        
        program_code = self.ui.programTable.item(selectedRow, 0).text()
        program_name = self.ui.programTable.item(selectedRow, 1).text()
        program_college = self.ui.programTable.item(selectedRow, 2).text()

        self.editProgramDialog = QDialog()
        self.editProgramDialog_ui = Ui_editProgramDialog()
        self.editProgramDialog_ui.setupUi(self.editProgramDialog)

        self.editProgramDialog_ui.dialog_lineEdit_1.setText(program_code)
        self.editProgramDialog_ui.dialog_lineEdit_2.setText(program_name)
        self.editProgramDialog_ui.dialog_comboBox_1.setCurrentText(program_college)

        self.editProgramDialog_ui.editProgramButton.clicked.connect(lambda: self.updateCurrentProgram(selectedRow))

        self.editProgramDialog.exec()
        QMessageBox.information(self, "Program Updated", "Program has been updated successfully.")

    def updateCurrentProgram(self, selectedRow):
        program_code = self.editProgramDialog_ui.dialog_lineEdit_6.text().strip()
        program_name = self.editProgramDialog_ui.dialog_lineEdit_7.text().strip().title()
        program_college = self.editProgramDialog_ui.dialog_comboBox_4.currentText().upper()

        self.ui.programTable.setItem(selectedRow, 0, QTableWidgetItem(program_code))
        self.ui.programTable.setItem(selectedRow, 1, QTableWidgetItem(program_name))
        self.ui.programTable.setItem(selectedRow, 2, QTableWidgetItem(program_college))

        self.programs[selectedRow] = [program_code, program_name, program_college]
        self.saveProgramData()

        self.editProgramDialog.close()


# end of PROGRAM PAGE

# start of COLLEGE PAGE

    def addCollege(self):
        college_code = self.ui.college_code.text().strip().upper()
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
            
            self.ui.comboBox_26.addItem(college_code)
            
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

    def editCollege(self):
        selectedRow = self.ui.collegeTable.currentRow()

        if selectedRow == -1:
            QMessageBox.warning(self, "No college selected", "Please select a college to edit.")
            return
        
        college_code = self.ui.collegeTable.item(selectedRow, 0).text().upper()
        college_name = self.ui.collegeTable.item(selectedRow, 1).text()

        self.editCollegeDialog = QDialog()
        self.editCollegeDialog_ui = Ui_editCollegeDialog()
        self.editCollegeDialog_ui.setupUi(self.editCollegeDialog)

        self.editCollegeDialog_ui.dialog_lineEdit_4.setText(college_code)
        self.editCollegeDialog_ui.dialog_lineEdit_5.setText(college_name)

        self.editCollegeDialog_ui.editCollegeButton.clicked.connect(lambda: self.updateCurrentCollege(selectedRow))

        self.editCollegeDialog.exec()
        QMessageBox.information(self, "College Updated", "College has been updated successfully.")

    def updateCurrentCollege(self, selectedRow):
        college_code = self.editCollegeDialog_ui.dialog_lineEdit_4.text().strip().upper()
        college_name = self.editCollegeDialog_ui.dialog_lineEdit_5.text().strip().title()

        self.ui.collegeTable.setItem(selectedRow, 0, QTableWidgetItem(college_code))
        self.ui.collegeTable.setItem(selectedRow, 1, QTableWidgetItem(college_name))

        self.colleges[selectedRow] = [college_code, college_name]
        self.saveCollegeData()

        self.editCollegeDialog.close()

# end of COLLEGE PAGE



    def clearForm(self):
        pass

    def deleteStudent(self):
        pass
        #selectedRow = self.ui.studentTable.currentRow()
        
        #if selectedRow != 1:
            

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
