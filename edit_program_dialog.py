# Form implementation generated from reading ui file '.\edit_program_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from pathlib import Path
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_editProgramDialog(object):
    def setupUi(self, editProgramDialog):
        editProgramDialog.setObjectName("editProgramDialog")
        editProgramDialog.resize(300, 190)
        editProgramDialog.setStyleSheet(Path('dialogstyle.qss').read_text())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(editProgramDialog.sizePolicy().hasHeightForWidth())
        editProgramDialog.setSizePolicy(sizePolicy)
        editProgramDialog.setMinimumSize(QtCore.QSize(300, 190))
        editProgramDialog.setMaximumSize(QtCore.QSize(300, 190))
        editProgramDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(editProgramDialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(parent=editProgramDialog)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_11 = QtWidgets.QFrame(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.frame_11.setFont(font)
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_11.setObjectName("frame_11")
        self.dialog_comboBox_4 = QtWidgets.QComboBox(parent=self.frame_11)
        self.dialog_comboBox_4.setGeometry(QtCore.QRect(110, 90, 91, 31))
        self.dialog_comboBox_4.setObjectName("dialog_comboBox_4")
        self.dialog_lineEdit_7 = QtWidgets.QLineEdit(parent=self.frame_11)
        self.dialog_lineEdit_7.setGeometry(QtCore.QRect(110, 50, 161, 31))
        self.dialog_lineEdit_7.setObjectName("dialog_lineEdit_7")
        self.dialog_lineEdit_6 = QtWidgets.QLineEdit(parent=self.frame_11)
        self.dialog_lineEdit_6.setGeometry(QtCore.QRect(110, 10, 161, 31))
        self.dialog_lineEdit_6.setObjectName("dialog_lineEdit_6")
        self.label_27 = QtWidgets.QLabel(parent=self.frame_11)
        self.label_27.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(parent=self.frame_11)
        self.label_28.setGeometry(QtCore.QRect(10, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_35 = QtWidgets.QLabel(parent=self.frame_11)
        self.label_35.setGeometry(QtCore.QRect(10, 90, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.editProgramButton = QtWidgets.QPushButton(parent=self.frame_11)
        self.editProgramButton.setGeometry(QtCore.QRect(160, 130, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        self.editProgramButton.setFont(font)
        self.editProgramButton.setObjectName("editProgramButton")
        self.verticalLayout_2.addWidget(self.frame_11)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(editProgramDialog)
        QtCore.QMetaObject.connectSlotsByName(editProgramDialog)

    def retranslateUi(self, editProgramDialog):
        _translate = QtCore.QCoreApplication.translate
        editProgramDialog.setWindowTitle(_translate("editProgramDialog", "Edit Program"))
        self.label_27.setText(_translate("editProgramDialog", "Program Code"))
        self.label_28.setText(_translate("editProgramDialog", "Program Name"))
        self.label_35.setText(_translate("editProgramDialog", "College Code"))
        self.editProgramButton.setText(_translate("editProgramDialog", "Edit Program"))
