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
    listToPrint = textToPrint.split()
    #print(*listToPrint, sep='\n')
    # 6. Print text 
    for word in listToPrint :
        image = t2p.wordToBitmap(word)
        t2p.waterPrint(image) # if I surround with print() it will print 'None' at the end (indica redundancia)