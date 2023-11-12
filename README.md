# Description de l'application

Cette application interroge le service PunAPI pour afficher un jeu de mots.

## Comment installer

1. Clonez ce dépôt: `git clone https://github.com/VOTRE_UTILISATEUR/ue19_labo09-10.git`
2. Accédez au répertoire: `cd ue19_labo09-10`
3. Installez les dépendances: `pip install -r requirements.txt`

## Comment lancer

Utilisez la commande suivante: `python app.py`

## Docker

Pour utiliser Docker, assurez-vous de l'avoir installé, puis exécutez les commandes suivantes:

1. Construire l'image: `docker build -t punapi-app .`
2. Lancer le conteneur: `docker run punapi-app`
