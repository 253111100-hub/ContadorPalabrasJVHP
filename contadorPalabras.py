import sys
from PyQt5 import QtWidgets, uic

class contadotPalabras(QtWidgets.QMainWindow):
    def __int__(self):
        super().__int__()
        #carga de nuestra vista
        uic.loadUi("contadorPalabras.ui",self)
        self.btnContar.clicked.connect(self.contarPalabras)


    def contarPalabras(self):
        #recuperar el texto 
        texto = self.edtCaracteres.Text()

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
        

app = QtWidgets.QApplication(sys.argv)
ventana = contadotPalabras()
ventana.show()
sys.exit(app.exec())