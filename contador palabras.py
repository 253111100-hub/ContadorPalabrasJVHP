import sys
from PyQt5 import QtWidgets, uic

class contadotPalabras(QtWidgets.QMainWindow):
    def __int__(self):
        super().__int__()
        #carga de nuestra vista
        uic.loadUi("contadorPalabras.ui",self)

app = QtWidgets.QApplication(sys.argv)
ventana = contadotPalabras()
ventana.ahow()
sys.exit(app.exec())