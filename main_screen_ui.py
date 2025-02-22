# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1155, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1155, 600))
        MainWindow.setMaximumSize(QSize(1155, 600))
        MainWindow.setStyleSheet(u"\n"
"#widget, #icon_only_widget, #full_menu_widget {\n"
"    background-color: #272727;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background: transparent;\n"
"    border: none;\n"
"	color: #E7ECEF;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #E7ECEF;\n"
"}\n"
"\n"
"#frame_11, #frame_13, #frame_8, #frame_10, #frame_9, #frame_7 {\n"
"	background-color: #272727;\n"
"}\n"
"")
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_15 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.homeButton1 = QPushButton(self.icon_only_widget)
        self.homeButton1.setObjectName(u"homeButton1")
        self.homeButton1.setMinimumSize(QSize(50, 50))
        self.homeButton1.setMaximumSize(QSize(50, 50))
        icon = QIcon()
        icon.addFile(u":/imgs/imgs/home_fixed.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homeButton1.setIcon(icon)
        self.homeButton1.setIconSize(QSize(40, 40))
        self.homeButton1.setCheckable(True)
        self.homeButton1.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.homeButton1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.studentButton1 = QPushButton(self.icon_only_widget)
        self.studentButton1.setObjectName(u"studentButton1")
        icon1 = QIcon()
        icon1.addFile(u":/imgs/imgs/student_transparent.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.studentButton1.setIcon(icon1)
        self.studentButton1.setIconSize(QSize(30, 30))
        self.studentButton1.setCheckable(True)
        self.studentButton1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.studentButton1)

        self.programButton1 = QPushButton(self.icon_only_widget)
        self.programButton1.setObjectName(u"programButton1")
        icon2 = QIcon()
        icon2.addFile(u":/imgs/imgs/program_fixed.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.programButton1.setIcon(icon2)
        self.programButton1.setIconSize(QSize(30, 30))
        self.programButton1.setCheckable(True)
        self.programButton1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.programButton1)

        self.collegeButton1 = QPushButton(self.icon_only_widget)
        self.collegeButton1.setObjectName(u"collegeButton1")
        icon3 = QIcon()
        icon3.addFile(u":/imgs/imgs/college_white_transparent.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.collegeButton1.setIcon(icon3)
        self.collegeButton1.setIconSize(QSize(30, 30))
        self.collegeButton1.setCheckable(True)
        self.collegeButton1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.collegeButton1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 375, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_15.addWidget(self.icon_only_widget)

        self.full_menu_widget = QWidget(self.centralwidget)
        self.full_menu_widget.setObjectName(u"full_menu_widget")
        self.full_menu_widget.setAutoFillBackground(False)
        self.full_menu_widget.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.homeButton2 = QPushButton(self.full_menu_widget)
        self.homeButton2.setObjectName(u"homeButton2")
        self.homeButton2.setMinimumSize(QSize(50, 50))
        self.homeButton2.setMaximumSize(QSize(50, 50))
        self.homeButton2.setIcon(icon)
        self.homeButton2.setIconSize(QSize(40, 40))
        self.homeButton2.setCheckable(True)
        self.homeButton2.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.homeButton2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.studentButton2 = QPushButton(self.full_menu_widget)
        self.studentButton2.setObjectName(u"studentButton2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.studentButton2.sizePolicy().hasHeightForWidth())
        self.studentButton2.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(11)
        font.setBold(False)
        self.studentButton2.setFont(font)
        self.studentButton2.setStyleSheet(u"")
        self.studentButton2.setIcon(icon1)
        self.studentButton2.setIconSize(QSize(30, 30))
        self.studentButton2.setCheckable(True)
        self.studentButton2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.studentButton2)

        self.programButton2 = QPushButton(self.full_menu_widget)
        self.programButton2.setObjectName(u"programButton2")
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(11)
        self.programButton2.setFont(font1)
        self.programButton2.setIcon(icon2)
        self.programButton2.setIconSize(QSize(30, 30))
        self.programButton2.setCheckable(True)
        self.programButton2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.programButton2)

        self.collegeButton2 = QPushButton(self.full_menu_widget)
        self.collegeButton2.setObjectName(u"collegeButton2")
        self.collegeButton2.setFont(font1)
        self.collegeButton2.setIcon(icon3)
        self.collegeButton2.setIconSize(QSize(30, 30))
        self.collegeButton2.setCheckable(True)
        self.collegeButton2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.collegeButton2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(105, 381, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.horizontalLayout_15.addWidget(self.full_menu_widget)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(2)
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.gridLayout_2 = QGridLayout(self.mainPage)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.mainPage)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.mainPage)
        self.studentPage = QWidget()
        self.studentPage.setObjectName(u"studentPage")
        self.verticalLayout_5 = QVBoxLayout(self.studentPage)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_7 = QWidget(self.studentPage)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(12)
        sizePolicy3.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy3)
        self.horizontalLayout_10 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_7 = QFrame(self.widget_7)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(12)
        sizePolicy4.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy4)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_7)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_5 = QFrame(self.frame_7)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy5)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.comboBox_29 = QComboBox(self.frame_5)
        self.comboBox_29.setObjectName(u"comboBox_29")
        sizePolicy.setHeightForWidth(self.comboBox_29.sizePolicy().hasHeightForWidth())
        self.comboBox_29.setSizePolicy(sizePolicy)
        self.comboBox_29.setMinimumSize(QSize(85, 28))
        self.comboBox_29.setMaximumSize(QSize(85, 28))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        self.comboBox_29.setFont(font2)

        self.horizontalLayout_18.addWidget(self.comboBox_29)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lineEdit_19 = QLineEdit(self.frame_5)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.lineEdit_19.sizePolicy().hasHeightForWidth())
        self.lineEdit_19.setSizePolicy(sizePolicy6)
        self.lineEdit_19.setMinimumSize(QSize(200, 0))
        self.lineEdit_19.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_11.addWidget(self.lineEdit_19)

        self.searchButton_16 = QPushButton(self.frame_5)
        self.searchButton_16.setObjectName(u"searchButton_16")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.searchButton_16.sizePolicy().hasHeightForWidth())
        self.searchButton_16.setSizePolicy(sizePolicy7)
        icon4 = QIcon()
        icon4.addFile(u":/imgs/imgs/search_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.searchButton_16.setIcon(icon4)
        self.searchButton_16.setIconSize(QSize(20, 20))

        self.horizontalLayout_11.addWidget(self.searchButton_16)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_11)

        self.horizontalSpacer_11 = QSpacerItem(28, 25, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_11)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.pushButton_52 = QPushButton(self.frame_5)
        self.pushButton_52.setObjectName(u"pushButton_52")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.pushButton_52.sizePolicy().hasHeightForWidth())
        self.pushButton_52.setSizePolicy(sizePolicy8)
        font3 = QFont()
        font3.setFamilies([u"Verdana"])
        font3.setPointSize(9)
        self.pushButton_52.setFont(font3)
        icon5 = QIcon()
        icon5.addFile(u":/imgs/imgs/add_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_52.setIcon(icon5)
        self.pushButton_52.setIconSize(QSize(20, 20))
        self.pushButton_52.setCheckable(True)
        self.pushButton_52.setAutoExclusive(True)

        self.horizontalLayout_38.addWidget(self.pushButton_52)

        self.pushButton_43 = QPushButton(self.frame_5)
        self.pushButton_43.setObjectName(u"pushButton_43")
        sizePolicy8.setHeightForWidth(self.pushButton_43.sizePolicy().hasHeightForWidth())
        self.pushButton_43.setSizePolicy(sizePolicy8)
        self.pushButton_43.setFont(font3)
        icon6 = QIcon()
        icon6.addFile(u":/imgs/imgs/edit_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_43.setIcon(icon6)
        self.pushButton_43.setIconSize(QSize(20, 20))

        self.horizontalLayout_38.addWidget(self.pushButton_43)

        self.pushButton_44 = QPushButton(self.frame_5)
        self.pushButton_44.setObjectName(u"pushButton_44")
        sizePolicy8.setHeightForWidth(self.pushButton_44.sizePolicy().hasHeightForWidth())
        self.pushButton_44.setSizePolicy(sizePolicy8)
        self.pushButton_44.setFont(font3)
        icon7 = QIcon()
        icon7.addFile(u":/imgs/imgs/delete_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_44.setIcon(icon7)
        self.pushButton_44.setIconSize(QSize(20, 20))

        self.horizontalLayout_38.addWidget(self.pushButton_44)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_38)

        self.horizontalSpacer_12 = QSpacerItem(28, 25, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_12)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.comboBox_28 = QComboBox(self.frame_5)
        self.comboBox_28.setObjectName(u"comboBox_28")
        sizePolicy8.setHeightForWidth(self.comboBox_28.sizePolicy().hasHeightForWidth())
        self.comboBox_28.setSizePolicy(sizePolicy8)
        self.comboBox_28.setFont(font2)

        self.horizontalLayout_39.addWidget(self.comboBox_28)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_39)


        self.verticalLayout_17.addWidget(self.frame_5)

        self.studentTable = QTableWidget(self.frame_7)
        if (self.studentTable.columnCount() < 6):
            self.studentTable.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.studentTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.studentTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        self.studentTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        self.studentTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        self.studentTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font2);
        self.studentTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.studentTable.setObjectName(u"studentTable")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(15)
        sizePolicy9.setHeightForWidth(self.studentTable.sizePolicy().hasHeightForWidth())
        self.studentTable.setSizePolicy(sizePolicy9)

        self.verticalLayout_17.addWidget(self.studentTable)


        self.horizontalLayout_10.addWidget(self.frame_7)

        self.widget_10 = QWidget(self.widget_7)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy10.setHorizontalStretch(4)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy10)
        self.widget_10.setMinimumSize(QSize(300, 0))
        self.widget_10.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_18 = QVBoxLayout(self.widget_10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_2 = QWidget(self.widget_10)
        self.widget_2.setObjectName(u"widget_2")
        self.frame_8 = QFrame(self.widget_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(0, 0, 282, 291))
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy11.setHorizontalStretch(2)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy11)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.comboBox_16 = QComboBox(self.frame_8)
        self.comboBox_16.setObjectName(u"comboBox_16")
        self.comboBox_16.setGeometry(QRect(110, 210, 91, 31))
        self.comboBox_17 = QComboBox(self.frame_8)
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.setObjectName(u"comboBox_17")
        self.comboBox_17.setGeometry(QRect(110, 170, 91, 31))
        self.comboBox_18 = QComboBox(self.frame_8)
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.setObjectName(u"comboBox_18")
        self.comboBox_18.setGeometry(QRect(110, 130, 91, 31))
        self.lineEdit_10 = QLineEdit(self.frame_8)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(110, 90, 161, 31))
        self.lineEdit_11 = QLineEdit(self.frame_8)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setGeometry(QRect(110, 50, 161, 31))
        self.lineEdit_12 = QLineEdit(self.frame_8)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setGeometry(QRect(110, 10, 161, 31))
        self.label_20 = QLabel(self.frame_8)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 10, 71, 31))
        font4 = QFont()
        font4.setFamilies([u"Verdana"])
        font4.setPointSize(10)
        self.label_20.setFont(font4)
        self.label_21 = QLabel(self.frame_8)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 50, 71, 31))
        self.label_21.setFont(font4)
        self.label_22 = QLabel(self.frame_8)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 90, 71, 31))
        self.label_22.setFont(font4)
        self.label_23 = QLabel(self.frame_8)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 130, 71, 31))
        self.label_23.setFont(font4)
        self.label_24 = QLabel(self.frame_8)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(10, 170, 71, 31))
        self.label_24.setFont(font4)
        self.label_25 = QLabel(self.frame_8)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(10, 210, 71, 31))
        self.label_25.setFont(font4)
        self.addStudentButton = QPushButton(self.frame_8)
        self.addStudentButton.setObjectName(u"addStudentButton")
        self.addStudentButton.setGeometry(QRect(160, 250, 111, 31))
        font5 = QFont()
        font5.setFamilies([u"Verdana"])
        font5.setPointSize(10)
        font5.setBold(True)
        self.addStudentButton.setFont(font5)

        self.verticalLayout_18.addWidget(self.widget_2)


        self.horizontalLayout_10.addWidget(self.widget_10)


        self.verticalLayout_5.addWidget(self.widget_7)

        self.stackedWidget.addWidget(self.studentPage)
        self.programPage = QWidget()
        self.programPage.setObjectName(u"programPage")
        self.horizontalLayout_6 = QHBoxLayout(self.programPage)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_9 = QWidget(self.programPage)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy3.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy3)
        self.horizontalLayout_12 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_10 = QFrame(self.widget_9)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy4.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy4)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_6 = QFrame(self.frame_10)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy5.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy5)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.comboBox_30 = QComboBox(self.frame_6)
        self.comboBox_30.setObjectName(u"comboBox_30")
        sizePolicy.setHeightForWidth(self.comboBox_30.sizePolicy().hasHeightForWidth())
        self.comboBox_30.setSizePolicy(sizePolicy)
        self.comboBox_30.setMinimumSize(QSize(85, 28))
        self.comboBox_30.setMaximumSize(QSize(85, 28))
        self.comboBox_30.setFont(font2)

        self.horizontalLayout_19.addWidget(self.comboBox_30)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lineEdit_20 = QLineEdit(self.frame_6)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        sizePolicy6.setHeightForWidth(self.lineEdit_20.sizePolicy().hasHeightForWidth())
        self.lineEdit_20.setSizePolicy(sizePolicy6)
        self.lineEdit_20.setMinimumSize(QSize(200, 0))
        self.lineEdit_20.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_13.addWidget(self.lineEdit_20)

        self.searchButton_17 = QPushButton(self.frame_6)
        self.searchButton_17.setObjectName(u"searchButton_17")
        sizePolicy7.setHeightForWidth(self.searchButton_17.sizePolicy().hasHeightForWidth())
        self.searchButton_17.setSizePolicy(sizePolicy7)
        self.searchButton_17.setIcon(icon4)
        self.searchButton_17.setIconSize(QSize(20, 20))

        self.horizontalLayout_13.addWidget(self.searchButton_17)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_13)

        self.horizontalSpacer_13 = QSpacerItem(28, 25, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_13)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.pushButton_51 = QPushButton(self.frame_6)
        self.pushButton_51.setObjectName(u"pushButton_51")
        sizePolicy8.setHeightForWidth(self.pushButton_51.sizePolicy().hasHeightForWidth())
        self.pushButton_51.setSizePolicy(sizePolicy8)
        self.pushButton_51.setFont(font3)
        self.pushButton_51.setIcon(icon5)
        self.pushButton_51.setIconSize(QSize(20, 20))
        self.pushButton_51.setCheckable(True)
        self.pushButton_51.setAutoExclusive(True)

        self.horizontalLayout_40.addWidget(self.pushButton_51)

        self.pushButton_46 = QPushButton(self.frame_6)
        self.pushButton_46.setObjectName(u"pushButton_46")
        sizePolicy8.setHeightForWidth(self.pushButton_46.sizePolicy().hasHeightForWidth())
        self.pushButton_46.setSizePolicy(sizePolicy8)
        self.pushButton_46.setFont(font3)
        self.pushButton_46.setIcon(icon6)
        self.pushButton_46.setIconSize(QSize(20, 20))

        self.horizontalLayout_40.addWidget(self.pushButton_46)

        self.pushButton_47 = QPushButton(self.frame_6)
        self.pushButton_47.setObjectName(u"pushButton_47")
        sizePolicy8.setHeightForWidth(self.pushButton_47.sizePolicy().hasHeightForWidth())
        self.pushButton_47.setSizePolicy(sizePolicy8)
        self.pushButton_47.setFont(font3)
        self.pushButton_47.setIcon(icon7)
        self.pushButton_47.setIconSize(QSize(20, 20))

        self.horizontalLayout_40.addWidget(self.pushButton_47)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_40)

        self.horizontalSpacer_14 = QSpacerItem(28, 25, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_14)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.comboBox_31 = QComboBox(self.frame_6)
        self.comboBox_31.setObjectName(u"comboBox_31")
        sizePolicy8.setHeightForWidth(self.comboBox_31.sizePolicy().hasHeightForWidth())
        self.comboBox_31.setSizePolicy(sizePolicy8)
        self.comboBox_31.setFont(font2)

        self.horizontalLayout_41.addWidget(self.comboBox_31)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_41)


        self.verticalLayout_19.addWidget(self.frame_6)

        self.programTable = QTableWidget(self.frame_10)
        if (self.programTable.columnCount() < 3):
            self.programTable.setColumnCount(3)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font2);
        self.programTable.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font2);
        self.programTable.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font2);
        self.programTable.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        self.programTable.setObjectName(u"programTable")
        sizePolicy9.setHeightForWidth(self.programTable.sizePolicy().hasHeightForWidth())
        self.programTable.setSizePolicy(sizePolicy9)

        self.verticalLayout_19.addWidget(self.programTable)


        self.horizontalLayout_12.addWidget(self.frame_10)

        self.widget_11 = QWidget(self.widget_9)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy10.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy10)
        self.widget_11.setMinimumSize(QSize(300, 0))
        self.widget_11.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_20 = QVBoxLayout(self.widget_11)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.widget_4 = QWidget(self.widget_11)
        self.widget_4.setObjectName(u"widget_4")
        self.frame_11 = QFrame(self.widget_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(0, 0, 282, 171))
        sizePolicy11.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy11)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.comboBox_26 = QComboBox(self.frame_11)
        self.comboBox_26.setObjectName(u"comboBox_26")
        self.comboBox_26.setGeometry(QRect(110, 90, 91, 31))
        self.lineEdit_18 = QLineEdit(self.frame_11)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setGeometry(QRect(110, 50, 161, 31))
        self.lineEdit_21 = QLineEdit(self.frame_11)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setGeometry(QRect(110, 10, 161, 31))
        self.label_27 = QLabel(self.frame_11)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 10, 101, 31))
        self.label_27.setFont(font4)
        self.label_28 = QLabel(self.frame_11)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(10, 50, 101, 31))
        self.label_28.setFont(font4)
        self.label_35 = QLabel(self.frame_11)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(10, 90, 101, 31))
        self.label_35.setFont(font4)
        self.addProgramButton = QPushButton(self.frame_11)
        self.addProgramButton.setObjectName(u"addProgramButton")
        self.addProgramButton.setGeometry(QRect(160, 130, 111, 31))
        self.addProgramButton.setFont(font5)

        self.verticalLayout_20.addWidget(self.widget_4)


        self.horizontalLayout_12.addWidget(self.widget_11)


        self.horizontalLayout_6.addWidget(self.widget_9)

        self.stackedWidget.addWidget(self.programPage)
        self.collegePage = QWidget()
        self.collegePage.setObjectName(u"collegePage")
        self.verticalLayout_6 = QVBoxLayout(self.collegePage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_8 = QWidget(self.collegePage)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy3.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy3)
        self.horizontalLayout_14 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_9 = QFrame(self.widget_8)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy4.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy4)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_9)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy5.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy5)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.comboBox_32 = QComboBox(self.frame_12)
        self.comboBox_32.setObjectName(u"comboBox_32")
        sizePolicy.setHeightForWidth(self.comboBox_32.sizePolicy().hasHeightForWidth())
        self.comboBox_32.setSizePolicy(sizePolicy)
        self.comboBox_32.setMinimumSize(QSize(85, 28))
        self.comboBox_32.setMaximumSize(QSize(85, 28))
        self.comboBox_32.setFont(font2)

        self.horizontalLayout_20.addWidget(self.comboBox_32)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lineEdit_22 = QLineEdit(self.frame_12)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        sizePolicy6.setHeightForWidth(self.lineEdit_22.sizePolicy().hasHeightForWidth())
        self.lineEdit_22.setSizePolicy(sizePolicy6)
        self.lineEdit_22.setMinimumSize(QSize(200, 0))
        self.lineEdit_22.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_16.addWidget(self.lineEdit_22)

        self.searchButton_18 = QPushButton(self.frame_12)
        self.searchButton_18.setObjectName(u"searchButton_18")
        sizePolicy7.setHeightForWidth(self.searchButton_18.sizePolicy().hasHeightForWidth())
        self.searchButton_18.setSizePolicy(sizePolicy7)
        self.searchButton_18.setIcon(icon4)
        self.searchButton_18.setIconSize(QSize(20, 20))

        self.horizontalLayout_16.addWidget(self.searchButton_18)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_16)

        self.horizontalSpacer_15 = QSpacerItem(28, 25, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_15)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.pushButton_53 = QPushButton(self.frame_12)
        self.pushButton_53.setObjectName(u"pushButton_53")
        sizePolicy8.setHeightForWidth(self.pushButton_53.sizePolicy().hasHeightForWidth())
        self.pushButton_53.setSizePolicy(sizePolicy8)
        self.pushButton_53.setFont(font3)
        self.pushButton_53.setIcon(icon5)
        self.pushButton_53.setIconSize(QSize(20, 20))
        self.pushButton_53.setCheckable(True)
        self.pushButton_53.setAutoExclusive(True)

        self.horizontalLayout_42.addWidget(self.pushButton_53)

        self.pushButton_49 = QPushButton(self.frame_12)
        self.pushButton_49.setObjectName(u"pushButton_49")
        sizePolicy8.setHeightForWidth(self.pushButton_49.sizePolicy().hasHeightForWidth())
        self.pushButton_49.setSizePolicy(sizePolicy8)
        self.pushButton_49.setFont(font3)
        self.pushButton_49.setIcon(icon6)
        self.pushButton_49.setIconSize(QSize(20, 20))

        self.horizontalLayout_42.addWidget(self.pushButton_49)

        self.pushButton_50 = QPushButton(self.frame_12)
        self.pushButton_50.setObjectName(u"pushButton_50")
        sizePolicy8.setHeightForWidth(self.pushButton_50.sizePolicy().hasHeightForWidth())
        self.pushButton_50.setSizePolicy(sizePolicy8)
        self.pushButton_50.setFont(font3)
        self.pushButton_50.setIcon(icon7)
        self.pushButton_50.setIconSize(QSize(20, 20))

        self.horizontalLayout_42.addWidget(self.pushButton_50)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_42)

        self.horizontalSpacer_16 = QSpacerItem(28, 25, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_16)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.comboBox_33 = QComboBox(self.frame_12)
        self.comboBox_33.setObjectName(u"comboBox_33")
        sizePolicy8.setHeightForWidth(self.comboBox_33.sizePolicy().hasHeightForWidth())
        self.comboBox_33.setSizePolicy(sizePolicy8)
        self.comboBox_33.setFont(font2)

        self.horizontalLayout_43.addWidget(self.comboBox_33)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_43)


        self.verticalLayout_21.addWidget(self.frame_12)

        self.collegeTable = QTableWidget(self.frame_9)
        if (self.collegeTable.columnCount() < 2):
            self.collegeTable.setColumnCount(2)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font2);
        self.collegeTable.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font2);
        self.collegeTable.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        self.collegeTable.setObjectName(u"collegeTable")
        sizePolicy9.setHeightForWidth(self.collegeTable.sizePolicy().hasHeightForWidth())
        self.collegeTable.setSizePolicy(sizePolicy9)

        self.verticalLayout_21.addWidget(self.collegeTable)


        self.horizontalLayout_14.addWidget(self.frame_9)

        self.widget_12 = QWidget(self.widget_8)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy10.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy10)
        self.widget_12.setMinimumSize(QSize(300, 0))
        self.widget_12.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_22 = QVBoxLayout(self.widget_12)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.widget_6 = QWidget(self.widget_12)
        self.widget_6.setObjectName(u"widget_6")
        self.frame_13 = QFrame(self.widget_6)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(0, 0, 282, 131))
        sizePolicy11.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy11)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.lineEdit_15 = QLineEdit(self.frame_13)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setGeometry(QRect(110, 50, 161, 31))
        self.lineEdit_16 = QLineEdit(self.frame_13)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setGeometry(QRect(110, 10, 161, 31))
        self.label_29 = QLabel(self.frame_13)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 10, 101, 31))
        self.label_29.setFont(font4)
        self.label_30 = QLabel(self.frame_13)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(10, 50, 101, 31))
        self.label_30.setFont(font4)
        self.addCollegeButton = QPushButton(self.frame_13)
        self.addCollegeButton.setObjectName(u"addCollegeButton")
        self.addCollegeButton.setGeometry(QRect(160, 90, 111, 31))
        self.addCollegeButton.setFont(font5)

        self.verticalLayout_22.addWidget(self.widget_6)


        self.horizontalLayout_14.addWidget(self.widget_12)


        self.verticalLayout_6.addWidget(self.widget_8)

        self.stackedWidget.addWidget(self.collegePage)

        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)

        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 40))
        self.widget.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menuButton = QPushButton(self.widget)
        self.menuButton.setObjectName(u"menuButton")
        sizePolicy.setHeightForWidth(self.menuButton.sizePolicy().hasHeightForWidth())
        self.menuButton.setSizePolicy(sizePolicy)
        self.menuButton.setMinimumSize(QSize(40, 40))
        self.menuButton.setMaximumSize(QSize(40, 40))
        icon8 = QIcon()
        icon8.addFile(u":/imgs/imgs/menu_fixed.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuButton.setIcon(icon8)
        self.menuButton.setIconSize(QSize(30, 40))
        self.menuButton.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.menuButton)

        self.horizontalSpacer = QSpacerItem(236, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font6 = QFont()
        font6.setFamilies([u"Verdana"])
        font6.setPointSize(12)
        font6.setBold(True)
        self.label_2.setFont(font6)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(236, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 2)


        self.horizontalLayout_15.addWidget(self.widget_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menuButton.toggled.connect(self.icon_only_widget.setVisible)
        self.menuButton.toggled.connect(self.full_menu_widget.setHidden)
        self.studentButton1.toggled.connect(self.studentButton2.setChecked)
        self.programButton1.toggled.connect(self.programButton2.setChecked)
        self.collegeButton1.toggled.connect(self.collegeButton2.setChecked)
        self.studentButton2.toggled.connect(self.studentButton1.setChecked)
        self.programButton2.toggled.connect(self.programButton1.setChecked)
        self.collegeButton2.toggled.connect(self.collegeButton1.setChecked)
        self.pushButton_52.clicked["bool"].connect(self.widget_10.setVisible)
        self.pushButton_51.clicked["bool"].connect(self.widget_11.setVisible)
        self.pushButton_53.clicked["bool"].connect(self.widget_12.setVisible)
        self.homeButton1.toggled.connect(self.homeButton2.setChecked)
        self.homeButton2.toggled.connect(self.homeButton1.setChecked)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Student Information System", None))
        self.homeButton1.setText("")
        self.studentButton1.setText("")
        self.programButton1.setText("")
        self.collegeButton1.setText("")
        self.homeButton2.setText("")
        self.studentButton2.setText(QCoreApplication.translate("MainWindow", u"Student", None))
        self.programButton2.setText(QCoreApplication.translate("MainWindow", u"Program", None))
        self.collegeButton2.setText(QCoreApplication.translate("MainWindow", u"College", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.comboBox_29.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search..", None))
        self.searchButton_16.setText("")
        self.pushButton_52.setText("")
        self.pushButton_43.setText("")
        self.pushButton_44.setText("")
        self.comboBox_28.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sort by", None))
        ___qtablewidgetitem = self.studentTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID Number", None));
        ___qtablewidgetitem1 = self.studentTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"First Name", None));
        ___qtablewidgetitem2 = self.studentTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem3 = self.studentTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem4 = self.studentTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Year Level", None));
        ___qtablewidgetitem5 = self.studentTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Program", None));
        self.comboBox_17.setItemText(0, QCoreApplication.translate("MainWindow", u"First Year", None))
        self.comboBox_17.setItemText(1, QCoreApplication.translate("MainWindow", u"Second Year", None))
        self.comboBox_17.setItemText(2, QCoreApplication.translate("MainWindow", u"Third Year", None))
        self.comboBox_17.setItemText(3, QCoreApplication.translate("MainWindow", u"Fourth Year", None))

        self.comboBox_18.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.comboBox_18.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))
        self.comboBox_18.setItemText(2, QCoreApplication.translate("MainWindow", u"Other", None))

        self.lineEdit_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ex. 2025-0001", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"ID #", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Year Level", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Program", None))
        self.addStudentButton.setText(QCoreApplication.translate("MainWindow", u"Add Student", None))
        self.comboBox_30.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search..", None))
        self.searchButton_17.setText("")
        self.pushButton_51.setText("")
        self.pushButton_46.setText("")
        self.pushButton_47.setText("")
        self.comboBox_31.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sort by", None))
        ___qtablewidgetitem6 = self.programTable.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Program Code", None));
        ___qtablewidgetitem7 = self.programTable.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Program Name", None));
        ___qtablewidgetitem8 = self.programTable.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"College Code", None));
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Program Code", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Program Name", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"College Code", None))
        self.addProgramButton.setText(QCoreApplication.translate("MainWindow", u"Add Program", None))
        self.comboBox_32.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search..", None))
        self.searchButton_18.setText("")
        self.pushButton_53.setText("")
        self.pushButton_49.setText("")
        self.pushButton_50.setText("")
        self.comboBox_33.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sort by", None))
        ___qtablewidgetitem9 = self.collegeTable.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"College Code", None));
        ___qtablewidgetitem10 = self.collegeTable.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"College Name", None));
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"College Code", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"College Name", None))
        self.addCollegeButton.setText(QCoreApplication.translate("MainWindow", u"Add College", None))
        self.menuButton.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Student Information System", None))
    # retranslateUi

