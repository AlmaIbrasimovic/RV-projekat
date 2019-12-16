import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QPushButton, QFileDialog, QLabel, QHBoxLayout
from PyQt5.QtCore import pyqtSlot, QObject, Qt
from PyQt5.QtGui import QIcon, QPixmap, QPalette

class App(QWidget):
	def __init__(self): #Konstruktor
		super().__init__()
		
		self.initUI()

	def initUI(self):
		self.setWindowTitle('Ucitavanje slika')
		self.setFixedSize(1000,1000)
		# Postavke za button A
		button_A = QPushButton('Ucitaj sliku kartice',self)
		button_A.setToolTip('Dugme za ucitavanje slike kreditne kartice!')
		button_A.move(10,10)
		button_A.setFixedSize(190,50)
		button_A.clicked.connect(self.ucitajSliku) # Povezivanje klika sa funkcijom

		# Postavke za button B
		button_B = QPushButton('Ucitaj sliku reference/treninga',self)
		button_B.setToolTip('Dugme za ucitavanje slike za reference za prepoznavanje brojeva!')
		button_B.move(10,100)
		button_B.setFixedSize(190,50)
		button_B.clicked.connect(self.ucitajReferencu)
		self.center() 
		self.show()

	@pyqtSlot() # Funkcija za ucitavanje slike
	def ucitajSliku(self):
		self.kreirajDijalog()
		print('Slika')
		
	@pyqtSlot()
	def ucitajReferencu(self):
		self.kreirajDijalog()
		print('Refernca')

	def center(self): # Da bi pozicionirali ne sredinu ekrana
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	
	def kreirajDijalog(self):
		options = QFileDialog.Options()
		hbox = QHBoxLayout(self)
		files = QFileDialog.getOpenFileName(self, "Ucitaj sliku", "", "JPG (*.jpg);;PNG (*.png)")
		pixmap = QPixmap(files[0])
		lbl = QLabel(self)
		lbl.setPixmap(pixmap)  
		hbox.addWidget(lbl)
		#self.setLayout(hbox)
		self.show()

 
if __name__ == '__main__':
	app = QApplication(sys.argv)
	program = App()
	app.setStyle("Fusion")
	sys.exit(app.exec_())