SabnzbdSendTweet
================

Post Processing script to send a tweet with the download


General Instructions
----------------------
1. Download this repo
2. Move the two script files (send_tweet.py & send_standalone_tweet.py) to your Sabnzbd scripts directory
3. Install tweepy
    - sudo apt-get install python-pip
    - sudo pip install tweepy
4.  Create a twitter account (or use an existing)
5.  Create a twitter application with that account (http://iag.me/socialmedia/how-to-create-a-twitter-app-in-8-easy-steps/)
    - Make sure it is read & write
6. Open send_tweet.py and replace the variables in the file with your variables from twitter


***Given that you can only assign one post processing script to a given category in Sabnzbd you may need to edit the CouchPotato and/or Sickbeard scripts to piggyback on them. Follow the instructions for each below if you want to piggy back on the CouchPotato script or Sickbeard script that are already running.***

CouchPotato
--------------------------
1. Follow General Instructions
2. Open sabToCouch.py
3. Add "import send_tweet" under "import autoProcessMovie"
4. Add "send_tweet.send_tweet(sys.argv[3])" under "autoProcessMovie.process(sys.argv[1], sys.argv[2], sys.argv[7])"
5. Profit!!!!!

SickBeard Instructions
-------------------------
1. Follow General Instructions
2. Open sabToCouch.py
3. Add "import send_tweet" under "import autoProcessMovie"
4. Add "send_tweet.send_tweet(sys.argv[3])" under "autoProcessTV.processEpisode(sys.argv[1], sys.argv[2])"
5. Profit!!!!!!

Standalone Installation Instructions
--------------------------
1. Follow General Instructions
2. Open Sabnzbd in a browser
3. Navigate to Config
4. Navigate to Categories in Config
5. Choose "send_standalone_tweet.py" for any categories that you want to trigger tweets
6. Profit!!!!!

