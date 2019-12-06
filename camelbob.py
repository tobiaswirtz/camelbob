import os
import sys
import textwrap
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

def formatString(s):
	newStr = ""
	for i in range(len(s)):
		if i % 2 == 0:
			newStr = newStr + s[i].lower()
		else:
			newStr = newStr + s[i].upper()
	return newStr

inputStr = sys.argv[1]

d = datetime.now(tz=None).strftime("%m-%d-%Y.%H:%M:%S")
filepath = "imgs/" + d + ".jpg"

os.system("cp Mocking-Spongebob.jpg " + filepath)

image = Image.open(filepath)
W, H = image.size

inputLength = len(inputStr)

canvas = ImageDraw.Draw(image)

inputStr = formatString(inputStr)
font  = ImageFont.truetype('Impact.ttf', size=23)
shadowcolor = "black"
lines = textwrap.wrap(inputStr, width=40)
y_text = 275 - (len(lines) * 6)
for line in lines:
	width, height = canvas.textsize(line, font=font)
	canvas.text((((W-width)/2) - 1, y_text), line, font=font, fill=shadowcolor)
	canvas.text((((W-width)/2) + 1, y_text), line, font=font, fill=shadowcolor)
	canvas.text((((W-width)/2), y_text - 1), line, font=font, fill=shadowcolor)
	canvas.text((((W-width)/2), y_text + 1), line, font=font, fill=shadowcolor)
	canvas.text((((W-width)/2), y_text), line, font=font)
	y_text += height

canvas = ImageDraw.Draw(image)

image.save(filepath)
command = "impbcopy " + filepath
os.system(command)
