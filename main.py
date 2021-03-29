import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow
from Dialog import Ui_Dialog


app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


#logic...
def openDialog():
	Dialog = QtWidgets.QDialog()
	ui = Ui_Dialog()
	ui.setupUi(Dialog)
	MainWindow.close()
	Dialog.show()

ui.pushButton.clicked.connect(openDialog)

sys.exit(app.exec_())
