import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MakeUnit(QDialog, QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        
        self.btnmakemain = QPushButton('메인화면으로',self)
        self.btnmakemain.clicked.connect(self.tomain)

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.btnmakemain)

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
    ex = MakeUnit()
    sys.exit(app.exec_())