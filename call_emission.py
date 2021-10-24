import sys
# PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
# 导入designer工具生成的login模块
from emission import Ui_MainWindow
from get_distance import calculate_distance
from get_emissions import calculate_emissions


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        # 添加登录按钮信号和槽。注意display函数不加小括号()
        self.pushButton.clicked.connect(self.display)
        # 添加退出按钮信号和槽。调用close函数
        # self.buttonBox.clicked.connect(self.close)

    def display(self):
        # use text Edit.text()to get input"":::::::::::::::"
        origin_text = self.textEdit_origin.toPlainText()
        dest_text = self.textEdit_dest.toPlainText()
        mass_text = self.textEdit_mass.toPlainText()
        mode_text = self.comboBox_mode.currentText()
        dist = calculate_distance(origin_text, dest_text)
        emission_text = calculate_emissions(dist, mode_text, mass_text)
        # 利用text Browser控件对象setText()函数设置界面显示
        self.textBrowser_emission.setText(emission_text)

if __name__ == "__main__":
    # PyQt5 app needs QApplication object. sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # intialize
    myWin = MyMainForm()
    # show widgets on screen
    myWin.show()
    # run app, sys.exit method makes sure the app exeit completely
    sys.exit(app.exec_())

# emission.py:
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'emission2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(495, 376)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mass = QtWidgets.QLabel(self.centralwidget)
        self.mass.setGeometry(QtCore.QRect(30, 160, 101, 16))
        self.mass.setObjectName("mass")
        self.comboBox_mode = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_mode.setGeometry(QtCore.QRect(30, 230, 91, 32))
        self.comboBox_mode.setObjectName("comboBox_mode")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 231, 16))
        self.label.setObjectName("label")
        self.origin = QtWidgets.QLabel(self.centralwidget)
        self.origin.setGeometry(QtCore.QRect(30, 50, 58, 16))
        self.origin.setObjectName("origin")
        self.textEdit_mass = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_mass.setGeometry(QtCore.QRect(30, 180, 104, 21))
        self.textEdit_mass.setObjectName("textEdit_mass")
        self.textBrowser_emission = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_emission.setGeometry(QtCore.QRect(170, 70, 101, 21))
        self.textBrowser_emission.setObjectName("textBrowser_emission")
        self.modeTrans = QtWidgets.QLabel(self.centralwidget)
        self.modeTrans.setGeometry(QtCore.QRect(30, 220, 121, 16))
        self.modeTrans.setObjectName("modeTrans")
        self.textEdit_origin = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_origin.setGeometry(QtCore.QRect(30, 70, 104, 21))
        self.textEdit_origin.setObjectName("textEdit_origin")
        self.textEdit_dest = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_dest.setGeometry(QtCore.QRect(30, 120, 104, 21))
        self.textEdit_dest.setObjectName("textEdit_dest")
        self.emission = QtWidgets.QLabel(self.centralwidget)
        self.emission.setGeometry(QtCore.QRect(170, 50, 111, 16))
        self.emission.setObjectName("emission")
        self.destination = QtWidgets.QLabel(self.centralwidget)
        self.destination.setGeometry(QtCore.QRect(30, 100, 101, 16))
        self.destination.setObjectName("destination")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 60, 112, 32))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 495, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mass.setText(_translate("MainWindow", "Cargo Mass (kg)"))
        self.comboBox_mode.setItemText(0, _translate("MainWindow", "air"))
        self.comboBox_mode.setItemText(1, _translate("MainWindow", "rail"))
        self.comboBox_mode.setItemText(2, _translate("MainWindow", "road"))
        self.label.setText(_translate("MainWindow", "Greenhouse Gas Emission Calculator"))
        self.origin.setText(_translate("MainWindow", "Origin"))
        self.modeTrans.setText(_translate("MainWindow", "Mode of Transport"))
        self.emission.setText(_translate("MainWindow", "CO2 Emissions (g)"))
        self.destination.setText(_translate("MainWindow", "Destination"))
        self.pushButton.setText(_translate("MainWindow", "calculate"))
