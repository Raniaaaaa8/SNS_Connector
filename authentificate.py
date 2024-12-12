import pymongo
import tweepy
import yaml
import os

# Charger les configurations à partir du fichier config.yml
def load_config():
    """Charge la configuration depuis le fichier YAML."""
    with open('config.yml', 'r') as file:
        config = yaml.safe_load(file)
    return config

# Fonction pour authentifier l'API Twitter
def authenticate_twitter_api():
    """Authentifie et renvoie le client API Twitter à partir du fichier de config."""
    config = load_config()
    
    bearer_token = config['twitter']['bearer_token']
    
    
    client = tweepy.Client(bearer_token=bearer_token)
    return client

# Connexion à MongoDB
def connect_to_mongodb():
    """Retourne la connexion MongoDB et crée la base de données et la collection si elles n'existent pas."""
    config = load_config()
    mongo_uri = config['mongodb']['uri']
    database_name = config['mongodb']['database_name']
    
    try:
        client = pymongo.MongoClient(mongo_uri)
        db = client[database_name]  # Crée la base de données (si elle n'existe pas)
        
        # Créer la collection si elle n'existe pas déjà
        collection = db[config['mongodb']['collection_name']]
        
        print(f"Connexion à MongoDB réussie. Base de données : {database_name}, Collection : {config['mongodb']['collection_name']}")
        return db
    except Exception as e:
        print(f"Erreur lors de la connexion à MongoDB : {e}")
        return None
