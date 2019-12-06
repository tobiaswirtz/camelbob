import os
import sys
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

def getSize(strLen):
	strSpan = 512 - 1
	fontSpan = 54 - 6
	valueScaled = float(-strLen - 1) / float(strSpan)
	return 6 + int(valueScaled * fontSpan)

inputStr = sys.argv[1]

d = datetime.now(tz=None).strftime("%m-%d-%Y.%H:%M:%S")
filepath = "imgs/" + d + ".jpg"

os.system("cp Mocking-Spongebob.jpg " + filepath)

image = Image.open(filepath)

canvas = ImageDraw.Draw(image)
font  = ImageFont.truetype('Impact.ttf', size=getSize(len(inputStr)))
