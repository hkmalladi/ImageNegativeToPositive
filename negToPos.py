from PIL import Image

file = open('lsOutput.csv','r')
lines = file.readlines()
# lsOutput.csv contains the list of files to be processed. Easiest way to populate it is by making it the output of the ls command.

for raw_image_file in lines:
  raw_image_file = raw_image_file.rstrip()
  raw_image = Image.open(raw_image_file)
  WIDTH,HEIGHT = raw_image.size
  neg_image = Image.new("RGB",(WIDTH,HEIGHT))
  raw_pixels = raw_image.load()
  neg_pixels = neg_image.load()

  for Y in range(HEIGHT):
	for X in range(WIDTH):
		# Getting RGB of each pixel
		R,G,B = raw_pixels[X,Y]
		oR = (R*.393) + (G*.769) + (B*.189)
		oG = (R*.349) + (G*.686) + (B*.168)
		oB = (R*.272) + (G*.534) + (B*.131)
		# Writing pixel data after doing necessary manipulations
		neg_pixels[X,Y] = (255-R,255-G,255-B)
# Saving the images after appending the string 'positive_' before them
  neg_image.save('positive_' + raw_image_file)
