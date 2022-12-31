#  vim: set ts=4 sw=4 tw=0 et ft=python :
import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

app = QApplication([])

win = QWidget()
win.setWindowTitle('PyStand')

layout = QVBoxLayout()

label = QLabel('Hello, World !!')
label.setAlignment(Qt.AlignCenter)
layout.addWidget(label)

btn = QPushButton(text = 'PUSH ME')
layout.addWidget(btn)

win.setLayout(layout)
win.resize(400, 300)

btn.clicked.connect(lambda : [
        print('exit'),
        win.close(),
    ])

win.show()

app.exec_()

