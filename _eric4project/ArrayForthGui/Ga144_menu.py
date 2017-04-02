import time
import os
import sys
from cf2fHack import *
from subprocess import Popen, PIPE
programmeArrayForth = './Okad2-42c-pd.exe'
programmeEditeur = ['gedit' , 'okadback.f'] 


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
        print("\n Lancer ArrayForth")
        # print os.getcwd()
        Popen(programmeArrayForth)
        time.sleep(4)
        print("Ok\n")

def Editeur():
        print("\n Lancer editeur Gedit")        
        Popen(programmeEditeur)
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
        
# -------------------------------------------------------------------
# ----------------------- Menu --------------------------------------
# -------------------------------------------------------------------
def menu():
        print ("-------------------------------------------------------------")
        print ("|                     ArrayForth GA144                      |")
        print ("|                                                           |")
        print ("|  1) Lancer ArrayForth                                     |")
        print ("|  2) Lancer editeur Gedit                                  |")
        print ("|  3) okadback.cf ---> okadback.f  editeur Gedit            |")
        print ("|  4) okadback.f  ---> okadback.cf ArrayForth               |")
        print ("|  5) mise a jour donnees editeur ArrayForth                |")
        print ("|  6) Commande a envoyer                                    |")
        print ("|  8) Initialiser ArrayForth (sauvegarde okadback.cf)       |")
        print ("|  9) Quitter                                               |")
        print ("-------------------------------------------------------------")
        choix = raw_input("\n    commande : ")
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


        

