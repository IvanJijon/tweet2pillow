from Classes.TweetCatcher import TweetCatcher
from Classes.Text2Pillow import Text2Pillow

# Initialization

t2p = Text2Pillow()

# 1. Get Last tweet
lastTweet = TweetCatcher.getHomeLastTweet()
# 2. Get tweet's text
tweetText = TweetCatcher.getTweetText(lastTweet)
# 3. Get tweet's hashtags
hashtags = TweetCatcher.getTweetHashtagsList(lastTweet)
# 4. Verify if hashtag 'waterPrint' is present
if TweetCatcher.isHashtagThere('waterPrint', hashtags) :
    # 5. retrieve text to print
    textToPrint = TweetCatcher.retrieveTextToPrint(tweetText)
    #print(textToPrint)
    listToPrint = textToPrint.split()
    #print(*listToPrint, sep='\n')
    
    t2p.wordToBit('tata')