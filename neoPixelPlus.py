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


	def gradient(self,startColor, endColor):
		stepSize = self.numPixels - 1
		rStep = (endColor[0] - startColor[0])/stepSize
		gStep = (endColor[1] - startColor[1])/stepSize
		bStep = (endColor[2] - startColor[2])/stepSize
		for index in range(self.numPixels):
			nextRed = round(startColor[0]+(index*rStep))
			nextGreen = round(startColor[1]+(index*gStep))
			nextBlue = round(startColor[2]+(index*bStep))
			self[index]= (nextRed,nextGreen,nextBlue)