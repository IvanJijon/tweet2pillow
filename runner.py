from Classes.TweetCatcher import TweetCatcher
from Classes.Text2Pillow import Text2Pillow


t2p = Text2Pillow()

text = ['Enanito123']
for word in text :
    image = t2p.wordToBitmap(word)
    t2p.waterPrint(image) # if I add print() it will print None at the end