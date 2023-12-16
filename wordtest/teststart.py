import sys
import json
import random
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import unitselect

def resource_path(path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,path)

class MakeUnit(QDialog, QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        
        selectClass = unitselect.SelectUnit()

        selectedunit = selectClass.start()

        self.answersheet = []

        with open(resource_path(f'unit\\{selectedunit}.json'),'r',encoding='UTF-8') as jsondict:
            self.answersheet = json.load(jsondict)

        self.words = list(self.answersheet.keys())
        random.shuffle(self.words)

        self.correct = 0
        self.wordnumber = 0
        self.wordmaxnumber = len(self.words)
        
        self.word = QLabel(f'{self.words[self.wordnumber]}',self)
        self.word.setAlignment(Qt.AlignCenter)

        self.inputline = QLineEdit(self)
        self.inputline.returnPressed.connect(self.next)

        self.btnmakemain = QPushButton('뒤로',self)
        self.btnmakemain.clicked.connect(self.tomain)
        self.btnmakemain.setAutoDefault(False)
        self.btnmakemain.setDefault(False)

        alayout = QHBoxLayout()

        vlayout = QVBoxLayout()
        vlayout.addStretch(1)
        vlayout.addWidget(self.word)
        vlayout.addWidget(self.inputline)
        vlayout.addWidget(self.btnmakemain)
        vlayout.addStretch(1)

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
    
    def start(self):
        self.word.setText(self.answersheet[self.wordnumber])

    def next(self):
        if self.wordnumber < self.wordmaxnumber:
            if self.answersheet[self.words[self.wordnumber]] == self.inputline.text():
                self.correct += 1
            self.word.setText(f'{self.words[self.wordnumber]}')
            self.wordnumber+=1
        else:
            self.word.setText(f'{self.correct} / {self.wordmaxnumber}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MakeUnit()
    sys.exit(app.exec_())