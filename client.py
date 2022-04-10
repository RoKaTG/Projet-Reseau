import socket
import threading
import tkinter              #bibliothéque python d'interface graphique
import tkinter.scrolledtext
from tkinter import simpledialog

Host = '169.254.1.1' #127.0.0.1       #idem qu'en serveur
Port = 8010


#Nous avons besoin de cette fois ci une classe client qui contiendra le gui et les methodes de thread

class Client :
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)       #creation du socket
        self.sock.connect((host, port))                               #connexion via port + host

        alert = tkinter.Tk()    #fenetre
        alert.withdraw()

        self.pseudo = simpledialog.askstring("Username", "Ecrivez votre pseudonyme", parent=alert)       #Pop up pour l'entrée du pseudo
        self.interface = False    #interface du chat
        self.run = True

        thread = threading.Thread(targuet=self.loop_gui())
        reception_thread = threading.Thread(targuet=self.reception)

        thread.start()
        reception_thread.start()


#Methode d'interface

    def loop_gui(self) :
        self.windows = tkinter.Tk()
        self.windows.configure(bg="lightgray")

        self.chat = tkinter.Label(self.windows, text="Chat :", bg="lightgrey")
        self.chat.config(font=("Arial", 11))
        self.chat.pack(padx=20, pady=5)

        self.scroll = tkinter.scrolledtext.ScrolledText(self.windows)
        self.scroll.pack(padx=20, pady=5)
        self.scroll.config(state='disabled')

        self.message = tkinter.Label(self.windows, text="Message :", bg="red")
        self.message.config(font=("Arial", 11))
        self.message.pack(padx=20, pady=5)

        self.imput = tkinter.Text(self.windows, height=5)
        self.imput.pack(padx=20, pady=5)

        self.send_button = tkinter.Button(self.windows, text="Send", command=self.write)
        self.send_button.config(font=("Arial", 11))
        self.send_button.pack(padx=20, pady=5)

        self.interface = True

        self.windows.protocol("WM_DELETE_WINDOWS", self.stop)

        self.windows.mainloop()

        # Methode qui permet l'ecriture du msg

    def write(self):
        message = f"{self.pseudo}: {self.imput.get('1.0', 'end')}"
        self.sock.send(message.encode('utf-8'))
        self.imput.delete('1.0', 'end')

        # Methode qui permet d'arreter la fenetre de chat

    def stop(self):
        self.run = False
        self.windows.destroy()
        self.sock.close()
        exit(0)


    def reception(self) :
        while self.run:
            try:
                msg = self.sock.recv(1024).decode('utf-8')
                if msg == 'Username':
                    self.sock.send(self.pseudo.encode('utf-8'))
                else:
                    if self.interface:
                        self.scroll.config(state='normal')
                        self.scroll.insert('end', msg)
                        self.scroll.yview('end')
                        self.scroll.config(state='disabled')
            except ConnectionAbortedError:
                break
            except:
                print('Erreur, fermeture du client')
                self.sock.close()
                break

client = Client(Host, Port)

