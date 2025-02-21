# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_student_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_editStudentDialog(object):
    def setupUi(self, editStudentDialog):
        if not editStudentDialog.objectName():
            editStudentDialog.setObjectName(u"editStudentDialog")
        editStudentDialog.resize(300, 310)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(editStudentDialog.sizePolicy().hasHeightForWidth())
        editStudentDialog.setSizePolicy(sizePolicy)
        editStudentDialog.setMinimumSize(QSize(300, 310))
        editStudentDialog.setMaximumSize(QSize(300, 310))
        font = QFont()
        font.setFamilies([u"Verdana"])
        editStudentDialog.setFont(font)
        editStudentDialog.setModal(True)
        self.horizontalLayout = QHBoxLayout(editStudentDialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(editStudentDialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dialogFrame = QFrame(self.widget)
        self.dialogFrame.setObjectName(u"dialogFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dialogFrame.sizePolicy().hasHeightForWidth())
        self.dialogFrame.setSizePolicy(sizePolicy1)
        self.dialogFrame.setFrameShape(QFrame.StyledPanel)
        self.dialogFrame.setFrameShadow(QFrame.Raised)
        self.dialogFrame.setLineWidth(1)
        self.dialog_comboBox_3 = QComboBox(self.dialogFrame)
        self.dialog_comboBox_3.addItem("")
        self.dialog_comboBox_3.addItem("")
        self.dialog_comboBox_3.setObjectName(u"dialog_comboBox_3")
        self.dialog_comboBox_3.setGeometry(QRect(110, 210, 91, 31))
        self.dialog_comboBox_2 = QComboBox(self.dialogFrame)
        self.dialog_comboBox_2.addItem("")
        self.dialog_comboBox_2.addItem("")
        self.dialog_comboBox_2.addItem("")
        self.dialog_comboBox_2.addItem("")
        self.dialog_comboBox_2.setObjectName(u"dialog_comboBox_2")
        self.dialog_comboBox_2.setGeometry(QRect(110, 170, 91, 31))
        self.dialog_comboBox_1 = QComboBox(self.dialogFrame)
        self.dialog_comboBox_1.addItem("")
        self.dialog_comboBox_1.addItem("")
        self.dialog_comboBox_1.setObjectName(u"dialog_comboBox_1")
        self.dialog_comboBox_1.setGeometry(QRect(110, 130, 91, 31))
        self.dialog_lineEdit_3 = QLineEdit(self.dialogFrame)
        self.dialog_lineEdit_3.setObjectName(u"dialog_lineEdit_3")
        self.dialog_lineEdit_3.setGeometry(QRect(110, 90, 161, 31))
        self.dialog_lineEdit_2 = QLineEdit(self.dialogFrame)
        self.dialog_lineEdit_2.setObjectName(u"dialog_lineEdit_2")
        self.dialog_lineEdit_2.setGeometry(QRect(110, 50, 161, 31))
        self.dialog_lineEdit_1 = QLineEdit(self.dialogFrame)
        self.dialog_lineEdit_1.setObjectName(u"dialog_lineEdit_1")
        self.dialog_lineEdit_1.setGeometry(QRect(110, 10, 161, 31))
        self.dialoglabel1 = QLabel(self.dialogFrame)
        self.dialoglabel1.setObjectName(u"dialoglabel1")
        self.dialoglabel1.setGeometry(QRect(10, 10, 71, 31))
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(10)
        self.dialoglabel1.setFont(font1)
        self.dialoglabel2 = QLabel(self.dialogFrame)
        self.dialoglabel2.setObjectName(u"dialoglabel2")
        self.dialoglabel2.setGeometry(QRect(10, 50, 71, 31))
        self.dialoglabel2.setFont(font1)
        self.dialoglabel3 = QLabel(self.dialogFrame)
        self.dialoglabel3.setObjectName(u"dialoglabel3")
        self.dialoglabel3.setGeometry(QRect(10, 90, 71, 31))
        self.dialoglabel3.setFont(font1)
        self.dialoglabel4 = QLabel(self.dialogFrame)
        self.dialoglabel4.setObjectName(u"dialoglabel4")
        self.dialoglabel4.setGeometry(QRect(10, 130, 71, 31))
        self.dialoglabel4.setFont(font1)
        self.dialoglabel5 = QLabel(self.dialogFrame)
        self.dialoglabel5.setObjectName(u"dialoglabel5")
        self.dialoglabel5.setGeometry(QRect(10, 170, 71, 31))
        self.dialoglabel5.setFont(font1)
        self.dialoglabel6 = QLabel(self.dialogFrame)
        self.dialoglabel6.setObjectName(u"dialoglabel6")
        self.dialoglabel6.setGeometry(QRect(10, 210, 71, 31))
        self.dialoglabel6.setFont(font1)
        self.editStudentButton = QPushButton(self.dialogFrame)
        self.editStudentButton.setObjectName(u"editStudentButton")
        self.editStudentButton.setGeometry(QRect(160, 250, 111, 31))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.editStudentButton.setFont(font2)

        self.verticalLayout.addWidget(self.dialogFrame)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(editStudentDialog)

        QMetaObject.connectSlotsByName(editStudentDialog)
    # setupUi

    def retranslateUi(self, editStudentDialog):
        editStudentDialog.setWindowTitle(QCoreApplication.translate("editStudentDialog", u"Edit Student", None))
        self.dialog_comboBox_3.setItemText(0, QCoreApplication.translate("editStudentDialog", u"BSCS", None))
        self.dialog_comboBox_3.setItemText(1, QCoreApplication.translate("editStudentDialog", u"BSIT", None))

        self.dialog_comboBox_2.setItemText(0, QCoreApplication.translate("editStudentDialog", u"First Year", None))
        self.dialog_comboBox_2.setItemText(1, QCoreApplication.translate("editStudentDialog", u"Second Year", None))
        self.dialog_comboBox_2.setItemText(2, QCoreApplication.translate("editStudentDialog", u"Third Year", None))
        self.dialog_comboBox_2.setItemText(3, QCoreApplication.translate("editStudentDialog", u"Fourth Year", None))

        self.dialog_comboBox_1.setItemText(0, QCoreApplication.translate("editStudentDialog", u"Male", None))
        self.dialog_comboBox_1.setItemText(1, QCoreApplication.translate("editStudentDialog", u"Female", None))

        self.dialoglabel1.setText(QCoreApplication.translate("editStudentDialog", u"ID #", None))
        self.dialoglabel2.setText(QCoreApplication.translate("editStudentDialog", u"First Name", None))
        self.dialoglabel3.setText(QCoreApplication.translate("editStudentDialog", u"Last Name", None))
        self.dialoglabel4.setText(QCoreApplication.translate("editStudentDialog", u"Gender", None))
        self.dialoglabel5.setText(QCoreApplication.translate("editStudentDialog", u"Year Level", None))
        self.dialoglabel6.setText(QCoreApplication.translate("editStudentDialog", u"Program", None))
        self.editStudentButton.setText(QCoreApplication.translate("editStudentDialog", u"Edit Student", None))
    # retranslateUi

