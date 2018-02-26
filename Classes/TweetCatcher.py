import twitter
import json

#print(json.dumps(<JSON OBJECT>, indent=2, sort_keys=True))

class TweetCatcher:
    
    def __init__(self):
        pass

    api = twitter.Api(consumer_key='cBhspMmZrb7gsOMvsnYJt67bI',
                  consumer_secret='UNSjkK9EjabjDD7SDigDR08eRMjiRBV1jb2N82B7fK9NeDEnuj',
                  access_token_key='962653614215974913-IlVgNftSrFbR1D45g4KwydYGj5w5Q4D',
                  access_token_secret='s42w0005PVkyPrT1GusV2JPYOMFGNACZXF8STEHD4vp5V')    

    @classmethod
    def getUserId(self, userAccount):
        user = self.api.GetUser(screen_name=userAccount)
        jsUser =json.loads(str(user))
        userId = jsUser['id']               
        return str(userId)

    @classmethod
    def getUserLastTweet(self, user_id):
        status = self.api.GetUserTimeline(user_id=user_id, count=1)
        return status[0].text

    @classmethod
    def getHomeLastTweet(self):
        tweet = self.api.GetUserTimeline(count=1)[0]
        return tweet

    @classmethod
    def getTweetHashtagsList(self, tweet):
        hl = []
        for hashtag in tweet.hashtags:
            hl.append(hashtag.text)
        return hl

    @classmethod
    def getTweetText(self, tweet):
        return tweet.text

    @classmethod
    def isHashtagThere(self, present, hashtags):    
        return present.lower() in [hashtag.lower() for hashtag in hashtags] 
    
    @classmethod
    def retrieveTextToPrint(self, text):
        return text.lower().replace('#waterprint','').strip()
        