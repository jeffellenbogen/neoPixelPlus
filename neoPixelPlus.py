from microbit import *
import neopixel

class neoPixelPlus(neopixel.NeoPixel)
	def __init__(self, pin, numPixels):
		super().__init__(pin,numPixel)
		self.numPixels = numPixels

	def rotate(strip, direction):
		length = self.numPixels
		# Rotate pixels left
		if (direction == -1):
			tempPixelData = strip[0]
			for index in range(length-1):
				strip[index]=strip[index+1]
			strip[length-1]=tempPixelData			