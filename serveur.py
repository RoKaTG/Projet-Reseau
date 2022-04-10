import socket
import threading

Host = ''
Port = 8010

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(Host, Port)

serveur.listen()

clients = []
pseudonyme = []

