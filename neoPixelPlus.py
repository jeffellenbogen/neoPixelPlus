from microbit import *
import neopixel

class neoPixelPlus(neopixel.NeoPixel):
	def __init__(self, pin, numPixels):
		super().__init__(pin,numPixels)
		self.numPixels = numPixels

	def rotate(self, direction):
		length = self.numPixels
		# Rotate pixels left
		if (direction == -1):
			tempPixelData = self[0]
			for index in range(length-1):
				self[index]=self[index+1]
			self[length-1]=tempPixelData
		else:
			tempPixelData = self[length-1]
			for index in range(length-1, 0, -1): # for loop with three parameters -> (start, finish, increment)		
				self[index]=self[index-1]
			self[0]=tempPixelData


