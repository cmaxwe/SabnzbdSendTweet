#Script to use if you are not launching the tweet from another script
import sys

import send_tweet

if len(sys.argv) == 8:
	send_tweet.send_tweet(sys.argv[3])
