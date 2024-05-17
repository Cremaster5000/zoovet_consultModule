from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys


class Warning(QMainWindow):
    def __init__(self, parent, info:str):
        super().__init__()
        
        self.parent = parent
        self.createWindow(info)
        self.parent.setDisabled(True)
        self.show()
        
        
    def createWindow(self, info):
        self.setWindowTitle("Aviso")
        self.setBaseSize(300, 150)        
        self.central_widget = QWidget(self)
        self.central_widget.setGeometry(QRect(0,0, 300, 150))
        self.data = QLabel(self.central_widget)
        self.data.setText(info)
        self.adjustSize()
        self.butonOk = QPushButton("Ok", self.central_widget)
        self.grid_layout = QGridLayout(self.central_widget)
        self.grid_layout.addWidget(self.data, 0, 1, Qt.AlignmentFlag.AlignCenter)
        self.grid_layout.addWidget(self.butonOk, 1, 1, Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.central_widget)
        self.butonOk.clicked.connect(self.ok)
        
    def ok(self):
        self.parent.setEnabled(True)
        self.close()
  