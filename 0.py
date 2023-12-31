import sys

from photo_open import PhotoGallery
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QLabel, QPushButton, QGridLayout, QWidget, \
    QScrollArea, QApplication
from PyQt5.QtGui import QPixmap


class GalleryAlbum(QMainWindow):
    def __init__(self, name_album):
        super().__init__()
        self.name_album = name_album
        self.layout = QGridLayout()
        self.add_button = QPushButton(f"Добавить в {self.name_album}", self)
        self.add_button.resize(915, 35)
        self.add_button.move(0, 30)
        self.add_button.clicked.connect(self.add_photo)
        self.scroll_area = QScrollArea(self)
        self.scroll_area.resize(915, 900)
        self.scroll_area.move(0, 100)
        self.setFixedSize(915, 1050)
        self.move(0, 0)
        self.row = 0
        self.col = 0

    def add_photo(self):
        photo_info = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')
        photo_path = photo_info[0]
        photo_expansion = photo_path.split('/')[-1].split('.')[-1]
        if photo_expansion == 'jpeg' or \
                photo_expansion == 'png' or \
                photo_expansion == 'jpg' or \
                photo_expansion == 'gif':
            pixmap = QPixmap(photo_path).scaled(220, 200)
            image = QLabel()
            image.resize(220, 210)
            image.setPixmap(pixmap)
            self.btn = QPushButton("Просмотр")
            self.btn.id = photo_path
            self.btn.setFixedSize(220, 30)
            self.btn.clicked.connect(self.this_photo)
            self.layout.addWidget(image, self.row, self.col % 4)
            self.layout.addWidget(self.btn, self.row + 1, self.col % 4)
            self.widget = QWidget()
            self.widget.setLayout(self.layout)
            self.scroll_area.setWidget(self.widget)
            self.col += 1
            if self.col % 4 == 0:
                self.row += 2

    def this_photo(self):
        self.window_this_photo = PhotoGallery(self.btn.sender().id)
        self.window_this_photo.show()


app = QApplication(sys.argv)
ex = GalleryAlbum('uiohwedf')
ex.show()
sys.exit(app.exec_())
