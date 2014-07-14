from PIL import Image


im = Image.open("OPEN IMAGE HERE").convert("RGB")

pixels = list(im.getdata())
width, height = im.size
pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]

print 'BREAK'
def getCharacter(R,G,B):
	luminosity = (0.2126*R + 0.7152*G + 0.0722*B)
	if luminosity > 200:
		return ' '
	elif luminosity > 150:
		return '.'
	elif luminosity > 100:
		return '^'
	elif luminosity > 50:
		return 'F'
	elif luminosity > 0:
		return '@'
	return '@'

with open("someText.txt","a") as f:
	for i in range(width):
		for j in range(height):
			r,g,b = pixels[i][j]
			f.write(getCharacter(r,g,b))
		f.write('\n')

