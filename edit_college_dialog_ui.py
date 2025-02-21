# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_college_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_editCollegeDialog(object):
    def setupUi(self, editCollegeDialog):
        if not editCollegeDialog.objectName():
            editCollegeDialog.setObjectName(u"editCollegeDialog")
        editCollegeDialog.resize(300, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(editCollegeDialog.sizePolicy().hasHeightForWidth())
        editCollegeDialog.setSizePolicy(sizePolicy)
        editCollegeDialog.setMinimumSize(QSize(300, 150))
        editCollegeDialog.setMaximumSize(QSize(300, 150))
        font = QFont()
        font.setFamilies([u"Verdana"])
        editCollegeDialog.setFont(font)
        editCollegeDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(editCollegeDialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(editCollegeDialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.dialogFrame = QFrame(self.widget)
        self.dialogFrame.setObjectName(u"dialogFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dialogFrame.sizePolicy().hasHeightForWidth())
        self.dialogFrame.setSizePolicy(sizePolicy1)
        self.dialogFrame.setAutoFillBackground(False)
        self.dialogFrame.setFrameShape(QFrame.StyledPanel)
        self.dialogFrame.setFrameShadow(QFrame.Raised)
        self.dialog_lineEdit_5 = QLineEdit(self.dialogFrame)
        self.dialog_lineEdit_5.setObjectName(u"dialog_lineEdit_5")
        self.dialog_lineEdit_5.setGeometry(QRect(110, 50, 161, 31))
        self.dialog_lineEdit_4 = QLineEdit(self.dialogFrame)
        self.dialog_lineEdit_4.setObjectName(u"dialog_lineEdit_4")
        self.dialog_lineEdit_4.setGeometry(QRect(110, 10, 161, 31))
        self.dialoglabel7 = QLabel(self.dialogFrame)
        self.dialoglabel7.setObjectName(u"dialoglabel7")
        self.dialoglabel7.setGeometry(QRect(10, 10, 101, 31))
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(10)
        self.dialoglabel7.setFont(font1)
        self.dialoglabel8 = QLabel(self.dialogFrame)
        self.dialoglabel8.setObjectName(u"dialoglabel8")
        self.dialoglabel8.setGeometry(QRect(10, 50, 101, 31))
        self.dialoglabel8.setFont(font1)
        self.editCollegeButton = QPushButton(self.dialogFrame)
        self.editCollegeButton.setObjectName(u"editCollegeButton")
        self.editCollegeButton.setGeometry(QRect(160, 90, 111, 31))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.editCollegeButton.setFont(font2)

        self.verticalLayout_2.addWidget(self.dialogFrame)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(editCollegeDialog)

        QMetaObject.connectSlotsByName(editCollegeDialog)
    # setupUi

    def retranslateUi(self, editCollegeDialog):
        editCollegeDialog.setWindowTitle(QCoreApplication.translate("editCollegeDialog", u"Edit College", None))
        self.dialoglabel7.setText(QCoreApplication.translate("editCollegeDialog", u"College Code", None))
        self.dialoglabel8.setText(QCoreApplication.translate("editCollegeDialog", u"College Name", None))
        self.editCollegeButton.setText(QCoreApplication.translate("editCollegeDialog", u"Edit College", None))
    # retranslateUi

