from PIL import Image, ImageFont, ImageDraw

class Text2Pillow:

    def __init__(self):
        pass

    def wordToBitmap(self, textToShow):
        # load the font and letter size
        font = ImageFont.truetype('arialbd.ttf', 15)
        # retrieve the size of text in pixels - returns X Y : X cols Y rows
        size = font.getsize(textToShow) 
        # create image canvas
        image = Image.new('1', size, 1)  #create a b/w image
        # creat a draw object to draw in the canvas
        draw = ImageDraw.Draw(image)
        # draw in the canvas
        draw.text((0, 0), textToShow, font=font)
        # return bitmap
        return image

    def waterPrint (self, image):
        # scan the bitmap:
        # print ' ' for black pixel and 
        # print '#' for white one
        for rownum in range(image.height): 
            line = []
            for colnum in range(image.width):
                # True = 1, False = 0
                if image.getpixel((colnum, rownum)): 
                    line.append(' ')
                else: 
                    line.append('♡')
            # Print line by line
            print (''.join(line))