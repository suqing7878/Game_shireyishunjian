# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
# Form implementation generated from reading ui file 'win_demo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtGui import QPixmap

import txt


class Ui_MainWindow(object):

    def __init__(self):
        self.label2 = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(972, 647)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(690, 40, 250, 300))
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 520, 731, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 30, 611, 331))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(730, 360, 151, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 410, 851, 61))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 972, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "image"))
        self.label_2.setText(_translate("MainWindow", "膀胱："))
        self.label_3.setText(_translate("MainWindow", "水份："))
        self.label_4.setText(_translate("MainWindow", "羞耻度："))
        self.label_5.setText(_translate("MainWindow", "生命值："))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", " "))
        self.label_7.setText(_translate("MainWindow", " "))
        self.label_8.setText(_translate("MainWindow", " "))
        self.label_9.setText(_translate("MainWindow", " "))
        self.label_10.setText(_translate("MainWindow", " "))
        self.menu.setTitle(_translate("MainWindow", "点击此处开始游戏"))
        self.label.setPixmap(QPixmap("./image/3.png"))
        self.menu.addAction("开始")
        self.label_6.setText(f"<a href='#'></a>")
        self.label_6.repaint()
        self.i = 2

        #########################################################################################################################


        self.menu.triggered.connect(lambda: self.textBrowser.setHtml(txt.txt(1)))
        self.menu.triggered.connect(lambda: self.label_6.setText(f"<a href='#'>下一步</a>"))
        self.menu.triggered.connect(lambda: self.label_6.setText(f"<a href='#'>下一步</a>"))

        print(f'1:{self.i}')


        self.label_6.linkActivated.connect(lambda: self.label_2.setText(f"<a href='#'>膀胱：{self.i}</a>"))


        self.label_6.repaint()
        self.label_6.setText(f"<a href='#'>出发</a>")
        print(f'2:{self.i}')
        self.label_6.linkActivated.connect(lambda: self.textBrowser.setHtml(txt.txt(2)))
        self.label_6.linkActivated.connect(lambda: self.textBrowser.setHtml(txt.txt(3)))

        self.label_6.linkActivated.connect(lambda: self.label_6.setText(f"<a href='#'>出发</a>"))
        self.label_6.linkActivated.connect(lambda: self.label_7.setText(f"<a href='#'>吃点东西再出发</a>"))




        self.label_6.linkActivated.connect(lambda: self.textBrowser.setHtml(txt.txt(5)))
        self.label_7.linkActivated.connect(lambda: self.textBrowser.setHtml(txt.txt(4)))
        self.label_7.linkActivated.connect(lambda: self.label_6.setText(f"<a href='#'>下一步</a>"))
        self.label_7.linkActivated.connect(lambda: self.label_7.setText(f"<a href='#'></a>"))



        self.label_6.linkActivated.connect(lambda: self.label_6.setText(f"<a href='#'>去厕所</a>"))
        self.label_6.linkActivated.connect(lambda: self.label_7.setText(f"<a href='#'>上马车</a>"))
        self.label_6.linkActivated.connect(lambda: self.textBrowser.setHtml(txt.txt(6)))
        self.label_7.linkActivated.connect(lambda: self.textBrowser.setHtml('dsdsd'))

        #self.label_8.linkActivated.connect(lambda: self.textBrowser.setHtml(txt.txt(1)))


        
        self.label_6.linkActivated.connect(self.linkClicked)


    def linkClicked(self):
        if self.i<=10:
            self.label.setPixmap(QPixmap("./image/3.png"))


        if self.i > 10:
            self.label.setPixmap(QPixmap("./image/2.png"))
            self.label_8.setText(f"<a href='#'>12121</a>")
            self.label_6.setText(f"<a href='#'></a>")
            self.label_7.setText(f"<a href='#'></a>")
            self.textBrowser.setHtml("dddd")


        self.i = self.i + 1
        print(self.i)





