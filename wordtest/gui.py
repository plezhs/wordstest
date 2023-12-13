import typing
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

class Main(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        edit = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(edit)

        self.setLayout(layout)
app = QApplication([])
dialog = Main()
dialog.show()
app.exec_()