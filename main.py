import cv2
import numpy as num
import kivy as mobile
import pyt as pc
from  matplotlib import pyplot as plt
import numpy as np
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QLabel, QPushButton, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("My App")

        # QTabWidget nesnesi oluşturma
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # İlk sekme oluşturma
        self.tab1 = QWidget()
        self.tabs.addTab(self.tab1, "Resim")

        # Düğme oluşturma
        self.button = QPushButton("Resim Yükle", self.tab1)
        self.button.move(10, 10)
        self.button.clicked.connect(self.select_image)

        # Resim gösterme alanı
        self.label = QLabel(self.tab1)
        self.label.move(10, 50)

    def select_image(self):
        # Dosya seçme penceresi açma
        filename, _ = QFileDialog.getOpenFileName(self, "Resim Yükle", "", "Resim Dosyaları (*.png *.jpg *.bmp)")

        if filename:
            # Resim yükleme
            pixmap = QPixmap(filename)
            self.label.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
