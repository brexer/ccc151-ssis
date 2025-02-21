from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QComboBox, QPushButton, QLabel

class EditStudentDialog(QDialog):
    def __init__(self, student_data, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit Student")
        self.student_data = student_data
        self.updated_data = {}

        layout = QVBoxLayout()

        self.id_edit = QLineEdit(self.student_data["ID"])
        self.fname_edit = QLineEdit(self.student_data["First Name"])
        self.lname_edit = QLineEdit(self.student_data["Last Name"])
        self.gender_edit = QComboBox()
        self.gender_edit.addItems(["Male", "Female"])
        self.gender_edit.setCurrentText(self.student_data["Gender"])
        self.yearlevel_edit = QComboBox()
        self.yearlevel_edit.addItems(["1", "2", "3", "4"])
        self.yearlevel_edit.setCurrentText(self.student_data["Year Level"])
        self.program_edit = QLineEdit(self.student_data["Program"])

        layout.addWidget(QLabel("ID"))
        layout.addWidget(self.id_edit)
        layout.addWidget(QLabel("First Name"))
        layout.addWidget(self.fname_edit)
        layout.addWidget(QLabel("Last Name"))
        layout.addWidget(self.lname_edit)
        layout.addWidget(QLabel("Gender"))
        layout.addWidget(self.gender_edit)
        layout.addWidget(QLabel("Year Level"))
        layout.addWidget(self.yearlevel_edit)
        layout.addWidget(QLabel("Program"))
        layout.addWidget(self.program_edit)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_data)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def save_data(self):
        self.updated_data = {
            "ID": self.id_edit.text(),
            "First Name": self.fname_edit.text(),
            "Last Name": self.lname_edit.text(),
            "Gender": self.gender_edit.currentText(),
            "Year Level": self.yearlevel_edit.currentText(),
            "Program": self.program_edit.text().upper()
        }
        self.accept()

    def get_updated_data(self):
        return self.updated_data