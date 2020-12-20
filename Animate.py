import csv
import os
from PIL import Image

inputfolder = "./input/SantaAndDeer"

with open('output.csv', mode='a') as file:
	writer = csv.writer(file)
	frame = 0
	for filename in os.listdir(inputfolder):
		img = Image.open(os.path.join(inputfolder,filename))
		width, height = img.size
		img = img.convert('RGB')
		img = img.transpose(Image.FLIP_TOP_BOTTOM)
		z=0
		for x in range(width):
			for y in range(height):
				z+=1
				r,g,b = img.getpixel((x,y))
				data = [x,y,z,r,g,b,frame]
				writer.writerow(data)
		frame +=1

