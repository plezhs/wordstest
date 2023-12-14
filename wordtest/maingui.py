import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from unitselect import SelectUnit

class Main(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
                                                                                
        # self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint) 

        self.btnexit = QPushButton('종료',self)                                 # 종료 버튼
        self.btnexit.clicked.connect(QCoreApplication.instance().quit)          #종료시키기

        self.btnstart = QPushButton('시작',self)
        self.btnstart.clicked.connect(self.selectwindow)

        self.btnedit = QPushButton('수정',self)

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.btnstart)
        vlayout.addWidget(self.btnexit)

        hlayout = QHBoxLayout()
        hlayout.addStretch(1)
        hlayout.addLayout(vlayout)
        hlayout.addStretch(3)

        self.setLayout(hlayout)

        self.setWindowTitle("단어 연습장")
        self.move(300,300)
        self.resize(550,400)
        self.show()

    def selectwindow(self):
        y = self.geometry()
        self.hide()
        self.second = SelectUnit()
        self.second.setGeometry(y)
        self.second.exec()
        x = self.second.geometry()
        self.setGeometry(x)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())