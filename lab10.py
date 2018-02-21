import tweepy
 
# personal details
consumer_key ="xxxxxxxxxxxxx"
consumer_secret ="sxxxxxxxxxxxxxxxxx"
access_token ="xxxxxxxxxxxxxx"
access_token_secret ="xxxxxxxxxxxxxxxxxxx"
 
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
# update the status
api.update_status(status ="hi!")
