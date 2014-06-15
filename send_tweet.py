import tweepy

def send_tweet(message):
	#Replace the following variables
	consumer_key = "YOUR_KEY"
	consumer_secret = "YOUR_SECRET"
	access_token = "YOUR_TOKEN"
	access_token_secret = "YOUR_TOKEN_SECRET"

	#Can leave blank if you don't want to mention anyone in the tweets.
	user_names_to_mention = "@YOUR_TWITTER_USERNAME"


	#Setup authentication and create API object
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	#Clip Message To 140
	total_len = len(message) + len(user_names_to_mention) + 1

	if(total_len > 140):
   		message = message[0:(140 - len(user_names_to_mention) - 4)] + "..."

	#Send the message
	api.update_status(user_names_to_mention + " " + message)
