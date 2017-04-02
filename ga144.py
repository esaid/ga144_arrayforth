#  Emmanuel SAID ,  lancer un programme depuis Python et
# simuler un clavier dans l application
# 16/10/2014
# shell.Activate : https://mail.python.org/pipermail/python-list/2011-April/600957.html
# sendkeys :  https://github.com/dzbios/pythonSendkeysLinuxAndWindows
import os
import time
import sendkeys
# from subprocess import Popen, PIPE

import win32com
import win32com.client
import win32gui



shell = win32com.client.Dispatch("WScript.Shell")
cheminarrayforth = "C:/GreenArrays/EVB001"
programme_arrayForth = "Okad.bat"
tlong = 2  # pause 5 s
t = 0.3  # pause 300ms


def ArrayForth():
    os.chdir(cheminarrayforth)
    print("\n Lancer ArrayForth ")
    print os.getcwd()
    shell.Run(programme_arrayForth)
    time.sleep(tlong)  # attente que l application soit lance
    print("Ok\n ")

def sendMesg(application, s):
    # ecrire le caractere s dans l application colorForth
    shell.AppActivate(application)
    time.sleep(t)  # pause
    sendkeys.sendkeys(s)
    time.sleep(t)  # pause

def beforeandsend(liste):  # decoupage lettre par lettre du message
    for item in liste:
        sendMesg("colorForth", item )

def CommandeArrayForth(chaine):
        beforeandsend(list(chaine))  # envoi du message au programme ColorForth

ArrayForth()  # lancer le programme ArrayForth

# h recupere le handle de la fenetre colorForth
h = win32gui.FindWindow( None,"colorForth")

# h : handle ,  x : int     y : int   width : int   height : int    bRepaint : int
win32gui.MoveWindow(h,0,0,750,650,True)

# cache la fenetre False
win32gui.ShowWindow(h , False)

# ecrire le message dans l application ArrayForth
#  envoi caractere par caractere
sendMesg("colorForth", "c ")
sendMesg(" colorForth", " " )
time.sleep(tlong)  # pause
#   envoi chaine
CommandeArrayForth("warm " )
time.sleep(tlong / 2)  # pause
# montre la fenetre True
win32gui.ShowWindow(h , True)

CommandeArrayForth("bye " )
