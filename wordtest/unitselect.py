import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

def resource_path(path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,path)

unitlist = []

class SelectUnit(QDialog, QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        imsi = os.listdir(resource_path('.\\unit'))
        for i in imsi:
            unitlist.append(i.split('.json'))

    def initUI(self):
        
        self.unitlistbox = QComboBox(self)
        self.unitlistbox.addItems(unitlist)

        self.btnmain = QPushButton('메인화면으로',self)
        self.btnmain.clicked.connect(self.tomain)

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.unitlistbox)
        vlayout.addWidget(self.btnmain)

        hlayout = QHBoxLayout()
        hlayout.addStretch(1)
        hlayout.addLayout(vlayout)
        hlayout.addStretch(1)

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