from microbit import *
import neopixel

class neoPixelPlus(neopixel.NeoPixel)
	def __init__(self, pin, numPixels):
		super().__init__(pin,numPixel)
		self.numPixels = numPixels