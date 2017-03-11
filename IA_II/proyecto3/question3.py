"""
    Universidad Simon Bolivar
    CI-5438 - Inteligencia Artificial
    Edward Fernandez 10-11121
    Carlos Ferreira 11-10323
    Stefani Castellanos 11-11394

    Description:
        This file contains the answer for question 3
"""

# .----------------------------------------------------------------------------.
# Import libraries to use.

import k_means as km        # Neural Network library
import numpy as np          # This provides access to an efficient
                            # multi-dimensional container of generic data.
import pandas as pd         # This provides access to function for data manipulation
                            # and analysis.
from PIL import Image       # 

# .----------------------------------------------------------------------------.

def main():
	# Open the image.
	originalIm = Image.open("Imagen.jpg")
	wImg, hImg = originalIm.size  
	pix = originalIm.load()      # Get the image info.

	# Create the matrix to store the pixel data.
	# Each row will be the form: [x,y,z]
	pixMatrix = np.zeros((wImg * hImg, 3))

	data = np.zeros((hImg, wImg, 3), dtype=np.uint8)

	i = 0
	for h in range(0, hImg):
		for w in range(0, wImg):
			pixMatrix[i][0], pixMatrix[i][1], pixMatrix[i][2] = pix[w,h] 	
			i += 1

	result = km.k_means(pixMatrix, 2)
	newPixels = result['centroids']

	i = 0
	for h in range(0, hImg):
		for w in range(0, wImg):
			data[w,h] = newPixels[i]
			i += 1

	# Draw the new image.
	newImg = Image.fromarray(data, 'RGB')
	newImg.save('test.png')

# .----------------------------------------------------------------------------.

if __name__ == '__main__':
    main()

# .----------------------------------------------------------------------------.
