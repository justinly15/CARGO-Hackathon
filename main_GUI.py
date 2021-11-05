import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from emission import Ui_MainWindow # import the GUI construction .py file
from get_distance import calculate_distance
from get_emissions import calculate_emissions


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        # add signal slot
        self.pushButton.clicked.connect(self.display)
        # self.buttonBox.clicked.connect(self.close)

    def display(self):
   
        # read text from textEdit widgets
        origin_text = self.textEdit_origin.toPlainText()
        dest_text = self.textEdit_dest.toPlainText()
        mass_text = self.textEdit_mass.toPlainText()
        mode_text = self.comboBox_mode.currentText()
        
        # calculate emission based on inputs
        dist = calculate_distance(origin_text, dest_text)
        emission_text = calculate_emissions(dist, mode_text, mass_text)
        
        # display text using textBrowser widget's object setText()
        self.textBrowser_emission.setText(emission_text)

if __name__ == "__main__":
    # PyQt5 app needs QApplication object. sys.argv is command line parameters list, to ensure that the program can be run by double-clicking
    app = QApplication(sys.argv)
    # intialize
    myWin = MyMainForm()
    # show widgets on screen
    myWin.show()
    # run app, sys.exit method makes sure the app exeit completely
    sys.exit(app.exec_())
