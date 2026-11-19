import sys
from PyQt5 import QtWidgets, uic

class contadorPalabras(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        #carga de nuestra vista
        uic.loadUi("contadorPalabras.ui",self)
        self.btnContar.clicked.connect(self.contarPalabras)


    def contarPalabras(self):
        #recuperar el texto 
        texto = self.edtCaracteres.text()

        #separar las palabras
        textoSeparado = texto.split()
        print(textoSeparado)
        #contar las palabras
        cantidadPalabras = len(textoSeparado)
        self.tvPalabras.setText(f"Plabras: {cantidadPalabras}")
        
        totalCaracteres = 0
        for palabra in textoSeparado:
            totalCaracteres += len(palabra)
        self.tvCaracteres.setText(f"Caracteres: {totalCaracteres}")
        #cambiar color rojo
        if cantidadPalabras >= 20:
            self.tvPalabras.setStyleSheet("color: red;")
        else:
            self.tvPalabras.setStyleSheet("color: black;")

        if totalCaracteres >= 120:
            self.tvCaracteres.setStyleSheet("color: #ff756b")
        else:
            self.tvCaracteres.setStyleSheet("color: #000000")

app = QtWidgets.QApplication(sys.argv)
ventana = contadorPalabras()
ventana.show()
sys.exit(app.exec())