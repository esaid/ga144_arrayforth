# -----------------------------------------------------------------------------
# GA144_fonctions pour Windows
# date :  Octobre 2012 version 1.0
# Auteur : Emmanuel SAID
# Utilisation  et modification des modules cf2f et cword de john.comeau
# -----------------------------------------------------------------------------
from cf2fHack import *
from subprocess import Popen, PIPE
import time

version = '1.0'
cheminarrayforth = 'C:/Program Files/GreenArrays/EVB001'
chemin_editeur = 'C:/Program Files/Notepad++'
programme_arrayForth = 'Okad.bat'
programme_editeur = ['notepad++.exe', cheminarrayforth + '/okadback.f'] 


# -------------------------------------------------------------------
# ---------------------- fonctions ----------------------------------
# -------------------------------------------------------------------

def send(commande):  # envoie les commandes pour programme xdotool
        p= Popen(commande, stdout=PIPE) 
        return p.communicate()
        
def beforeandsend(liste): # decoupage lettre par lettre + pause 
        for item in liste:
                send (["xdotool", "type", item ])
                time.sleep(0.5)

def idColorForth():
        test1 = ["xdotool", "search", "--title", "colorForth"]
        id = send(test1)[0].strip() # on recupere id fenetre colorforth
        
        return id

def activeColorForth(id):
        
        chaine = ["xdotool", "windowactivate", id]
        send(chaine)
        time.sleep(2)


def ArrayForth():
        os.chdir(cheminarrayforth)
        print("\n Lancer ArrayForth")
        # print os.getcwd()
        
        Popen(programme_arrayForth)
        time.sleep(4)
        print("Ok\n")

def Editeur():
        print("\n Lancer editeur Gedit")
        os.chdir(chemin_editeur)
        Popen(programme_editeur)
        time.sleep(2)
        print("Ok\n")
        
def Bye():
        print("\n bye") 
        quit() 
def CommandeArrayForth(chaine):
        
        id = idColorForth() # recuperation id de ColorForth
        if id == "" :
                print("\n ArrayForth introuvable...")
        else :
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
        

