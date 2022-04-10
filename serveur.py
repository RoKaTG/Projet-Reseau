import socket
import threading

Host = '169.254.1.1'  #127.0.0.1           #Ip du serveur
Port = 8010         #Port à utilisé dependant des ports dispo

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #Création du serveur avec les sockets
serveur.bind((Host, Port))                                #On bind l'ip et le port au serveur pour les connexion

serveur.listen()

liste_clients = []       #Nbr de client et les usernames
pseudonyme = []


#Methode qui gére les diffusions de signaux

def diffusion(message) :
    for client in liste_clients :
        client.send(message)      #envoi du signal qui est le msg


#Methode qui sert d'handler pour les signaux

def tri(client) :
    while True:
        try:
            message = client.recv(1024)   #Envoi du message si aucune erreur
            diffusion(message)
        except:
            index = liste_clients.index(client)     #Sinon ferme l'instance et deco le client
            liste_clients.remove(client)
            client.close()
            user = pseudonyme[index]
            pseudonyme.remove(user)
            break

#Methode qui gére la reception des threads et signaux

def reception() :
    while True:
        client, address = serveur.accept()           #Pour accepter les differentes connexion de client
        print(f"Connexion depuis {str(address)}")

        client.send("Username".encode('utf-8'))       #Gére la création d'un username
        user = client.recv(1024)

        pseudonyme.append(user)
        liste_clients.append(client)

        print(f"Votre pseudonyme est {user}")

        diffusion(f"{user} s'est connecté au salon\n".encode('utf-8'))
        client.send("Vous vous êtes connecté au salon !".encode('utf-8'))

        thread = threading.Thread(target=tri, args=(client,))
        thread.start()

print("Server running...")
reception()
