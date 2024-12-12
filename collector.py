import requests
import time
import tweepy
from authentificate import authenticate_twitter_api

def collect_tweets(keyword):
    """Collecte des tweets liés à un mot-clé donné."""
    client = authenticate_twitter_api()
    max_tweets=10 # entre 10 et 100
    response=None
    try:
        response = client.search_recent_tweets(query=keyword, max_results=max_tweets, tweet_fields=["created_at", "author_id", "text", "public_metrics"])  # Collecte 10 tweets
        
    except tweepy.errors.TooManyRequests:
            print("Limite de requêtes atteinte. Pause pendant 15 minutes...")
            #time.sleep(15 * 60)  # Pause de 15 minutes pour éviter le blocage
    except Exception as e:
            print(f"Erreur lors de la collecte des tweets : {e}")
    return response

def save_to_mongo(tweet_data, db):
    """Enregistre les tweets et les images dans MongoDB."""
    collection = db["posts"]  # Nom de la collection
    tweet_record = {
        "text": tweet_data['text'],
        "image_url": tweet_data['image_url'],
        "comments": tweet_data['comments'],
        "date": tweet_data['date']
    }
    collection.insert_one(tweet_record)  # Insérer le tweet dans la collection

def download_image(image_url, image_id):
    """Télécharge l'image et la sauvegarde localement."""
    try:
        response = requests.get(image_url)
        image_path = f'images/{image_id}.jpg'
        with open(image_path, 'wb') as file:
            file.write(response.content)
        return image_path
    except Exception as e:
        print(f"Erreur lors du téléchargement de l'image: {e}")
        return None

def extract_image_and_comments(tweet):
    """Extrait les images et commentaires d'un tweet."""
    entities = tweet.entities if tweet.entities else {}  # Vérifie que 'entities' n'est pas None
    media = entities.get('media', [{}])  # Récupère les médias s'ils existent
    image_url = media[0].get('media_url') if media else None  # Vérifie si une image est présente

    tweet_data = {
        'text': tweet.text,
        'image_url': image_url,
        'comments': [],  # Les commentaires ne peuvent pas être directement récupérés avec l'API
        'date': tweet.created_at
    }
    return tweet_data
