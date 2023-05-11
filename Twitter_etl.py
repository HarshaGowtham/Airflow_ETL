import tweepy
import s3fs
import json
import pandas as pd
from datetime import datetime


access_key = "XeWI5Af9srBmiZidWxcHqccOS"

access_secret_key = "r8KlSEPH3BIRu1uXq4nNU546YyAzuHMPP60NsL1GFO2usoKGcL"

consumer_key = "904245926637707265-jKorBLYNjQXfbToD25qfMwbCUcTlTJW"

consumer_secret_key = "NzjSdiBBtyI9nofT32gaeem5pgnd8ZvN8TT4vdZurcpPV"

#twitter authentication

auth = tweepy.OAuthHandler(access_key, access_secret_key)
auth.set_access_token(consumer_key, consumer_secret_key)

api = tweepy.API(auth)

tweets = api.user_timeline(screen_name = '@elonmusk' , count = 200, include_rts = False, )
