from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy,json
conkey = 'f7fAWeRuKEANYP7xOcy8O1haV'
consec = 'ck98S69p3FzMudnBQ7xJHsY5JsNvx1JJXbfi6eOp6rWrtEJDjS'
access_token = '2283497094-g69dRa2o5hgUD36rhSV8Fd13BFeOH8NDCCkBk9x'
access_token_secret = 'kiLSMAJ2M5mKy970wWd6Fmfoo9ACJGFwebPzu6cUiLzMS'
auth = tweepy.OAuthHandler(conkey, consec)
auth.set_access_token(access_token, access_token_secret)

#api = tweepy.API(auth)

#status = "Testing AllAuth!"
#api.update_status(status=status)

#public_tweets = api.feed()
##pass

#consumer key, consumer secret, access token, access secret.
#ckey="fsdfasdfsafsffa"
#csecret="asdfsadfsadfsadf"
##atoken="asdf-aassdfs"
#asecret="asdfsadfsdafsdafs"
global count

#print(twitterStream)
