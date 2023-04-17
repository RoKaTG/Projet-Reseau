# Projet-Reseau
Ce projet est une application Python qui permet de créer un chat interactif sur un réseau ad-hoc à l'aide de Raspberry Pi. L'application a été développée avec l'IDE JetBrains PyCharm.

## Prérequis
Avant de pouvoir exécuter l'application, vous aurez besoin des éléments suivants :

-Un IDE Python comme PyCharm ou Python installé sur votre machine

-Des Raspberry Pi connectés à un réseau ad-hoc

-Les adresses IP des Raspberry Pi

-Un port disponible sur votre ordinateur ou votre réseau

## Installation et exécution
Téléchargez le projet à partir de GitHub.

Ouvrez le projet dans l'IDE Python de votre choix.

Ouvrez les fichiers client.py et server.py dans l'éditeur de texte.

Dans chaque fichier, modifiez la valeur de HOST pour correspondre à l'adresse IP de votre Raspberry Pi.

Par exemple, si l'adresse IP de votre Raspberry Pi est 192.168.1.100, vous devez définir HOST comme suit :

```python
HOST = '192.168.1.100'```

Définissez également un numéro de port disponible sur votre ordinateur ou votre réseau.

Par exemple, si vous souhaitez utiliser le port 5000, vous devez définir PORT comme suit :



PORT = 5000
Enregistrez les fichiers modifiés.

Ouvrez un terminal et exécutez le fichier server.py sur votre Raspberry Pi à l'aide de la commande suivante :

bash
Copy code
python server.py
Dans un autre terminal, exécutez le fichier client.py sur votre ordinateur à l'aide de la commande suivante :

bash
Copy code
python client.py
Vous pouvez désormais utiliser le chat interactif en tapant des messages dans le terminal du client.

Conclusion
C'est tout ! Vous pouvez maintenant utiliser cette application pour discuter avec d'autres personnes sur votre réseau ad-hoc. N'hésitez pas à explorer le code source et à l'améliorer si vous le souhaitez.
