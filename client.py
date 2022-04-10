import socket
import threading
import tkinter              #bibliothéque python d'interface graphique
import tkinter.scrolledtext
from tkinter import simpledialog

Host = ''       #idem qu'en serveur
Port = 8010

#Nous avons besoin de cette fois ci une classe client qui contiendra le gui et les methodes de thread
class Client :
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)       #creation du socket
        self.sock.connect(host, port)                                #connexion via port + host

        alert = tkinter.Tk()    #fenetre
        alert.withdraw()

        self.pseudo = simpledialog.askstring("Username", "Ecrivez votre pseudonyme", parent=alert)       #Pop up pour l'entrée du pseudo
        self.interface = False    #interface du chat
        self.run = True

        thread = threading.Thread(targuet=self.loop)
        reception_thread = threading.Thread(targuet=self.reception)

        thread.start()
        reception_thread.start()

    def loop(self) :
        pass

    def reception(self) :
        pass

