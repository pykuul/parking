# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 13:42:13 2018

@author: Tuan Nguyen - quangtuan1412@gmail.com
"""
import os
import sys
from time import strftime
from PyQt5.QtWidgets import QMainWindow, QApplication, QLCDNumber
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon

class ClassMain(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.dong_ho = QLCDNumber(self)
        self.dong_ho.setNumDigits(8)
        self.dong_ho.setGeometry(10,10,280,80)
        
        dem_gio = QTimer(self)
        dem_gio.timeout.connect(self.hien_gio)
        dem_gio.start(1000)
        
        self.setWindowTitle('Vsmart CARPARKING SYSTEM V.1.01')
        self.setWindowIcon(QIcon('clock.png'))
        self.resize(300,100) #setFixedSize(300,100)
        self.show()
    
    def hien_gio(self):
        self.dong_ho.display(strftime("%H" + ":" + "%M" + ":" + "%S"))
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ClassMain()
    sys.exit(app.exec_())