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
	originalIm = Image.open("Imagen2.jpg")
	wImg, hImg = originalIm.size  
	pix = originalIm.load()      # Get the image info.

	kClusters = [2,4,8,16,32,64,128]

	for k in kClusters:
		print "Cantidad de clusters a usar: " + str(k)
		# Create the matrix to store the pixel data.
		# Each row will be the form: [x,y,z]
		pixMatrix = np.zeros((wImg * hImg, 3))

		data = np.zeros((hImg, wImg, 3), dtype=np.uint8)

		i = 0
		for w in range(0, wImg):
			for h in range(0, hImg):
				pixMatrix[i][0], pixMatrix[i][1], pixMatrix[i][2] = pix[w,h] 	
				i += 1

		print "Se usa k-means"
		result = km.k_means(pixMatrix, k)

		j = 0
		for w in range(0, wImg):
			for h in range(0, hImg):
				for i in range(0, len(result['clusters'])):
					if np.any(result['clusters'][i] == pixMatrix[j]):	
						data[h,w] = result['centroids'][i]
						break
				j += 1
		

		# Draw the new image.
		print "Se crea la nueva imagen con " + str(k) + " colores \n"
		newImg = Image.fromarray(data, 'RGB')
		newImg.save('Imagen_' + str(k) + ".png")

# .----------------------------------------------------------------------------.

if __name__ == '__main__':
    main()

# .----------------------------------------------------------------------------.
