import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class SelectUnit(QDialog, QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        
        self.btnselectmain = QPushButton('메인화면으로',self)
        self.btnselectmain.clicked.connect(self.tomain)

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.btnselectmain)

        hlayout = QHBoxLayout()
        hlayout.addLayout(vlayout)

        self.setLayout(hlayout)

        self.setWindowTitle("단어 연습장")
        self.move(300,300)
        self.resize(550,400)
        self.show()

    def tomain(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SelectUnit()
    sys.exit(app.exec_())