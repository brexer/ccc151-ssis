# Form implementation generated from reading ui file '.\edit_college_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from pathlib import Path
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_editCollegeDialog(object):
    def setupUi(self, editCollegeDialog):
        editCollegeDialog.setObjectName("editCollegeDialog")
        editCollegeDialog.resize(300, 150)
        editCollegeDialog.setStyleSheet(Path('dialogstyle.qss').read_text())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(editCollegeDialog.sizePolicy().hasHeightForWidth())
        editCollegeDialog.setSizePolicy(sizePolicy)
        editCollegeDialog.setMinimumSize(QtCore.QSize(300, 150))
        editCollegeDialog.setMaximumSize(QtCore.QSize(300, 150))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        editCollegeDialog.setFont(font)
        editCollegeDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(editCollegeDialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(parent=editCollegeDialog)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dialogFrame = QtWidgets.QFrame(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dialogFrame.sizePolicy().hasHeightForWidth())
        self.dialogFrame.setSizePolicy(sizePolicy)
        self.dialogFrame.setAutoFillBackground(False)
        self.dialogFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.dialogFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.dialogFrame.setObjectName("dialogFrame")
        self.dialog_lineEdit_5 = QtWidgets.QLineEdit(parent=self.dialogFrame)
        self.dialog_lineEdit_5.setGeometry(QtCore.QRect(110, 50, 161, 31))
        self.dialog_lineEdit_5.setObjectName("dialog_lineEdit_5")
        self.dialog_lineEdit_4 = QtWidgets.QLineEdit(parent=self.dialogFrame)
        self.dialog_lineEdit_4.setGeometry(QtCore.QRect(110, 10, 161, 31))
        self.dialog_lineEdit_4.setObjectName("dialog_lineEdit_4")
        self.dialoglabel7 = QtWidgets.QLabel(parent=self.dialogFrame)
        self.dialoglabel7.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.dialoglabel7.setFont(font)
        self.dialoglabel7.setObjectName("dialoglabel7")
        self.dialoglabel8 = QtWidgets.QLabel(parent=self.dialogFrame)
        self.dialoglabel8.setGeometry(QtCore.QRect(10, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.dialoglabel8.setFont(font)
        self.dialoglabel8.setObjectName("dialoglabel8")
        self.editCollegeButton = QtWidgets.QPushButton(parent=self.dialogFrame)
        self.editCollegeButton.setGeometry(QtCore.QRect(160, 90, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        self.editCollegeButton.setFont(font)
        self.editCollegeButton.setObjectName("editCollegeButton")
        self.verticalLayout_2.addWidget(self.dialogFrame)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(editCollegeDialog)
        QtCore.QMetaObject.connectSlotsByName(editCollegeDialog)

    def retranslateUi(self, editCollegeDialog):
        _translate = QtCore.QCoreApplication.translate
        editCollegeDialog.setWindowTitle(_translate("editCollegeDialog", "Edit College"))
        self.dialoglabel7.setText(_translate("editCollegeDialog", "College Code"))
        self.dialoglabel8.setText(_translate("editCollegeDialog", "College Name"))
        self.editCollegeButton.setText(_translate("editCollegeDialog", "Edit College"))
