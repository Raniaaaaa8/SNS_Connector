# Projet : Collecte de posts sur Twitter

## Objectif
Ce projet permet de collecter des tweets liés à un sujet précis (par exemple, "le décès du président Jacques Chirac") en utilisant l'API Twitter. Les tweets, les images associées et les commentaires sont ensuite stockés dans une base de données MongoDB.

## Pré-requis
- Python 3.x
- Bibliothèques Python : `tweepy`, `requests`, `pymongo`, `pyyaml`

## Installation des dépendances
1. Clonez ce projet ou téléchargez les fichiers.
2. Installez les dépendances nécessaires avec la commande suivante :

```bash
pip install tweepy pymongo requests pyyaml
```
## Configuration

Créez un fichier `config.yml` avec vos informations d'API Twitter et de connexion MongoDB (voir l'exemple ci-dessous).  
Dans le fichier `config.yml`, renseignez vos clés d'API Twitter et les informations de connexion MongoDB :

```yaml
twitter:
  api_key: "VOTRE_API_KEY"
  api_secret_key: "VOTRE_API_SECRET_KEY"
  access_token: "VOTRE_ACCESS_TOKEN"
  access_token_secret: "VOTRE_ACCESS_TOKEN_SECRET"

mongodb:
  uri: "mongodb+srv://<user>:<password>@cluster0.mongodb.net/test"
  database_name: "social_media_db"
  collection_name: "posts"
```
## Utilisation

Exécutez le fichier principal `main.py` pour collecter les tweets sur un sujet donné et les enregistrer dans MongoDB.  
Exemple d'exécution :

```bash
python main.py
```
## Utilisation

Le programme collectera les tweets liés au mot-clé défini dans la variable `keyword` du fichier `main.py`, et les enregistrera dans votre base de données MongoDB.

## Structure du projet

- `config.py` : Chargement des configurations depuis `config.yml`.
- `authenticate.py` : Authentification à l'API Twitter et connexion à MongoDB.
- `collector.py` : Collecte des tweets, extraction des images et commentaires, et sauvegarde dans MongoDB.
- `main.py` : Exécution du programme principal.
- `config.yml` : Fichier de configuration des clés d'API et de la connexion MongoDB.

## Remarques

- Assurez-vous que MongoDB est bien configuré et accessible (utilisez MongoDB Atlas et le playground du fichier playground-1.mongodb.js si nécessaire).
- Les images sont téléchargées localement dans le dossier `images` (créé automatiquement).
#   S N S _ C o n n e c t o r  
 