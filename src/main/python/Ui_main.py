# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/mac/Data/code/MagmaGameClient/src/main/python/main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(563, 568)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 14, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 350, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 380, 541, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 2, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 4, 2, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 3, 2, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 1, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(330, 60, 221, 291))
        self.textBrowser.setObjectName("textBrowser")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(318, 5, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 60, 312, 291))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.minecraftCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.minecraftCheckBox.setObjectName("minecraftCheckBox")
        self.gridLayout_2.addWidget(self.minecraftCheckBox, 1, 1, 1, 1)
        self.factorioLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.factorioLabel.setObjectName("factorioLabel")
        self.gridLayout_2.addWidget(self.factorioLabel, 0, 0, 1, 1)
        self.factorioCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.factorioCheckBox.setObjectName("factorioCheckBox")
        self.gridLayout_2.addWidget(self.factorioCheckBox, 0, 1, 1, 1)
        self.minecraftLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.minecraftLabel.setObjectName("minecraftLabel")
        self.gridLayout_2.addWidget(self.minecraftLabel, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 563, 20))
        self.menubar.setObjectName("menubar")
        self.menuGame_Selector = QtWidgets.QMenu(self.menubar)
        self.menuGame_Selector.setObjectName("menuGame_Selector")
        self.menuChat = QtWidgets.QMenu(self.menubar)
        self.menuChat.setObjectName("menuChat")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuGame_Selector.menuAction())
        self.menubar.addAction(self.menuChat.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Game Activator"))
        self.label_4.setText(_translate("MainWindow", "Custom Forwarding"))
        self.label_6.setText(_translate("MainWindow", "Custom Two"))
        self.label_8.setText(_translate("MainWindow", "Custom Four"))
        self.label_9.setText(_translate("MainWindow", "Custom Five"))
        self.checkBox.setText(_translate("MainWindow", "Connected"))
        self.checkBox_3.setText(_translate("MainWindow", "Connected"))
        self.label_5.setText(_translate("MainWindow", "Custom One"))
        self.checkBox_5.setText(_translate("MainWindow", "Connected"))
        self.checkBox_4.setText(_translate("MainWindow", "Connected"))
        self.checkBox_2.setText(_translate("MainWindow", "Connected"))
        self.label_7.setText(_translate("MainWindow", "Custom Three"))
        self.lineEdit.setText(_translate("MainWindow", "Port"))
        self.lineEdit_2.setText(_translate("MainWindow", "Port"))
        self.lineEdit_3.setText(_translate("MainWindow", "Port"))
        self.lineEdit_4.setText(_translate("MainWindow", "Port"))
        self.lineEdit_5.setText(_translate("MainWindow", "Port"))
        self.label_10.setText(_translate("MainWindow", "Log"))
        self.minecraftCheckBox.setText(_translate("MainWindow", "Connected"))
        self.factorioLabel.setText(_translate("MainWindow", "Factorio"))
        self.factorioCheckBox.setText(_translate("MainWindow", "Connected"))
        self.minecraftLabel.setText(_translate("MainWindow", "Minecraft"))
        self.label_2.setText(_translate("MainWindow", "IP: localhost:34197"))
        self.label_3.setText(_translate("MainWindow", "IP: localhost:25565"))
        self.menuGame_Selector.setTitle(_translate("MainWindow", "Game Selector"))
        self.menuChat.setTitle(_translate("MainWindow", "Chat"))