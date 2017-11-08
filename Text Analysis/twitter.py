import tweepy
from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("Vadodara, Gujarat, India")
from textblob import TextBlob

# Consumer keys and access tokens, used for OAuth
consumer_key        = 'E1JNN3IMIh6F6bmsK2BQOGBhP'
consumer_secret     = 'm6coRZ7eEc4GzybqezZmjPnWRb6FA1MhCUKo0QVuulWyqdWOrk'
access_token        = '1374602324-IRs1aPkpDUIumTfNcSmoHcmQWjge5IYpoTVnc2y'
access_token_secret = '263wMQvZ6JJsxtpMAOZAGivIBPgFbvcejYuuKNBJqLgme'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Send the tweet
#message = 'This is a test'
#api.update_status(message)
#print(api.trends_closest(location.latitude, location.longitude))
#dd = api.trends_place(2295402) # WOEID of your location (WOEID = Where on earth ID)
#for i in range(0,10):          # Returns top 10 Trends for the place
#    print(dd[0]['trends'][i]['name'])

def sentiment_analysis(quote, num_tweets):
    # Checks if the sentiment for our quote is
    # positive or negative, returns True if
    # majority of valid tweets have positive sentiment
    list_of_tweets = api.search(quote, count=num_tweets)
    positive, null = 0, 0
    #dd = Userdata()
    for tweet in list_of_tweets:
        #ww = dd.FilterData(tweet.text)
        
        blob = TextBlob(tweet.text).sentiment
        if not blob.subjectivity == 0:
            print(tweet.text.encode('utf-8'))
        
            if blob.subjectivity == 0:
                null += 1
                next
            if blob.polarity > 0:
                print(blob.polarity)
                print()
                positive += 1
            else:
                print(blob.polarity)
                print()
            
    if positive > ((num_tweets - null)/2):
        return True
    else:
        return False
    

print(sentiment_analysis('BJP',50))

