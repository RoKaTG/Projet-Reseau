import socket
import threading

Host = ''           #Ip du serveur
Port = 8010         #Port à utilisé dependant des ports dispo

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #Création du serveur avec les sockets
serveur.bind(Host, Port)                                #On bind l'ip et le port au serveur pour les connexion

serveur.listen()

liste_clients = []       #Nbr de client et les usernames
pseudonyme = []


#Methode qui gére les diffusions de signaux

def diffusion(message) :
    for client in liste_clients :
        client.send(message)      #envoi du signal qui est le msg


