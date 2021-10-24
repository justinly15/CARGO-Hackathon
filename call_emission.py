#导入程序运行必须模块
import sys
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from emission import Ui_Dialog

class MyMainForm(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    #PyQt5 app needs QApplication object. sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #intialize
    myWin = MyMainForm()
    #show widgets on screen
    myWin.show()
    #run app, sys.exit method makes sure the app exeit completely
    sys.exit(app.exec_())
