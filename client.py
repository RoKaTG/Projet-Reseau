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

        thread = threading.Thread(targuet=self.interface)
        reception_thread = threading.Thread(targuet=self.reception)

        thread.start()
        reception_thread.start()


#Methode qui permet l'ecriture du msg

    def write(self):
        message = f"{self.pseudo}: {self.imput.get('1.0','end')}"
        self.sock.send(message.encode('utf-8'))
        self.imput.delete('1.0', 'end')


#Methode qui permet d'arreter la fenetre de chat

    def stop(self):
        self.run = False
        self.windows.destroy()
        self.sock.close()
        exit(0)


#Methode d'interface

    def interface(self) :
        self.windows = tkinter.Tk()

        self.chat = tkinter.Label(self.win, text="Chat :")
        self.chat.config(font=("Helvetica", 11))

        self.scroll = tkinter.scrolledtext.ScrolledText(self.windows)
        self.scroll.pack(padx=30, pady=5)
        self.scroll.config(state='disabled')

        self.message = tkinter.Label(self.win, text="Message :")
        self.message.config(font=("Helvetica", 11))

        self.imput = tkinter.Text(self.windows, height=5)
        self.imput.pack(padx=30, pady=5)

        self.envoyer = tkinter.Button(self.windows, text="Envoyer", command=self.write)
        self.envoyer.config(font=("Arial", 11))
        self.imput.pack(padx=30, pady=5)

        self.interface = True

        self.windows.protocol("WM_DELETE_WINDOWS", self.stop)
        self.windows.mainloop()


    def reception(self) :
        pass

