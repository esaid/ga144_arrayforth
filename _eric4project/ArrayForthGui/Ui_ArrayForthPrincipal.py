from PyQt4.QtGui import  *
from PyQt4.QtCore import  *
from PyQt4 import uic

from GA144_fonctions_py2 import *

import  sys
UiMaFenetre,  Klass = uic.loadUiType('ArrayForthWindow.ui') 
class MaFenetre(QMainWindow,  UiMaFenetre):
    def __init__(self,  conteneur=None):
        if conteneur is None : conteneur = self
        QMainWindow.__init__(conteneur)
        self.setupUi(conteneur)
        self.createConnexions()
        
    def createConnexions(self):
        
        self.connect(self.actionInfo,  SIGNAL("triggered()"),  self.info) 
        self.connect(self.commandLinkButton_ArrayForthRun, SIGNAL("clicked()"), ArrayForth)
        self.connect(self.commandLinkButton_EditRun, SIGNAL("clicked()"), Editeur)

        self.connect(self.pushButton_Save, SIGNAL("clicked()"), InitArrayForth)
        
        self.connect(self.commandLinkButton_cf_to_f, SIGNAL("clicked()"), ConversionCF_toForth)
        self.connect(self.commandLinkButton_f_to_cf, SIGNAL("clicked()"), ConversionForth_toCF)
        
        self.connect(self.pushButton_Maj, SIGNAL("clicked()"), MajArrayForth)
        self.connect(self.pushButton_Send, SIGNAL("clicked()"), Commande)
        
    """"
       self.connect(self.actionCalculer,  SIGNAL("triggered()"),  self.calcul)
        
    def calcul(self):
        n1 = self.spinBoxNombre1.value() 
        n2 = self.spinBoxNombre2.value()
        op = self.comboBoxOperation.currentText() 
        ch = str(n1)+str(op)+ str(n2)
        try : res = eval(ch)
        except ZeroDivisionError : res = "#div0"
        self.labelResultat.setText (str(res)) 
      
       """
    def info(self):
       QMessageBox.information(self,"info : "," GA144 ,  Auteur Emmanuel SAID "," version : "+version)
        
    
    
if __name__ == "__main__":
   
    a = QApplication(sys.argv)
    f = MaFenetre()
    f.show()
    r = a.exec_()
    
