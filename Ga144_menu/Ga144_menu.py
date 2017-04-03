# programme adapte pour Windows OS
# notepad++  lancer un terminal Run : cmd en mode administrateur
# configurer notepad++ pour pouvoir etre appelle de n'importe quel repertoire
# set path=%path%;c:\Program Files (x86)\Notepad++
#
import time
import sendkeys
import win32com.client
import win32gui
from cf2fHack import *
#from subprocess import Popen, PIPE
shell = win32com.client.Dispatch("WScript.Shell")
cheminarrayforth = "C:/GreenArrays/EVB001"
programme_arrayforth = "Okad.bat"
programmeEditeur = "notepad++.exe okadback.f"
arrayforth = "colorForth"   #  nom de la fenetre active du prg ArrayForth
t = 0.5   # 500ms
# -------------------------------------------------------------------
# ---------------------- fonctions ----------------------------------
# -------------------------------------------------------------------

def sendMesg(application , s):  # envoie le caractere s dans l application
        shell.AppActivate(application)
        time.sleep(t)
        sendkeys.sendkeys(s)

def beforeandsend(liste): # decoupage lettre par lettre + pause 
        for item in liste:
                sendMesg(arrayforth , item)
                time.sleep(t)

def idColorForth():
        h = win32gui.FindWindow(None, arrayforth)  # recupere le handle de la fenetre arrayforth

        return h

def activeColorForth(h):
        win32gui.ShowWindow(h,True)


def ArrayForth():
        os.chdir(cheminarrayforth)
        print("\n Lancer ArrayForth")
        print os.getcwd()
        shell.Run(programme_arrayforth)
        time.sleep(4)

        print("Ok\n")

def Editeur():

        print("\n Lancer editeur Notepad++ ")
        shell.Run(programmeEditeur)
        time.sleep(2)
        print("Ok\n")
        
def Bye():
        chaine = " bye "  # bye
        CommandeArrayForth(chaine)
        print("\n bye")
        quit()
def CommandeArrayForth(chaine):
        
        id = idColorForth() # recuperation id de ColorForth
        if id == 0:
                print("\n ArrayForth introuvable...")
        else:
                # print("\n La fenetre colorForth a %s "  %id ," suivant ")
                activeColorForth(id)  # rend actif la fenetre ColorForth
                beforeandsend(list(chaine)) # envoi du message au programme ColorForth
                 
def InitArrayForth():
        print("\n Initialisation ArrayForth")
        chaine = " warm compile 0 !back " # 0 !back sauvegarde 1440 blocs
        CommandeArrayForth(chaine)
        print ("\n  Sauvegarde okadback.cf: " )

def MajArrayForth():
        chaine = " warm 0 @back " # 0 @back recharge  1440 blocs
        CommandeArrayForth(chaine)
        print ("\n  mise a jour okadback.cf " )
        
def Commande():
        chaine = raw_input("\n Commande a envoyer :")
        CommandeArrayForth(chaine)
        
                
def ConversionCF_toForth():
        print("\n Conversion ColorForth vers Forth")
        cf2f("okadback.cf","okadback.f")
        print("\n fin conversion")

def ConversionForth_toCF():
        print("\n Conversion  Forth vers ColorForth")
        f2cf("okadback.f","okadback.cf")
        print("\n fin conversion")

def erreur():
        print("\n erreur saisie menu")
        print ("\n" * 100)
        
# -------------------------------------------------------------------
# ----------------------- Menu --------------------------------------
# -------------------------------------------------------------------
def menu():
        print ("-------------------------------------------------------------")
        print ("|                     ArrayForth GA144                      |")
        print ("|                                                           |")
        print ("|  1) Lancer ArrayForth                                     |")
        print ("|  2) Lancer editeur Notepad++                              |")
        print ("|  3) okadback.cf ---> okadback.f  vers editeur Notepad++   |")
        print ("|  4) okadback.f  ---> okadback.cf vers ArrayForth          |")
        print ("|  5) mise a jour donnees  ArrayForth                       |")
        print ("|  6) Commande a envoyer                                    |")
        print ("|  8) Initialiser ArrayForth (sauvegarde okadback.cf)       |")
        print ("|  9) Quitter                                               |")
        print ("-------------------------------------------------------------")
        choix = raw_input("    commande : ")
        option = { '1' :  ArrayForth ,
                   '2' :  Editeur ,
                   '3' :  ConversionCF_toForth ,
                   '4' :  ConversionForth_toCF ,
                   '5' :  MajArrayForth ,
                   '6' :  Commande ,
                   '8' :  InitArrayForth ,
                   '9' :  Bye
                }
        option.get(choix , erreur)()
while True:

        menu()


        

