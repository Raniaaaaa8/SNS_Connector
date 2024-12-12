# main.py : Fichier principal pour lancer le programme
import os
from collector import collect_tweets, save_to_mongo, download_image, extract_image_and_comments
from authentificate import connect_to_mongodb

def main():
    # Connexion à MongoDB
    db = connect_to_mongodb()
    
    # Collecte de tweets
    keyword = "décès du président Jacques Chirac"
    tweets = collect_tweets(keyword)
    if tweets :
        for tweet in tweets.data:
            tweet_data = extract_image_and_comments(tweet)
            
            # Sauvegarde des tweets dans MongoDB
            save_to_mongo(tweet_data, db)
            
            # Télécharger l'image si elle existe
            if tweet_data['image_url']:
                image_path = download_image(tweet_data['image_url'], tweet.id)
                tweet_data['image_path'] = image_path
            
            print(f"Tweet enregistré: {tweet_data['text'][:100]}...")  # Affiche un extrait du texte du tweet

if __name__ == "__main__":
    main()
