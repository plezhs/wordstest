import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from teststart import MakeUnit

def resource_path(path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,path)

class SelectUnit(QDialog, QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.unitlist = self.getlist()
        
        self.unitlistbox = QComboBox(self)
        self.unitlistbox.addItems(self.unitlist)

        self.startbtn = QPushButton('시작',self)
        self.startbtn.clicked.connect(self.totestwindow)

        self.btnmain = QPushButton('메인화면으로',self)
        self.btnmain.clicked.connect(self.tomain)

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.unitlistbox)
        vlayout.addWidget(self.startbtn)
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
    
    def totestwindow(self):
        y = self.geometry()
        self.hide()
        self.fourth = MakeUnit()
        self.fourth.setGeometry(y)
        self.fourth.exec()
        x = self.fourth.geometry()
        self.setGeometry(x)
        self.show()

    def start(self):
        a = self.unitlistbox.currentText()
        return a

    def getlist(self):
        a= []
        listf = os.listdir(resource_path('.\\unit'))
        for j in listf:
            i = j.split('.json')[0]
            a.append(i)
        return a


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SelectUnit()
    sys.exit(app.exec_())