'''
'''

import sys
from pathlib import Path

from PIL import Image, ImageOps

from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (
	QApplication,
	QLabel,
	QMainWindow,
	QStatusBar,
	QToolBar,
	QGraphicsView,
	QFileDialog,
	QGraphicsScene,
	QGraphicsPixmapItem
	)

from layout_objects import Window, ImageWindow 


class GlitKit(ImageWindow):
	def __init__(self):
		super().__init__(windowTitle="GMONEY")

		qimage_glit = self._load_glit()
		pixmap_glit = QPixmap.fromImage(qimage_glit)
		self._reload_canvas(pixmap_glit)
	
	def _init_ui(self):
		self.graphicsView = QGraphicsView()
		self.setCentralWidget(self.graphicsView)
		self._createStatusBar(message="meow")

	def _load_glit(self):
		pil_glit = Image.open("./glit.png")
		pil_glit = pil_glit.convert("L")

		glit_data = pil_glit.tobytes("raw", "L")
		return QImage(
            glit_data,
            pil_glit.width,
            pil_glit.height,
            pil_glit.width,
            QImage.Format.Format_Grayscale8
        )


if __name__ == "__main__":

	app = QApplication([])

	window = GlitKit() 
	
	window.show()
	sys.exit(app.exec())

