import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from vista import Ui_MainWindow  

alfabeto = ['A','B','C','D','E','F','G','H','I','J','K',
            'L','M','N','Ñ','O','P','Q','R','S','T','U', 
            'V','W','X','Y','Z', 
            '-','0','1','2','3','4','5','6','7','8','9']
estados = []
tablaT = []

class MiAplicacion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.automata)

    def automata(self):
        texto = self.ui.lineEdit.text()
        matricula = list(texto)
        if len(matricula)==9:
            self.estadoCero(matricula)
        else:
            self.casoError()
            return self.ui.label_2.setText("El tamaño de la cadena no es el adecuado")
            
    def estadoCero(self, matricula):
        if(matricula[0]==alfabeto[5]):
            estados.append("--->q0")
            self.estadoUno(matricula)
        else:
            self.casoError()

    def estadoUno(self,matricula):
        if (matricula[1] in [alfabeto[i] for i in range(2, 10)]):
            estados.append("--->q1")
            self.estadoDos(matricula)
        else:
            self.casoError()
        
    def estadoDos(self,matricula):
        if(matricula[2]==alfabeto[27]):
            estados.append("--->q2")
            self.estadoTres(matricula)
        else:
            self.casoError()


    def estadoTres(self,matricula):
        if(matricula[3]==alfabeto[28]):
            estados.append("--->q3")
            self.estadoCuatro(matricula)
        elif (matricula[3] in [alfabeto[i] for i in range(29, 38)]):
            estados.append("--->q3")
            self.estadoDoce(matricula)
        else:
            self.casoError()

    def estadoCuatro(self,matricula):
        if(matricula[4]==alfabeto[28]):
            estados.append("--->q4")
            self.estadoCinco(matricula)       
        elif (matricula[4] in [alfabeto[i] for i in range(29, 38)]): 
            estados.append("--->q4")
            self.estadoDiez(matricula)
        else:
            self.casoError()
        
    def estadoCinco(self,matricula):
        if(matricula[5]==alfabeto[28]):
            estados.append("--->q5")
            self.estadoSeis(matricula)       
        elif (matricula[5] in [alfabeto[i] for i in range(29, 38)]): 
            estados.append("--->q5")
            self.estadoOnce(matricula)
        else:
            self.casoError()

    def estadoSeis(self,matricula):
        if(matricula[6] in [alfabeto[i] for i in range(29, 38)]): 
            estados.append("--->q6")
            self.estadoSiete(matricula)  
        else:
            self.casoError()
        
    def estadoSiete(self,matricula):
        if(matricula[7]==alfabeto[27]):
            estados.append("--->q7")
            self.estadoOcho(matricula)  
        else:
            self.casoError()
        
    def estadoOcho(self,matricula):
        if(matricula[8] in [alfabeto[i] for i in range(0, 27)]): 
            estados.append("--->q8")
            self.estadoNueve(matricula)  
        else:
            self.casoError()

    def estadoNueve(self, matricula):
        estados.append("--->q9")
        self.recorridoTransiciones(matricula)
        return self.ui.label_2.setText("La cadena esta permitida")

    def estadoDiez(self,matricula):
        if(matricula[5] in [alfabeto[i] for i in range(28, 38)]): 
            estados.append("--->q10")
            self.estadoOnce(matricula)  
        else:
            self.casoError()
    
    def estadoOnce(self,matricula):
        if(matricula[6] in [alfabeto[i] for i in range(28, 38)]): 
            estados.append("--->q11")
            self.estadoSiete(matricula) 
        else:
            self.casoError()

    def estadoDoce(self,matricula):
        if(matricula[4]==alfabeto[28]):
            estados.append("--->q12")
            self.estadoTrece(matricula)
        elif (matricula[4] in [alfabeto[i] for i in range(29, 38)]): 
            estados.append("--->q12")
            self.estadoDieciseis(matricula)
        else:
            self.casoError()

    def estadoTrece(self,matricula):
        if(matricula[5]==alfabeto[28]):
            estados.append("--->q13")
            self.estadoCatorce(matricula)
        elif (matricula[5] in [alfabeto[i] for i in range(29, 38)]): 
            estados.append("--->q13")
            self.estadoDiecinueve(matricula)
        else:
            self.casoError()

    def estadoCatorce(self,matricula):
        if(matricula[6]==alfabeto[28]):
            estados.append("--->q14")
            self.estadoQuince(matricula)
        elif (matricula[6] in [alfabeto[i] for i in range(29, 38)]): 
            estados.append("--->q14")
            self.estadoVeinte(matricula)
        else:
            self.casoError()

    def estadoQuince(self,matricula):
        if(matricula[7]==alfabeto[27]):
            estados.append("--->q15")
            self.estadoOcho(matricula)
        else:
            self.casoError()

    def estadoDieciseis(self,matricula):
        if(matricula[5]==alfabeto[28]):
            estados.append("--->q16")
            self.estadoDiecinueve(matricula)
        elif (matricula[5] in [alfabeto[i] for i in range(29, 38)]): 
            estados.append("--->q16")
            self.estadoDiecisiete(matricula)
        else:
            self.casoError()

    def estadoDiecisiete(self,matricula):
        if(matricula[6]==alfabeto[28]):
            estados.append("--->q17")
            self.estadoVeintiuno(matricula)
        elif (matricula[6] in [alfabeto[i] for i in range(29, 38)]): 
            estados.append("--->q17")
            self.estadoDieciocho(matricula)
        else:
            self.casoError()

    def estadoDieciocho(self,matricula):
        if(matricula[7]==alfabeto[27]):
            estados.append("--->q18")
            self.estadoOcho(matricula)
        else:
            self.casoError()

    def estadoDiecinueve(self,matricula):
        if(matricula[6]==alfabeto[28]):
            estados.append("--->q19")
            self.estadoVeinte(matricula)
        elif (matricula[6] in [alfabeto[i] for i in range(29, 38)]): 
            estados.append("--->q19")
            self.estadoVeintiuno(matricula)
        else:
            self.casoError()

    def estadoVeinte(self,matricula):
        if(matricula[7]==alfabeto[27]):
            estados.append("--->q20")
            self.estadoOcho(matricula)
        else:
            self.casoError()

    def estadoVeintiuno(self,matricula):
        if(matricula[7]==alfabeto[27]):
            estados.append("--->q21")
            self.estadoOcho(matricula)
        else:
            self.casoError(self)
        
    def recorridoTransiciones(self, matricula):
        transicionesR= ""

        recorrido = ''.join(estados)
        self.ui.label_6.setText(recorrido)

        for i in range(len(estados) - 1):
            sublista = [estados[i], matricula[i], estados[i + 1]]
            tablaT.append(sublista)

        sublista = [estados[-1], matricula[-1]]
        tablaT.append(sublista)
        tablaT.pop()

        for sublista in tablaT:
            transicionesR += str(sublista) + '\n'

        self.ui.textEdit.setPlainText(transicionesR)
        
        estados.clear()
        tablaT.clear()
        sublista.clear()

    def casoError(self):
        estados.clear()
        self.ui.label_6.setText("CASO NO VALIDO")
        self.ui.textEdit.setPlainText("CASO NO VALIDO")
        return self.ui.label_2.setText("Está matrícula no es correcta")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiAplicacion()
    ventana.show()
    sys.exit(app.exec_())