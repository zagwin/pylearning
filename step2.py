#!usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter

try:
	# load image
	img = Image.open('Lenna.png')
	# print information
	print 'The size of the image is: '
	print (img.format, img.size, img.mode)

	# blur image
	blurred = img.filter(ImageFilter.BLUR)

	img.show(title='Lenna')
	blurred.show()

	# save image
	blurred.save('blurred.png')
except:
	print 'Unable to load image'
