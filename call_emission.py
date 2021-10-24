import sys
# PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QDialog
# 导入designer工具生成的login模块
from emission import Ui_Dialog
from get_distance import calculate_distance
from get_emissions import calculate_emissions


class MyMainForm(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        # 添加登录按钮信号和槽。注意display函数不加小括号()
        self.buttonBox.clicked.connect(self.display)
        # 添加退出按钮信号和槽。调用close函数
        #self.cancel_Button.clicked.connect(self.close)

    def display(self):
        # use text Edit.text()to get input"":::::::::::::::"
        origin_text = self.textEdit_origin.text()
        dest_text = self.textEdit_dest.text()
        mass_text = self.textEdit_mass.text()
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