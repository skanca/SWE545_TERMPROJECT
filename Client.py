import threading
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import string
#user interface
class ClientDialog(QDialog):
    def __init__(self):
        self.qt_app = QApplication(sys.argv)
        QDialog.__init__(self, None)
        self.setWindowTitle("TIC-TAC-TOE Client")
        self.setMinimumSize(500, 200)
        self.resize(640, 480)

    def run(self):
        self.show()
        self.qt_app.exec_()

app = ClientDialog()
app.run()
