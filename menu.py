import cv2
import numpy as num
import kivy as mobile
import pyt as pc
from  matplotlib import pyplot as plt
import numpy as np
import sys
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QLabel, QPushButton, QFileDialog

def upload(win):
    label = QtWidgets.QLabel(win)
    filename, _ = QFileDialog.getOpenFileName(label, "Resim Yükle", "", "Resim Dosyaları (*.png *.jpg *.bmp)")

def button(win):
    background = QtWidgets.QLabel(win)
    pixmap = QtGui.QPixmap("ahaha.jpg")
    background.setPixmap(pixmap)
    background.setScaledContents(True)
    label1 = QtWidgets.QPushButton(win)
    label1.move(10, 10)
    label1.setText("Resim Yükle")
    res = label1.clicked.connect(lambda: upload(win))
def Window():
    app = QApplication(sys.argv)
    win =QtWidgets.QWidget()
    win.setWindowTitle("Photoroot")
    win.setGeometry(30,90,920,720)
    win.setFixedSize(920,720)
    button(win)
    win.show()
    sys.exit(app.exec())

Window()