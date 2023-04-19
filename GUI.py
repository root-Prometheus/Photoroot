import cv2
import numpy as num
import kivy as mobile
import pyt as pc
from  matplotlib import pyplot as plt
import numpy as np
import sys
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QLabel, QPushButton, QFileDialog
def clicked():
    print("Click")

def status(win):
    label1 = QtWidgets.QLabel(win)
    pixmap = QtGui.QPixmap("el.jpg")
    label1.setPixmap(pixmap.scaled(600, 600))  # Görüntü boyutu QLabel boyutlarına uyacak şekilde ölçeklenir.
    label1.move(200, 100)
    label1.setScaledContents(True)
    return label1
def delete(label):
    label.setPixmap(QtGui.QPixmap())

def upload(label):
    filename, _ = QFileDialog.getOpenFileName(label, "Resim Yükle", "", "Resim Dosyaları (*.png *.jpg *.bmp)")
    pixmap = QtGui.QPixmap(filename)
    label.setPixmap(pixmap.scaled(600, 600))  # Görüntü boyutu QLabel boyutlarına uyacak şekilde ölçeklenir.
    label.move(200, 100)
    label.setScaledContents(True)

def save(win):
        label = status(win)
        # Dosya kaydetme penceresi açma
        filename, _ = QFileDialog.getSaveFileName(label, "Resmi Kaydet", "",
                                                  "PNG Dosyası (*.png);;JPEG Dosyası (*.jpg);;BMP Dosyası (*.bmp)")

        if filename:
            # Resmi kaydetme
            label.pixmap.save(filename)


def button(win):
    background = QtWidgets.QLabel(win)
    pixmap = QtGui.QPixmap("ahaha.jpg")
    background.setPixmap(pixmap)
    background.setScaledContents(True)
    img = status(win)
    label1 = QtWidgets.QPushButton(win)
    label1.move(10,10)
    label1.setText("Resim Yükle")
    label1.clicked.connect(lambda: upload(img))
    #----------------------------------------#
    label2 = QtWidgets.QPushButton(win)
    label2.move(110, 10)
    label2.setText("Resimi Düzenle")
    #----------------------------------------#
    label3 = QtWidgets.QPushButton(win)
    label3.move(210, 10)
    label3.setText("Resim Sil")
    label3.clicked.connect(lambda: delete(img))
    #-----------------------------------------#
    label4 = QtWidgets.QPushButton(win)
    label4.move(310, 10)
    label4.setText("Resimi indir")
    label4.clicked.connect(lambda: save(win))

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