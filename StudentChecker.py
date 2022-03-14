
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import qrcode
import datetime
from datetime import date
import time
import random
import pyodbc
from PyQt5.QtCore import QVariant
from win32api import GetSystemMetrics
from Ex import *
import Ex
class Ui_MainWindow(object):
    _QrLiveTimer = QtCore.QTimer()
    _globalTime=0
    _TTL=0


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        if GetSystemMetrics(0)==1366 and GetSystemMetrics(1)==768:
            MainWindow.resize(500, 400)
            MainWindow.setMinimumSize(QtCore.QSize(500, 650))
            MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
            MainWindow.setGeometry(0,0,500,650)
        else:
            MainWindow.resize(600,850)
            MainWindow.setMinimumSize(QtCore.QSize(600, 850))
            MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        desktop = QtWidgets.QDesktopWidget()
        rect = desktop.availableGeometry(desktop.primaryScreen())
        center = rect.center()
        center.setX(center.x() - (MainWindow.width() // 2))
        center.setY(center.y() - (MainWindow.height() // 2))
        MainWindow.move(center)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("EmC_4fzD_vA.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.stackedWidget1 = QtWidgets.QStackedWidget(self.centralwidget)
# 1---------------------------------------------
        self.stackedWidget1.setObjectName("stackedWidget1")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
# ---------------
# INPUT PAGE BEGIN
# ---------------
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setText("")
        if GetSystemMetrics(0)==1366 and GetSystemMetrics(1)==768:
            self.label_2.setPixmap(QtGui.QPixmap("EmC_4fzD_vA (2).jpg"))
        else:
            self.label_2.setPixmap(QtGui.QPixmap("EmC_4fzD_vA (1).jpg"))
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label = QtWidgets.QLabel(self.page)
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        if GetSystemMetrics(0)==1366 and GetSystemMetrics(1)==768:
            font.setPointSize(28)
        else:
            font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(    "color: rgb(255, 107, 0);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.login = QtWidgets.QLineEdit(self.page)
        if GetSystemMetrics(0)==1366 and GetSystemMetrics(1)==768:
            self.login.setMinimumSize(QtCore.QSize(280, 30))
        else:
            self.login.setMinimumSize(QtCore.QSize(350,35))
        self.login.setStyleSheet("border:1px solid rgb(140, 140, 140);\n"
                                 "border-radius:10px;\n"
                                 "font: 12pt \"Montserrat\";\n"
                                 "padding-left: 7px;\n"
                                 "")
        self.login.setObjectName("login")
        self.verticalLayout.addWidget(self.login, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.passw = QtWidgets.QLineEdit(self.page)
        if GetSystemMetrics(0) == 1366 and GetSystemMetrics(1) == 768:
            self.passw.setMinimumSize(QtCore.QSize(280, 30))
        else:
            self.passw.setMinimumSize(QtCore.QSize(350, 35))
        self.passw.setStyleSheet("border:1px solid rgb(140, 140, 140);\n"
                                 "border-radius:10px;\n"
                                 "font: 12pt \"Montserrat\";\n"
                                 "padding-left: 7px;\n"
                                 "")
        self.passw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passw.setObjectName("passw")
        self.verticalLayout.addWidget(self.passw, 0, QtCore.Qt.AlignCenter|QtCore.Qt.AlignVCenter)
        spacerItem3 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.innetw = QtWidgets.QCheckBox(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.innetw.sizePolicy().hasHeightForWidth())
        self.innetw.setSizePolicy(sizePolicy)
        if GetSystemMetrics(0)==1366 and GetSystemMetrics(1)==768:
            self.innetw.setMinimumSize(QtCore.QSize(280, 30))
        else:
            self.innetw.setMinimumSize(QtCore.QSize(340, 20))
            self.innetw.setMaximumSize(QtCore.QSize(200, 100))
        self.innetw.setStyleSheet("font: 12pt \"Montserrat\";\n"
                                  "color: rgb(130, 130, 130);\n"
                                  "")
        self.innetw.setIconSize(QtCore.QSize(30, 30))
        self.innetw.setObjectName("innetw")
        self.verticalLayout.addWidget(self.innetw, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_8 = QtWidgets.QLabel(self.page)
        if GetSystemMetrics(0) == 1366 and GetSystemMetrics(1) == 768:
            self.label_8.setMinimumSize(QtCore.QSize(280, 30))
            self.label_8.setMaximumSize(QtCore.QSize(280, 30))
        else:
             self.label_8.setMinimumSize(QtCore.QSize(340, 30))
        self.label_8.setStyleSheet("font: 9pt \"Montserrat\";\n""color:white")
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8, 0, QtCore.Qt.AlignHCenter)
        spacerItem4 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.avt_but = QtWidgets.QPushButton(self.page)
        if GetSystemMetrics(0) == 1366 and GetSystemMetrics(1) == 768:
            self.avt_but.setMinimumSize(QtCore.QSize(280, 30))
            self.avt_but.setMaximumSize(QtCore.QSize(280, 30))
        else:
            self.avt_but.setMinimumSize(QtCore.QSize(350, 45))
            self.avt_but.setMaximumSize(QtCore.QSize(350, 50))
        self.avt_but.setStyleSheet("QPushButton{\n"
                                   "border:1px solid rgb(140, 140, 140);\n"
                                   "border-radius:10px;\n"
                                   "font: 13pt \"Montserrat\";\n"
                                   "padding-left: 7px;\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "background-color: qlineargradient(spread:pad, x1:0.528, y1:0.301136,"
                                   " x2:0.522, y2:0.0227273, stop:0.169154 rgba(255, 102, 0, 255),"
                                   " stop:0.910448 rgba(212, 83, 0, 255));\n"
                                   "}\n"
                                   "QPushButton:hover {\n"
                                   " background-color:  qlineargradient(spread:pad, x1:0.528, y1:0.301136,"
                                   " x2:0.522, y2:0.0227273, stop:0.169154 rgba(240, 87, 0, 240),"
                                   " stop:0.910448 rgba(200, 71, 0, 243));\n"
                                   "}\n"
                                   "QPushButton:!hover {\n"
                                   "background-color:  qlineargradient(spread:pad, x1:0.528, y1:0.301136,"
                                   " x2:0.522, y2:0.0227273,"
                                   " stop:0.169154 rgba(255, 102, 0, 255), stop:0.910448 rgba(212, 83, 0, 255));\n"
                                   "}\n"
                                   "QPushButton:pressed { \n"
                                   " background-color:  qlineargradient(spread:pad, x1:0.528,"
                                   " y1:0.301136, x2:0.522, y2:0.0227273, stop:0.169154 rgba(220, 67, 0, 220),"
                                   " stop:0.910448 rgba(180, 51, 0, 223));\n"
                                   "}\n"
                                   "")
        self.avt_but.setObjectName("avt_but")
        self.verticalLayout.addWidget(self.avt_but, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem5 = QtWidgets.QSpacerItem(20, 49, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.stackedWidget1.addWidget(self.page)
# 1 END AND INPUT PAGE END
# ----------------------------

#2 -----------------------------------
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
# RASPISANIE PAGE BEGIN---------
# ----------------------------
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.fox_img_11 = QtWidgets.QLabel(self.page_2)
        if GetSystemMetrics(0) == 1366 and GetSystemMetrics(1) == 768:
            self.fox_img_11.setMinimumSize(QtCore.QSize(55, 85))
            self.fox_img_11.setMaximumSize(QtCore.QSize(30, 80))
        else:
            self.fox_img_11.setMinimumSize(QtCore.QSize(65, 95))
            self.fox_img_11.setMaximumSize(QtCore.QSize(40, 90))
        self.fox_img_11.setStyleSheet("border:0px;\n"
                                      "background-color: rgb(255, 189, 0);\n"
                                      "padding-left: 8px;")
        self.fox_img_11.setText("")
        self.fox_img_11.setPixmap(QtGui.QPixmap("54_oooo.plus1.jpg"))
        self.fox_img_11.setObjectName("fox_img_11")
        self.horizontalLayout_22.addWidget(self.fox_img_11, 0, QtCore.Qt.AlignTop)
        self.username_labl_11 = QtWidgets.QLabel(self.page_2)
        self.username_labl_11.setMinimumSize(QtCore.QSize(120, 0))
        self.username_labl_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.username_labl_11.setStyleSheet("background-color: rgb(255, 100, 129);\n"
                                            "font: 12pt \"Montserrat\";\n"
                                            "background-color: rgb(255, 189, 0);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "padding-left: 5px;")
        self.username_labl_11.setObjectName("username_labl_11")
        self.horizontalLayout_22.addWidget(self.username_labl_11)
        self.stackedWidget2 = QtWidgets.QStackedWidget(self.page_2)
        self.stackedWidget2.setObjectName("stackedWidget2")
        self.page_22 = QtWidgets.QWidget()
        self.page_22.setObjectName("page_22")
        self.verticalLayout_50 = QtWidgets.QVBoxLayout(self.page_22)
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName("verticalLayout_50")
        self.rasp_lab2 = QtWidgets.QLabel(self.page_22)
        self.rasp_lab2.setMinimumSize(QtCore.QSize(493, 90))
        self.rasp_lab2.setMaximumSize(QtCore.QSize(1677725, 1677725))
        self.rasp_lab2.setStyleSheet("color:white;\n"
                                     "background-color: qlineargradient(spread:pad, x1:0.626726, y1:0.523,"
                                     " x2:0.97, y2:0.517455, stop:0.169154 rgba(255, 189, 0, 255),"
                                     " stop:0.910448 rgba(255, 127, 0, 226));\n"
                                     "font:  28pt \"Montserrat\";\n"
                                     "padding-right: 70px;\n"
                                     "")
        self.rasp_lab2.setAlignment(QtCore.Qt.AlignCenter)
        self.rasp_lab2.setObjectName("rasp_lab2")
        self.verticalLayout_50.addWidget(self.rasp_lab2)
        self.stackedWidget2.addWidget(self.page_22)
        self.page_23 = QtWidgets.QWidget()
        self.page_23.setObjectName("page_23")
        self.verticalLayout_51 = QtWidgets.QVBoxLayout(self.page_23)
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName("verticalLayout_51")
        self.rasp_lab1 = QtWidgets.QLabel(self.page_23)
        self.rasp_lab1.setMinimumSize(QtCore.QSize(493, 90))
        self.rasp_lab1.setMaximumSize(QtCore.QSize(1677725, 1677725))
        self.rasp_lab1.setStyleSheet("color:white;\n"
                                     "background-color: qlineargradient(spread:pad, x1:0.626726, y1:0.523,"
                                     " x2:0.97, y2:0.517455, stop:0.169154 rgba(255, 189, 0, 255),"
                                     " stop:0.910448 rgba(255, 127, 0, 226));\n"
                                     "font:  28pt \"Montserrat\";\n"
                                     "padding-right: 90px;\n"
                                     "")
        self.rasp_lab1.setAlignment(QtCore.Qt.AlignCenter)
        self.rasp_lab1.setObjectName("rasp_lab1")
        self.verticalLayout_51.addWidget(self.rasp_lab1)
        self.stackedWidget2.addWidget(self.page_23)
        self.page_24 = QtWidgets.QWidget()
        self.page_24.setObjectName("page_24")
        self.verticalLayout_52 = QtWidgets.QVBoxLayout(self.page_24)
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName("verticalLayout_52")
        self.rasp_lab3 = QtWidgets.QLabel(self.page_24)
        self.rasp_lab3.setMinimumSize(QtCore.QSize(0, 95))
        self.rasp_lab3.setMaximumSize(QtCore.QSize(16777215, 95))
        self.rasp_lab3.setStyleSheet("color:white;\n"
                                     "background-color: qlineargradient(spread:pad, x1:0.626726, y1:0.523, x2:0.97,"
                                     " y2:0.517455, stop:0.169154 rgba(255, 189, 0, 255),"
                                     " stop:0.910448 rgba(255, 127, 0, 226));\n"
                                     "font:  28pt \"Montserrat\";\n"
                                     "\n"
                                     "\n"
                                     "")
        self.rasp_lab3.setAlignment(QtCore.Qt.AlignCenter)
        self.rasp_lab3.setObjectName("rasp_lab3")
        self.verticalLayout_52.addWidget(self.rasp_lab3)
        self.stackedWidget2.addWidget(self.page_24)
        self.horizontalLayout_22.addWidget(self.stackedWidget2)
        self.horizontalLayout_21.addLayout(self.horizontalLayout_22)
        self.exitprof_11 = QtWidgets.QPushButton(self.page_2)
        self.exitprof_11.setMinimumSize(QtCore.QSize(140, 95))
        self.exitprof_11.setMaximumSize(QtCore.QSize(16777215, 95))
        self.exitprof_11.setStyleSheet("QPushButton{"
                                       "background-color: rgb(255, 142, 29);\n"
                                       "border:0px;\n"
                                       "font:  10pt \"Montserrat\";\n"
                                       "color: white;\n"
                                       "padding-right: 5px;"
                                       "}"
                                       "\n"
                                       "QPushButton:hover{\n"
                                       "background-color: rgb(250, 137, 24)\n"
                                       "}\n"
                                       "QPushButton:!hover {\n"
                                       "background-color: rgb(255, 142, 29)\n"
                                       "}\n"
                                       "QPushButton:pressed { \n"
                                       "background-color: rgb(245, 132, 19);\n"
                                       "}")
        self.exitprof_11.setText("Выйти из профиля")
        self.exitprof_11.setObjectName("exitprof_11")
        self.horizontalLayout_21.addWidget(self.exitprof_11, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_3.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.verticalLayout_43 = QtWidgets.QVBoxLayout()
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.qr_but_5 = QtWidgets.QPushButton(self.page_2)
        self.qr_but_5.setMinimumSize(QtCore.QSize(220, 45))
        self.qr_but_5.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.qr_but_5.setFont(font)
        self.qr_but_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.qr_but_5.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.qr_but_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.qr_but_5.setAutoFillBackground(False)
        self.qr_but_5.setStyleSheet("QPushButton{\n"
                                    "border:0px;\n"
                                    "font:  14pt \"Montserrat\";\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "padding-left:7px;\n"
                                    "margin:1px;\n"
                                    "margin-top:0px;\n"
                                    "margin-bottom:0px;\n"
                                    "text-align: left;\n"
                                    "border-radius: 10px;\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    " background-color: #C4C4C4\n"
                                    "}\n"
                                    "QPushButton:!hover {\n"
                                    "background-color: white\n"
                                    "}\n"
                                    "QPushButton:pressed { \n"
                                    "background-color: rgb(170, 170, 170);\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("KDDrYR9vBYw.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.qr_but_5.setIcon(icon3)
        self.qr_but_5.setIconSize(QtCore.QSize(35, 35))
        self.qr_but_5.setAutoDefault(False)
        self.qr_but_5.setDefault(False)
        self.qr_but_5.setObjectName("qr_but_5")
        self.verticalLayout_43.addWidget(self.qr_but_5)
        self.rasp_but_5 = QtWidgets.QPushButton(self.page_2)
        self.rasp_but_5.setMinimumSize(QtCore.QSize(220, 45))
        self.rasp_but_5.setStyleSheet("QPushButton{\n"
                                      "border:0px;\n"
                                      "font:  14pt \"Montserrat\";\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "padding-left:7px;\n"
                                      "margin:1px;\n"
                                      "margin-top:0px;\n"
                                      "margin-bottom:0px;\n"
                                      "text-align: left;\n"
                                      "border-radius: 10px;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "background-color: #C4C4C4\n"
                                      "}\n"
                                      "QPushButton:!hover {\n"
                                      "background-color: white\n"
                                      "}\n"
                                      "QPushButton:pressed { \n"
                                      "background-color: rgb(170, 170, 170);\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("qcjlEydLQ4s.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rasp_but_5.setIcon(icon4)
        self.rasp_but_5.setIconSize(QtCore.QSize(35, 35))
        self.rasp_but_5.setObjectName("rasp_but_5")
        self.verticalLayout_43.addWidget(self.rasp_but_5)
        self.pos_but_5 = QtWidgets.QPushButton(self.page_2)
        self.pos_but_5.setMinimumSize(QtCore.QSize(220, 45))
        self.pos_but_5.setStyleSheet("QPushButton{\n"
                                     "border:0px;\n"
                                     "font:  14pt \"Montserrat\";\n"
                                     "background-color: rgb(255, 255, 255);\n"
                                     "padding-left:7px;\n"
                                     "margin:1px;\n"
                                     "margin-top:0px;\n"
                                     "margin-bottom:0px;\n"
                                     "text-align: left;\n"
                                     "border-radius: 10px;\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "background-color: #C4C4C4\n"
                                     "}\n"
                                     "QPushButton:!hover {\n"
                                     "background-color: white\n"
                                     "}\n"
                                     "QPushButton:pressed { \n"
                                     "background-color: rgb(170, 170, 170);\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pos_but_5.setIcon(icon5)
        self.pos_but_5.setIconSize(QtCore.QSize(35, 35))
        self.pos_but_5.setObjectName("pos_but_5")
        self.verticalLayout_43.addWidget(self.pos_but_5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_43.addItem(spacerItem6)
        self.horizontalLayout_19.addLayout(self.verticalLayout_43)
        self.l1_5 = QtWidgets.QFrame(self.page_2)
        self.l1_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.l1_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.l1_5.setObjectName("l1_5")
        self.horizontalLayout_19.addWidget(self.l1_5, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_47 = QtWidgets.QVBoxLayout()
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName("verticalLayout_47")
        self.stackedWidget3 = QtWidgets.QStackedWidget(self.page_2)
        self.stackedWidget3.setEnabled(True)
        self.stackedWidget3.setObjectName("stackedWidget3")
        self.page_21 = QtWidgets.QWidget()
        self.page_21.setObjectName("page_21")
        self.verticalLayout_44 = QtWidgets.QVBoxLayout(self.page_21)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.verticalLayout_45 = QtWidgets.QVBoxLayout()
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_45.addItem(spacerItem7)
        self.label_7 = QtWidgets.QLabel(self.page_21)
        self.label_7.setStyleSheet("")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("Qr.jpg"))
        self.label_7.setObjectName("label_7")
        self.verticalLayout_45.addWidget(self.label_7, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_45.addItem(spacerItem8)
        self.progressBar_5 = QtWidgets.QProgressBar(self.page_21)
        self.progressBar_5.setMinimumSize(QtCore.QSize(350, 28))
        self.progressBar_5.setStyleSheet("QProgressBar {\n"
                                         "border-radius: 14px;\n"
                                         "border: 1px solid;\n"
                                         "padding: 1px;\n"
                                         "}\n"
                                         "QProgressBar::chunk {\n"
                                         "border-radius: 12px;\n"
                                         "background-color: qlineargradient(spread:pad, x1:0.626726, y1:0.523,"
                                         " x2:0.97, y2:0.517455, stop:0.169154 rgba(255, 189, 0, 255),"
                                         " stop:0.910448 rgba(255, 127, 0, 226));\n"
                                         "}\n"
                                         "")
        self.progressBar_5.setMaximum(100)
        self.progressBar_5.setProperty("value", 0)
        self.progressBar_5.setFormat("")
        self.progressBar_5.setObjectName("progressBar_5")
        self.verticalLayout_45.addWidget(self.progressBar_5, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_45.addItem(spacerItem9)
        self.verticalLayout_44.addLayout(self.verticalLayout_45)
        self.stackedWidget3.addWidget(self.page_21)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.lab4 = QtWidgets.QLabel(self.page_3)
        self.lab4.setMinimumSize(QtCore.QSize(50, 50))
        self.lab4.setStyleSheet("font: 16pt \"Montserrat\";")
        self.lab4.setAlignment(QtCore.Qt.AlignCenter)
        self.lab4.setObjectName("lab4")
        self.verticalLayout_9.addWidget(self.lab4)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page_3)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 890, 699))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setObjectName("gridLayout")
        self.pb_1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pb_1.setMinimumSize(QtCore.QSize(50, 40))
        self.pb_1.setStyleSheet("QPushButton{\n"
                                         "border-radius: 10px;\n"
                                         "background-color: qlineargradient(spread:pad, x1:0.0948209, y1:0.437, x2:0.870428, y2:0.409, stop:0.522388 rgba(255, 190, 17, 242), stop:0.845771 rgba(255, 158, 21, 252));\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "font: 14pt \"Montserrat\";\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.149254 rgba(255, 148, 0, 255), stop:0.930348 rgba(255, 102, 0, 255));\n"
                                         "}\n"
                                         "QPushButton:!hover {\n"
                                         "background-color: qlineargradient(spread:pad, x1:0.0948209, y1:0.437, x2:0.870428, y2:0.409, stop:0.522388 rgba(255, 190, 17, 242), stop:0.845771 rgba(255, 158, 21, 252));\n"
                                         "}\n"
                                         "QPushButton:pressed { \n"
                                         "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.263682 rgba(255, 148, 0, 255), stop:0.930348 rgba(255, 102, 0, 255));\n"
                                         "}")
        self.pb_1.setObjectName("pb1")
        self.gridLayout.addWidget(self.pb_1, 1, 1, 1, 1)
        self.pb_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pb_2.setMinimumSize(QtCore.QSize(50, 40))
        self.pb_2.setStyleSheet("QPushButton{\n"
                                        "border-radius: 10px;\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.0948209, y1:0.437, x2:0.870428, y2:0.409, stop:0.522388 rgba(255, 190, 17, 242), stop:0.845771 rgba(255, 158, 21, 252));\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "font: 14pt \"Montserrat\";\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.149254 rgba(255, 148, 0, 255), stop:0.930348 rgba(255, 102, 0, 255));\n"
                                        "}\n"
                                        "QPushButton:!hover {\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.0948209, y1:0.437, x2:0.870428, y2:0.409, stop:0.522388 rgba(255, 190, 17, 242), stop:0.845771 rgba(255, 158, 21, 252));\n"
                                        "}\n"
                                        "QPushButton:pressed { \n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.263682 rgba(255, 148, 0, 255), stop:0.930348 rgba(255, 102, 0, 255));\n"
                                        "}")
        self.pb_2.setObjectName("pb_2")
        self.gridLayout.addWidget(self.pb_2, 2, 0, 1, 1)
        self.pb_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pb_3.setMinimumSize(QtCore.QSize(50, 40))
        self.pb_3.setStyleSheet("QPushButton{\n"
                                        "border-radius: 10px;\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.0948209, y1:0.437, x2:0.870428, y2:0.409, stop:0.522388 rgba(255, 190, 17, 242), stop:0.845771 rgba(255, 158, 21, 252));\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "font: 14pt \"Montserrat\";\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.149254 rgba(255, 148, 0, 255), stop:0.930348 rgba(255, 102, 0, 255));\n"
                                        "}\n"
                                        "QPushButton:!hover {\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.0948209, y1:0.437, x2:0.870428, y2:0.409, stop:0.522388 rgba(255, 190, 17, 242), stop:0.845771 rgba(255, 158, 21, 252));\n"
                                        "}\n"
                                        "QPushButton:pressed { \n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.263682 rgba(255, 148, 0, 255), stop:0.930348 rgba(255, 102, 0, 255));\n"
                                        "}")
        self.pb_3.setObjectName("pb_3")
        self.gridLayout.addWidget(self.pb_3, 0, 1, 1, 1)
        self.pb_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pb_4.setMinimumSize(QtCore.QSize(50, 40))
        self.pb_4.setStyleSheet("QPushButton{\n"
                                        "border-radius: 10px;\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.0948209, y1:0.437, x2:0.870428, y2:0.409, stop:0.522388 rgba(255, 190, 17, 242), stop:0.845771 rgba(255, 158, 21, 252));\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "font: 14pt \"Montserrat\";\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.149254 rgba(255, 148, 0, 255), stop:0.930348 rgba(255, 102, 0, 255));\n"
                                        "}\n"
                                        "QPushButton:!hover {\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.0948209, y1:0.437, x2:0.870428, y2:0.409, stop:0.522388 rgba(255, 190, 17, 242), stop:0.845771 rgba(255, 158, 21, 252));\n"
                                        "}\n"
                                        "QPushButton:pressed { \n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.263682 rgba(255, 148, 0, 255), stop:0.930348 rgba(255, 102, 0, 255));\n"
                                        "}")
        self.pb_4.setObjectName("pb_4")
        self.gridLayout.addWidget(self.pb_4, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem10, 3, 0, 1, 1)
        self.pb_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pb_5.setMinimumSize(QtCore.QSize(50, 40))
        self.pb_5.setStyleSheet("QPushButton{\n"
                                        "border-radius: 10px;\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.0948209, y1:0.437, x2:0.870428, y2:0.409, stop:0.522388 rgba(255, 190, 17, 242), stop:0.845771 rgba(255, 158, 21, 252));\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "font: 14pt \"Montserrat\";\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.149254 rgba(255, 148, 0, 255), stop:0.930348 rgba(255, 102, 0, 255));\n"
                                        "}\n"
                                        "QPushButton:!hover {\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.0948209, y1:0.437, x2:0.870428, y2:0.409, stop:0.522388 rgba(255, 190, 17, 242), stop:0.845771 rgba(255, 158, 21, 252));\n"
                                        "}\n"
                                        "QPushButton:pressed { \n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.263682 rgba(255, 148, 0, 255), stop:0.930348 rgba(255, 102, 0, 255));\n"
                                        "}")
        self.pb_5.setObjectName("pb_5")
        self.gridLayout.addWidget(self.pb_5, 1, 0, 1, 1)
        self.pb_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pb_6.setMinimumSize(QtCore.QSize(50, 40))
        self.pb_6.setStyleSheet("QPushButton{\n"
                                         "border-radius: 10px;\n"
                                         "background-color: qlineargradient(spread:pad, x1:0.0948209, y1:0.437, x2:0.870428, y2:0.409, stop:0.522388 rgba(255, 190, 17, 242), stop:0.845771 rgba(255, 158, 21, 252));\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "font: 14pt \"Montserrat\";\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.149254 rgba(255, 148, 0, 255), stop:0.930348 rgba(255, 102, 0, 255));\n"
                                         "}\n"
                                         "QPushButton:!hover {\n"
                                         "background-color: qlineargradient(spread:pad, x1:0.0948209, y1:0.437, x2:0.870428, y2:0.409, stop:0.522388 rgba(255, 190, 17, 242), stop:0.845771 rgba(255, 158, 21, 252));\n"
                                         "}\n"
                                         "QPushButton:pressed { \n"
                                         "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.263682 rgba(255, 148, 0, 255), stop:0.930348 rgba(255, 102, 0, 255));\n"
                                         "}")
        self.pb_6.setObjectName("pb_6")
        self.gridLayout.addWidget(self.pb_6, 2, 1, 1, 1)
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea_2.setLineWidth(0)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.addWidget(self.scrollArea_2)
        self.stackedWidget3.addWidget(self.page_3)
        self.stackedWidgetPage1_4 = QtWidgets.QWidget()
        self.stackedWidgetPage1_4.setObjectName("stackedWidgetPage1_4")
        self.verticalLayout_46 = QtWidgets.QVBoxLayout(self.stackedWidgetPage1_4)
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName("verticalLayout_46")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.stackedWidgetPage1_4)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 890, 749))
        self.scrollAreaWidgetContents.setStyleSheet("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.comboBox_3 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        if GetSystemMetrics(0) == 1366 and GetSystemMetrics(1) == 768:
            self.comboBox_3.setMinimumSize(QtCore.QSize(0, 60))
            self.comboBox_3.setMaximumSize(QtCore.QSize(16777215, 60))
            self.comboBox_3.setStyleSheet("QComboBox {\n"
                                          "    border: 0px;\n"
                                          "    border-radius: 15px;\n"
                                          "    padding: 1px 10px 1px 10px;\n"
                                          "    color: rgb(255, 255, 255);\n"
                                          "    font: 13pt \"MingLiU_HKSCS-ExtB\";\n"
                                          "    height: 80px;\n"
                                          "    margin: 10px;\n"
                                          "}\n"
                                          "QComboBox QAbstractItemView {\n"
                                          "    border: 2px solid darkgray;\n"
                                          "    selection-background-color: lightgray;\n"
                                          "}\n"
                                          "QComboBox:editable {\n"
                                          "    background: white;\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox:!editable, QComboBox::drop-down:editable {\n"
                                          "    \n"
                                          "    background-color: qlineargradient(spread:pad, x1:0.617124, y1:0.534, x2:0.940299, y2:0.523, stop:0.149254 rgba(255, 189, 0, 255), stop:0.905473 rgba(255, 148, 0, 255));\n"
                                          "}\n"
                                          "\n"
                                          "/* QComboBox gets the \"on\" state when the popup is open */\n"
                                          "QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
                                          "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                          "                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
                                          "                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox:on { /* shift the text when the popup opens */\n"
                                          "    padding-top: 3px;\n"
                                          "    padding-left: 4px;\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox::drop-down {\n"
                                          "    subcontrol-origin: padding;\n"
                                          "    subcontrol-position: top right;\n"
                                          "width: 20px;\n"
                                          "padding-right: 10px;\n"
                                          "    border-left-color: darkgray;\n"
                                          "    border-left-style: solid; /* just a single line */\n"
                                          "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                          "    border-bottom-right-radius: 3px;\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox::down-arrow {\n"
                                          "    image: url(arrow251.jpg);\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                          "    top: 1px;\n"
                                          "    left: 1px;\n"
                                          "}")
        else:
            self.comboBox_3.setMinimumSize(QtCore.QSize(0, 70))
            self.comboBox_3.setMaximumSize(QtCore.QSize(16777215, 65))
            self.comboBox_3.setStyleSheet("QComboBox {\n"
                                     "    border: 0px;\n"
                                      "    border-radius: 20px;\n"
                                      "    padding: 1px 18px 1px 20px;\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    font: 13pt \"MingLiU_HKSCS-ExtB\";\n"
                                      "    height: 80px;\n"
                                      "    margin: 10px;\n"
                                      "margin-top: 11px;"
                                      "}\n"
                                      "QComboBox QAbstractItemView {\n"
                                      "    border: 2px solid darkgray;\n"
                                      "    selection-background-color: lightgray;\n"
                                      "}\n"
                                      "QComboBox:editable {\n"
                                      "    background: white;\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox:!editable, QComboBox::drop-down:editable {\n"
                                      "    \n"
                                      "    background-color: qlineargradient(spread:pad, x1:0.617124, y1:0.534, x2:0.940299, y2:0.523, stop:0.149254 rgba(255, 189, 0, 255), stop:0.905473 rgba(255, 148, 0, 255));\n"
                                      "}\n"
                                      "\n"
                                      "/* QComboBox gets the \"on\" state when the popup is open */\n"
                                      "QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
                                      "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                      "                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
                                      "                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox:on { /* shift the text when the popup opens */\n"
                                      "    padding-top: 3px;\n"
                                      "    padding-left: 4px;\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox::drop-down {\n"
                                      "    subcontrol-origin: padding;\n"
                                      "    subcontrol-position: top right;\n"
                                      "width: 20px;\n"
                                      "padding-right: 30px;\n"
                                      "    border-left-color: darkgray;\n"
                                      "    border-left-style: solid; /* just a single line */\n"
                                      "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                      "    border-bottom-right-radius: 3px;\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox::down-arrow {\n"
                                      "    image: url(arrow25.jpg);\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                      "    top: 1px;\n"
                                      "    left: 1px;\n"
                                      "}")
        self.comboBox_3.setIconSize(QtCore.QSize(25, 25))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox_3.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_3, 0, QtCore.Qt.AlignBottom)
        self.comboBox_5 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        if GetSystemMetrics(0) == 1366 and GetSystemMetrics(1) == 768:
            self.comboBox_5.setMinimumSize(QtCore.QSize(0, 60))
            self.comboBox_5.setMaximumSize(QtCore.QSize(16777215, 60))
            self.comboBox_5.setStyleSheet("QComboBox {\n"
                                          "    border: 0px;\n"
                                          "    border-radius: 15px;\n"
                                          "    padding: 1px 10px 1px 10px;\n"
                                          "    color: rgb(255, 255, 255);\n"
                                          "    font: 13pt \"MingLiU_HKSCS-ExtB\";\n"
                                          "    height: 80px;\n"
                                          "    margin: 10px;\n"
                                          "}\n"
                                          "QComboBox QAbstractItemView {\n"
                                          "    border: 2px solid darkgray;\n"
                                          "    selection-background-color: lightgray;\n"
                                          "}\n"
                                          "QComboBox:editable {\n"
                                          "    background: white;\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox:!editable, QComboBox::drop-down:editable {\n"
                                          "    \n"
                                          "    background-color: qlineargradient(spread:pad, x1:0.617124, y1:0.534, x2:0.940299, y2:0.523, stop:0.149254 rgba(255, 189, 0, 255), stop:0.905473 rgba(255, 148, 0, 255));\n"
                                          "}\n"
                                          "\n"
                                          "/* QComboBox gets the \"on\" state when the popup is open */\n"
                                          "QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
                                          "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                          "                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
                                          "                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox:on { /* shift the text when the popup opens */\n"
                                          "    padding-top: 3px;\n"
                                          "    padding-left: 4px;\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox::drop-down {\n"
                                          "    subcontrol-origin: padding;\n"
                                          "    subcontrol-position: top right;\n"
                                          "width: 20px;\n"
                                          "padding-right: 20px;\n"
                                          "    border-left-color: darkgray;\n"
                                          "    border-left-style: solid; /* just a single line */\n"
                                          "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                          "    border-bottom-right-radius: 3px;\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox::down-arrow {\n"
                                          "    image: url(arrow251.jpg);\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                          "    top: 1px;\n"
                                          "    left: 1px;\n"
                                          "}")
        else:
            self.comboBox_5.setMinimumSize(QtCore.QSize(0, 70))
            self.comboBox_5.setMaximumSize(QtCore.QSize(16777215, 65))
            self.comboBox_5.setStyleSheet("QComboBox {\n"
                                          "    border: 0px;\n"
                                          "    border-radius: 20px;\n"
                                          "    padding: 1px 18px 1px 20px;\n"
                                          "    color: rgb(255, 255, 255);\n"
                                          "    font: 13pt \"MingLiU_HKSCS-ExtB\";\n"
                                          "    height: 80px;\n"
                                          "    margin: 10px;\n"
                                          "}\n"
                                          "QComboBox QAbstractItemView {\n"
                                          "    border: 2px solid darkgray;\n"
                                          "    selection-background-color: lightgray;\n"
                                          "}\n"
                                          "QComboBox:editable {\n"
                                          "    background: white;\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox:!editable, QComboBox::drop-down:editable {\n"
                                          "    \n"
                                          "    background-color: qlineargradient(spread:pad, x1:0.617124, y1:0.534, x2:0.940299, y2:0.523, stop:0.149254 rgba(255, 189, 0, 255), stop:0.905473 rgba(255, 148, 0, 255));\n"
                                          "}\n"
                                          "\n"
                                          "/* QComboBox gets the \"on\" state when the popup is open */\n"
                                          "QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
                                          "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                          "                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
                                          "                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox:on { /* shift the text when the popup opens */\n"
                                          "    padding-top: 3px;\n"
                                          "    padding-left: 4px;\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox::drop-down {\n"
                                          "    subcontrol-origin: padding;\n"
                                          "    subcontrol-position: top right;\n"
                                          "width: 20px;\n"
                                          "padding-right: 30px;\n"
                                          "    border-left-color: darkgray;\n"
                                          "    border-left-style: solid; /* just a single line */\n"
                                          "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                          "    border-bottom-right-radius: 3px;\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox::down-arrow {\n"
                                          "    image: url(arrow25.jpg);\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                          "    top: 1px;\n"
                                          "    left: 1px;\n"
                                          "}")
        self.comboBox_5.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.comboBox_5.setAutoFillBackground(False)
        self.comboBox_5.setEditable(False)
        self.comboBox_5.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox_5.setIconSize(QtCore.QSize(25, 25))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.149254 rgba(255, 195, 0, 255), stop:0.930348 rgba(255, 148, 0, 255));\n"
                                      "border: 0px;\n"
                                      "border-radius: 5px;\n"
                                      "font: 10pt \"Montserrat\";\n"
                                      "padding: 4px;\n"
                                      "text-align: center;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.149254 rgba(255, 148, 0, 255), stop:0.930348 rgba(255, 102, 0, 255));\n"
                                      "}\n"
                                      "QPushButton:!hover {\n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.149254 rgba(255, 195, 0, 255), stop:0.930348 rgba(255, 148, 0, 255));\n"
                                      "}\n"
                                      "QPushButton:pressed { \n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.263682 rgba(255, 148, 0, 255), stop:0.930348 rgba(255, 102, 0, 255));\n"
                                      "}\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_5.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 7, -1, 7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("font: 13pt \"Segoe UI Symbol\";\n"
                                    "padding-left: 3px;\n"
                                    "border: 1px solid rgb(140, 140, 140);"
                                    "border-radius: 10px;"
                                    "\n"
                                    "\n"
                                    "")
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_6.addWidget(self.lineEdit)
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton_2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.0948209, y1:0.437, x2:0.870428, y2:0.409, stop:0.522388 rgba(255, 190, 17, 242), stop:0.845771 rgba(255, 158, 21, 252));\n"
            "color: rgb(255, 255, 255);\n"
            "font: 12pt \"Montserrat\";\n"
            "border:0px;\n"
            "margin-right: 4px;"
            "border-radius: 10px;"
            "margin-left: 7px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_6.addWidget(self.pushButton_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_8.addLayout(self.verticalLayout_5)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.verticalLayout_46.addLayout(self.horizontalLayout)
        self.stackedWidget3.addWidget(self.stackedWidgetPage1_4)
        self.page_13 = QtWidgets.QWidget()
        self.page_13.setObjectName("page_13")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_13)
        self.verticalLayout_10.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.page_13)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font:  30pt \"Montserrat\";")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_10.addWidget(self.label_9, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.pushButton_6 = QtWidgets.QPushButton(self.page_13)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.234, y1:0.42, x2:0.885572, y2:0.426, stop:0.263682 rgba(76, 255, 76, 226), stop:0.930348 rgba(77, 242, 83, 255));\n"
                                        "border: 0px;\n"
                                        "border-radius: 5px;\n"
                                        "margin :7px 7px 0px 7px;\n"
                                        "font: 10pt \"Montserrat\";\n"
                                        "padding: 4px;\n"
                                        "text-align: center;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.149254 rgba(255, 148, 0, 255), stop:0.930348 rgba(255, 102, 0, 255));\n"
                                        "}\n"
                                        "QPushButton:!hover {\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.0948209, y1:0.437, x2:0.870428, y2:0.409, stop:0.522388 rgba(255, 190, 17, 242), stop:0.845771 rgba(255, 158, 21, 252));\n"
                                        "}\n"
                                        "QPushButton:pressed { \n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.263682 rgba(255, 148, 0, 255), stop:0.930348 rgba(255, 102, 0, 255));\n"
                                        "}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_10.addWidget(self.pushButton_6, 0, QtCore.Qt.AlignLeft)
        self.stackedWidget3.addWidget(self.page_13)
        self.page_14 = QtWidgets.QWidget()
        self.page_14.setObjectName("page_14")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page_14)
        self.verticalLayout_11.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.pushButton_7 = QtWidgets.QPushButton(self.page_14)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.234, y1:0.42, x2:0.885572, y2:0.426, stop:0.263682 rgba(76, 255, 76, 226), stop:0.930348 rgba(77, 242, 83, 255));\n"
                                        "border: 0px;\n"
                                        "border-radius: 5px;\n"
                                        "margin-bottom :7px;\n"
                                        "font: 10pt \"Montserrat\";\n"
                                        "padding: 4px;\n"
                                        "text-align: center;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.149254 rgba(255, 148, 0, 255), stop:0.930348 rgba(255, 102, 0, 255));\n"
                                        "}\n"
                                        "QPushButton:!hover {\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.149254 rgba(255, 195, 0, 255), stop:0.930348 rgba(255, 148, 0, 255));\n"
                                        "}\n"
                                        "QPushButton:pressed { \n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.263682 rgba(255, 148, 0, 255), stop:0.930348 rgba(255, 102, 0, 255));\n"
                                        "}\n"
                                        "")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_11.addWidget(self.pushButton_7, 0, QtCore.Qt.AlignHCenter)
        self.label_10 = QtWidgets.QLabel(self.page_14)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("border: 1px solid;")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_11.addWidget(self.label_10)
        self.tableWidget_4 = QtWidgets.QTableWidget(self.page_14)
        self.tableWidget_4.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.verticalLayout_11.addWidget(self.tableWidget_4)
        self.pushButton_8 = QtWidgets.QPushButton(self.page_14)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.234, y1:0.42, x2:0.885572, y2:0.426, stop:0.263682 rgba(76, 255, 76, 226), stop:0.930348 rgba(77, 242, 83, 255));\n"
                                        "border: 0px;\n"
                                        "border-radius: 5px;\n"
                                        "margin :7px 7px 0px 7px;\n"
                                        "font: 10pt \"Montserrat\";\n"
                                        "padding: 4px;\n"
                                        "text-align: center;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.149254 rgba(255, 148, 0, 255), stop:0.930348 rgba(255, 102, 0, 255));\n"
                                        "}\n"
                                        "QPushButton:!hover {\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.0948209, y1:0.437, x2:0.870428, y2:0.409, stop:0.522388 rgba(255, 190, 17, 242), stop:0.845771 rgba(255, 158, 21, 252));\n"
                                        "}\n"
                                        "QPushButton:pressed { \n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.263682 rgba(255, 148, 0, 255), stop:0.930348 rgba(255, 102, 0, 255));\n"
                                        "}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_11.addWidget(self.pushButton_8, 0, QtCore.Qt.AlignLeft)
        self.stackedWidget3.addWidget(self.page_14)
        self.stackedWidgetPage2_4 = QtWidgets.QWidget()
        self.stackedWidgetPage2_4.setObjectName("stackedWidgetPage2_4")
        self.verticalLayout_48 = QtWidgets.QVBoxLayout(self.stackedWidgetPage2_4)
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName("verticalLayout_48")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.stackedWidgetPage2_4)
        self.pushButton_21.setStyleSheet("border: 0px;\n"
                                         "\n"
                                         "margin: 10px, 0px;")
        self.pushButton_21.setText("")
        if GetSystemMetrics(0) == 1366 and GetSystemMetrics(1) == 768:
            icon7 = QtGui.QIcon()
            icon7.addPixmap(QtGui.QPixmap("2 2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        else:
            icon7 = QtGui.QIcon()
            icon7.addPixmap(QtGui.QPixmap("2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_21.setIcon(icon7)
        self.pushButton_21.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_21.setObjectName("pushButton_21")
        self.horizontalLayout_20.addWidget(self.pushButton_21, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.comboBox = QtWidgets.QComboBox(self.stackedWidgetPage2_4)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 45))
        self.comboBox.setStyleSheet("QComboBox {\n"
                                    "outline: 0;\n"
                                    "    border: 0px;\n"
                                    "    border-radius: 20px;\n"
                                    "    padding: 1px 12px 1px 10px;\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "margin: 10px, 0px;\n"
                                    "    font: 15pt \"Montserrat\";\n"
                                    "background-color: qlineargradient(spread:pad, x1:0.617124, y1:0.534,"
                                    " x2:0.940299, y2:0.523, stop:0.149254 rgba(255, 189, 0, 255),"
                                    " stop:0.905473 rgba(255, 148, 0, 255));\n"
                                    "}\n"
                                    "QComboBox QAbstractItemView {\n"
                                    "    border: 0;\n"
                                    "outline: 0;\n"
                                    "    selection-background-color: lightgray;\n"
                                    "background-color: qlineargradient(spread:pad, x1:0.617124, y1:0.534,"
                                    " x2:0.940299, y2:0.523, stop:0.149254 rgba(255, 189, 0, 255),"
                                    " stop:0.905473 rgba(255, 148, 0, 255));\n"
                                    "}\n"
                                    "QComboBox:editable {\n"
                                    "    background: white;\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox:!editable, QComboBox::drop-down:editable {\n"
                                    "    \n"
                                    "    background-color: qlineargradient(spread:pad, x1:0.617124, y1:0.534,"
                                    " x2:0.940299, y2:0.523, stop:0.149254 rgba(255, 189, 0, 255),"
                                    " stop:0.905473 rgba(255, 148, 0, 255));\n"
                                    "}\n"
                                    "\n"
                                    "/* QComboBox gets the \"on\" state when the popup is open */\n"
                                    "QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
                                    "    background-color: qlineargradient(spread:pad, x1:0.617124,"
                                    " y1:0.534, x2:0.940299, y2:0.523, stop:0.149254 rgba(255, 189, 0, 255),"
                                    " stop:0.905473 rgba(255, 148, 0, 255));\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox:on { /* shift the text when the popup opens */\n"
                                    "    padding-top: 3px;\n"
                                    "    padding-left: 18px;\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox::drop-down {\n"
                                    "    subcontrol-origin: padding;\n"
                                    "    subcontrol-position: top right;\n"
                                    "border-radius: 40px;"
                                    "width: 20px;\n"
                                    "outline: 0;\n"
                                    "padding-right: 8px;\n"
                                    "    border-left-color: darkgray;\n"
                                    "    border-left-style: solid; /* just a single line */\n"
                                    "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                    "    border-bottom-right-radius: 3px;\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox::down-arrow {\n"
                                    "    image: url(arrow27.jpg);\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                    "    top: 1px;\n"
                                    "    left: 1px;\n"
                                    "}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_20.addWidget(self.comboBox, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.pushButton_23 = QtWidgets.QPushButton(self.stackedWidgetPage2_4)
        self.pushButton_23.setStyleSheet("border: 0px;\n"
                                         "\n"
                                         "margin: 10px,0px;")
        self.pushButton_23.setText("")
        if GetSystemMetrics(0) == 1366 and GetSystemMetrics(1) == 768:
            icon8 = QtGui.QIcon()
            icon8.addPixmap(QtGui.QPixmap("FWmrWriX2Bk 2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        else:
            icon8 = QtGui.QIcon()
            icon8.addPixmap(QtGui.QPixmap("FWmrWriX2Bk.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_23.setIcon(icon8)
        self.pushButton_23.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_23.setObjectName("pushButton_23")
        self.horizontalLayout_20.addWidget(self.pushButton_23, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.verticalLayout_48.addLayout(self.horizontalLayout_20)
        self.stackedWidget = QtWidgets.QStackedWidget(self.stackedWidgetPage2_4)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_9)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label2 = QtWidgets.QLabel(self.page_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.label2.setStyleSheet("margin-top: 53px;\n")
        self.verticalLayout_7.addWidget(self.label2, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_4 = QtWidgets.QLabel(self.page_9)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font:  28pt \"Montserrat\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.stackedWidget.addWidget(self.page_9)
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_11)
        self.verticalLayout_8.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_11)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.234, y1:0.42, x2:0.885572, y2:0.426, stop:0.263682 rgba(76, 255, 76, 226), stop:0.930348 rgba(77, 242, 83, 255));\n"
                                        "border: 0px;\n"
                                        "border-radius: 5px;\n"
                                        "margin-bottom :7px;\n"
                                        "font: 10pt \"Montserrat\";\n"
                                        "padding: 4px;\n"
                                        "text-align: center;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.149254 rgba(255, 148, 0, 255), stop:0.930348 rgba(255, 102, 0, 255));\n"
                                        "}\n"
                                        "QPushButton:!hover {\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.234, y1:0.42, x2:0.885572, y2:0.426, stop:0.263682 rgba(76, 255, 76, 226), stop:0.930348 rgba(77, 242, 83, 255));\n"
                                        "}\n"
                                        "QPushButton:pressed { \n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.263682 rgba(255, 148, 0, 255), stop:0.930348 rgba(255, 102, 0, 255));\n"
                                        "}\n"
                                        "")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_8.addWidget(self.pushButton_3, 0, QtCore.Qt.AlignHCenter)
        self.label_6 = QtWidgets.QLabel(self.page_11)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border: 1px solid;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.page_11)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.verticalLayout_8.addWidget(self.tableWidget_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.page_11)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.234, y1:0.42, x2:0.885572, y2:0.426, stop:0.263682 rgba(76, 255, 76, 226), stop:0.930348 rgba(77, 242, 83, 255));\n"
                                        "border: 0px;\n"
                                        "border-radius: 5px;\n"
                                        "margin :7px 7px 0px 7px;\n"
                                        "font: 10pt \"Montserrat\";\n"
                                        "padding: 4px;\n"
                                        "text-align: center;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.149254 rgba(255, 148, 0, 255), stop:0.930348 rgba(255, 102, 0, 255));\n"
                                        "}\n"
                                        "QPushButton:!hover {\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.0948209, y1:0.437, x2:0.870428, y2:0.409, stop:0.522388 rgba(255, 190, 17, 242), stop:0.845771 rgba(255, 158, 21, 252));\n"
                                        "}\n"
                                        "QPushButton:pressed { \n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.263682 rgba(255, 148, 0, 255), stop:0.930348 rgba(255, 102, 0, 255));\n"
                                        "}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_8.addWidget(self.pushButton_4, 0, QtCore.Qt.AlignLeft)
        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setObjectName("page_12")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_12)
        self.verticalLayout_9.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.page_12)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font:  30pt \"Montserrat\";")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_9.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.pushButton_5 = QtWidgets.QPushButton(self.page_12)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.234, y1:0.42, x2:0.885572, y2:0.426, stop:0.263682 rgba(76, 255, 76, 226), stop:0.930348 rgba(77, 242, 83, 255));\n"
                                        "border: 0px;\n"
                                        "border-radius: 5px;\n"
                                        "margin :7px 7px 0px 7px;\n"
                                        "font: 10pt \"Montserrat\";\n"
                                        "padding: 4px;\n"
                                        "text-align: center;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.149254 rgba(255, 148, 0, 255), stop:0.930348 rgba(255, 102, 0, 255));\n"
                                        "}\n"
                                        "QPushButton:!hover {\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.0948209, y1:0.437, x2:0.870428, y2:0.409, stop:0.522388 rgba(255, 190, 17, 242), stop:0.845771 rgba(255, 158, 21, 252));\n"
                                        "}\n"
                                        "QPushButton:pressed { \n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.454364, x2:1, y2:0.403, stop:0.263682 rgba(255, 148, 0, 255), stop:0.930348 rgba(255, 102, 0, 255));\n"
                                        "}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_9.addWidget(self.pushButton_5, 0, QtCore.Qt.AlignLeft)
        self.stackedWidget.addWidget(self.page_12)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_10)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_49 = QtWidgets.QVBoxLayout()
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName("verticalLayout_49")
        self.label_3 = QtWidgets.QLabel(self.stackedWidgetPage2_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("\n")
        self.verticalLayout_49.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
        self.para1_5 = QtWidgets.QLabel(self.page_10)
        self.para1_5.setMinimumSize(QtCore.QSize(30, 20))
        font = QtGui.QFont()
        font.setFamily("Mohave")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.para1_5.setFont(font)
        self.para1_5.setStyleSheet("text-align: right;\n"
                                   "font: 13pt \"Mohave\";\n"
                                   "color: #6B6B6B;\n"
                                   ""
                                   "margin-left:25px;\n"
                                   "color: #6B6B6B;")
        self.para1_5.setObjectName("para1_5")
        self.verticalLayout_49.addWidget(self.para1_5, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.para1line_5 = QtWidgets.QFrame(self.page_10)
        self.para1line_5.setStyleSheet("margin-right:50px;\n"
                                       "margin-left:50px;")
        self.para1line_5.setMidLineWidth(2)
        self.para1line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.para1line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.para1line_5.setObjectName("para1line_5")
        self.verticalLayout_49.addWidget(self.para1line_5)
        self.para2_5 = QtWidgets.QLabel(self.page_10)
        self.para2_5.setMinimumSize(QtCore.QSize(30, 50))
        self.para2_5.setStyleSheet("margin-top:50px;\n"
                                   "\n"
                                   "margin-left:25px;\n"
                                   "font: 12pt \"Mohave\";\n"
                                   "color: #6B6B6B;")
        self.para2_5.setObjectName("para2_5")
        self.verticalLayout_49.addWidget(self.para2_5, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.para2line_5 = QtWidgets.QFrame(self.stackedWidgetPage2_4)
        self.para2line_5.setStyleSheet("margin-right:50px;\n"
                                       "margin-left:50px;")
        self.para2line_5.setMidLineWidth(2)
        self.para2line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.para2line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.para2line_5.setObjectName("para2line_5")
        self.verticalLayout_49.addWidget(self.para2line_5)
        self.para3_5 = QtWidgets.QLabel(self.page_10)
        self.para3_5.setMinimumSize(QtCore.QSize(30, 50))
        self.para3_5.setStyleSheet("margin-top:50px;\n"
                                   "\n"
                                   "margin-left:25px;\n"
                                   "font: 13pt \"Mohave\";\n"
                                   "color: #6B6B6B;")
        self.para3_5.setObjectName("para3_5")
        self.verticalLayout_49.addWidget(self.para3_5, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.para3line_5 = QtWidgets.QFrame(self.page_10)
        self.para3line_5.setStyleSheet("margin-right:50px;\n"
                                       "margin-left:50px;")
        self.para3line_5.setMidLineWidth(2)
        self.para3line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.para3line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.para3line_5.setObjectName("para3line_5")
        self.verticalLayout_49.addWidget(self.para3line_5)
        self.para4_5 = QtWidgets.QLabel(self.page_10)
        self.para4_5.setMinimumSize(QtCore.QSize(30, 50))
        self.para4_5.setStyleSheet("margin-top:50px;\n"
                                   "\n"
                                   "margin-left:25px;\n"
                                   "font: 13pt \"Mohave\";\n"
                                   "color: #6B6B6B;")
        self.para4_5.setObjectName("para4_5")
        self.verticalLayout_49.addWidget(self.para4_5, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.para4line_5 = QtWidgets.QFrame(self.page_10)
        self.para4line_5.setStyleSheet("margin-right:50px;\n"
                                       "margin-left:50px;")
        self.para4line_5.setMidLineWidth(2)
        self.para4line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.para4line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.para4line_5.setObjectName("para4line_5")
        self.verticalLayout_49.addWidget(self.para4line_5)
        self.para5_5 = QtWidgets.QLabel(self.page_10)
        self.para5_5.setMinimumSize(QtCore.QSize(30, 50))
        self.para5_5.setStyleSheet("margin-top:50px;\n"
                                   "\n"
                                   "margin-left:25px;\n"
                                   "font: 13pt \"Mohave\";\n"
                                   "color: #6B6B6B;")
        self.para5_5.setObjectName("para5_5")
        self.verticalLayout_49.addWidget(self.para5_5, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.para5line_5 = QtWidgets.QFrame(self.stackedWidgetPage2_4)
        self.para5line_5.setStyleSheet("margin-right:50px;\n"
                                       "margin-left:50px;")
        self.para5line_5.setMidLineWidth(2)
        self.para5line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.para5line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.para5line_5.setObjectName("para5line_5")
        self.verticalLayout_49.addWidget(self.para5line_5)
        self.para6_5 = QtWidgets.QLabel(self.page_10)
        self.para6_5.setMinimumSize(QtCore.QSize(30, 50))
        self.para6_5.setStyleSheet("margin-top:50px;\n"
                                   "\n"
                                   "margin-left:25px;\n"
                                   "font: 13pt \"Mohave\";\n"
                                   "color: #6B6B6B;")
        self.para6_5.setObjectName("para6_5")
        self.verticalLayout_49.addWidget(self.para6_5, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.para6line_5 = QtWidgets.QFrame(self.page_10)
        self.para6line_5.setStyleSheet("margin-right:50px;\n"
                                       "margin-left:50px;")
        self.para6line_5.setMidLineWidth(2)
        self.para6line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.para6line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.para6line_5.setObjectName("para6line_5")
        self.verticalLayout_49.addWidget(self.para6line_5)
        self.para7_5 = QtWidgets.QLabel(self.page_10)
        self.para7_5.setMinimumSize(QtCore.QSize(30, 50))
        self.para7_5.setStyleSheet("margin-top:50px;\n"
                                   "\n"
                                   "margin-left:25px;\n"
                                   "font: 13pt \"Mohave\";\n"
                                   "color: #6B6B6B;")
        self.para7_5.setObjectName("para7_5")
        self.verticalLayout_49.addWidget(self.para7_5, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.para7line_5 = QtWidgets.QFrame(self.page_10)
        self.para7line_5.setStyleSheet("margin-right:50px;\n"
                                       "margin-left:50px;")
        self.para7line_5.setMidLineWidth(2)
        self.para7line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.para7line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.para7line_5.setObjectName("para7line_5")
        self.verticalLayout_49.addWidget(self.para7line_5)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_49.addItem(spacerItem11)
        self.verticalLayout_4.addLayout(self.verticalLayout_49)
        self.stackedWidget.addWidget(self.page_10)
        self.verticalLayout_48.addWidget(self.stackedWidget)
        self.stackedWidget3.addWidget(self.stackedWidgetPage2_4)
        self.verticalLayout_47.addWidget(self.stackedWidget3)
        self.horizontalLayout_19.addLayout(self.verticalLayout_47)
        self.verticalLayout_3.addLayout(self.horizontalLayout_19)
        self.stackedWidget1.addWidget(self.page_2)
        self.horizontalLayout_9.addWidget(self.stackedWidget1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.stackedWidget1.setCurrentIndex(0)
        self.stackedWidget2.setCurrentIndex(0)
        self.stackedWidget3.setCurrentIndex(2)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "StudentChecker"))
        self.label.setText(_translate("MainWindow", "StudentChecker"))
        self.login.setPlaceholderText(_translate("MainWindow", "Почта sfedu"))
        self.passw.setPlaceholderText(_translate("MainWindow", "Пароль"))
        self.innetw.setText(_translate("MainWindow", "Оставаться в сети"))
        self.label_8.setText(_translate("MainWindow", "Неправильно введены почта или пароль!"))
        self.avt_but.setText(_translate("MainWindow", "Авторизоваться"))
        self.username_labl_11.setText(_translate("MainWindow", ""))
        self.rasp_lab2.setText(_translate("MainWindow", "Расписание занятий"))
        self.rasp_lab1.setText(_translate("MainWindow", "Посещаемость"))
        self.rasp_lab3.setText(_translate("MainWindow", "QR-код"))
        self.qr_but_5.setText(_translate("MainWindow", "QR-код"))
        self.rasp_but_5.setText(_translate("MainWindow", "Расписание"))
        self.pos_but_5.setText(_translate("MainWindow", "Посещаемость"))
        self.lab4.setText(_translate("MainWindow", "Выберите дисциплину для генерации Qr-кода:"))
        self.pb_1.setText(_translate("MainWindow", "Резерв-2"))
        self.pb_2.setText(_translate("MainWindow", "Резерв-3"))
        self.pb_3.setText(_translate("MainWindow", "Основы проектной деятельности"))
        self.pb_4.setText(_translate("MainWindow", "Математика"))
        self.pb_5.setText(_translate("MainWindow", "Резерв-1"))
        self.pb_6.setText(_translate("MainWindow", "Резерв-4"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Выберите дисциплину"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Текущая пара"))
        self.label_3.setText(_translate("MainWindow", "Неделя: " + str(w)))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "1 Пара"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "2 Пара"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "3 Пара"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "4 Пара"))
        self.comboBox_5.setItemText(5, _translate("MainWindow", "5 Пара"))
        self.comboBox_5.setItemText(6, _translate("MainWindow", "6 Пара"))
        self.comboBox_5.setItemText(7, _translate("MainWindow", "7 Пара"))
        self.pushButton.setText(_translate("MainWindow", "Ручное редактирование"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "🔍 Введите ФИО студента"))
        self.pushButton_2.setText(_translate("MainWindow", "Поиск"))
        self.comboBox.setItemText(0, _translate("MainWindow", ""))
        self.comboBox.setItemText(1, _translate("MainWindow", "Понедельник"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Вторник"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Среда"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Четверг"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Пятница"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Суббота"))
        self.label_4.setText(_translate("MainWindow", "Расписание не найдено"))
        self.label2.setText(_translate("MainWindow", "Неделя: "+str(w)))
        self.label_9.setText(_translate("MainWindow", "Студент не найден"))
        self.pushButton_6.setText(_translate("MainWindow", "← Вернуться к общему списку"))
        self.pushButton_7.setText(_translate("MainWindow", "Ручное редактирование"))
        self.label_10.setText(_translate("MainWindow", "Результаты поиска:"))
        self.pushButton_8.setText(_translate("MainWindow", "← Вернуться к общему списку"))
        self.para1_5.setText(_translate("MainWindow", "1  пр.История Г-218    КТбо1-4, КТбо1-12"))
        self.para2_5.setText(_translate("MainWindow", "2"))
        self.para3_5.setText(_translate("MainWindow", "3"))
        self.para4_5.setText(_translate("MainWindow", "4  пр.Математика Д-312    КТбо1-1, КТсо1-3"))
        self.para5_5.setText(_translate("MainWindow", "5"))
        self.para6_5.setText(_translate("MainWindow", "6"))
        self.para7_5.setText(_translate("MainWindow", "7"))
        self.rasp_but_5.clicked.connect(Ex.gotorasp(self))
        self.qr_but_5.clicked.connect(Ex.menuchoice(self))
        self.pos_but_5.clicked.connect(Ex.gotoposCheck(self))
        self.avt_but.clicked.connect(Ex.gotorasp1(self))
        self.pushButton_21.clicked.connect(Ex.befWeek(self))
        self.pushButton_23.clicked.connect(Ex.nextWeek(self))
        self.exitprof_11.clicked.connect(Ex.gotoinput(self))
        self.pushButton_6.clicked.connect(Ex.returnToPos(self))
        self.pushButton_8.clicked.connect(Ex.returnToPos(self))
        self.comboBox.currentIndexChanged.connect(Ex.comboChange(self))
        self.pushButton.clicked.connect(Ex.checkReduct(self))
        self.pushButton_2.clicked.connect(Ex.Search(self))
        self.pushButton_7.clicked.connect(Ex.checkSearchReduct(self))
        self.pb_4.clicked.connect(Ex.startQrMatan())
        self.pb_3.clicked.connect(Ex.startQrProject())
        self.pb_5.clicked.connect(Ex.startQrRezerv1(self))
        self.pb_1.clicked.connect(Ex.startQrRezerv2(self))
        self.pb_2.clicked.connect(Ex.startQrRezerv3(self))
        self.pb_6.clicked.connect(Ex.startQrRezerv4(self))
# MAIN
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
