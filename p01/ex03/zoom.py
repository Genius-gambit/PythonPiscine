from load_image import ft_load
from PIL import Image
import numpy as np
import sys
import os
import matplotlib.pyplot as plt

def	print_rows_first_elem(arr, int):
	count = 0
	for row in arr:
		count += 1
	length = count
	count = 0
	for row in arr:
		if count == 0:
			print("[[[" if int == 1 else "[[", row[0], "]", sep="")
		if count > 0 and count < 3 or count > length - 4:
			if int == 1:
				if count == length - 1:
					print("  [", row[0], "]]]", sep="")
				elif count < length - 1:
					print("  [", row[0], "]", sep="")
			else:
				print("  ", row[0], "]]" if count == (length
					- 1) else "", sep="")
		if count == 2:
			print(" ...")
		count += 1

def	main():
	try:
		path = sys.argv[1]
		if not path.lower().endswith(("jpg", "jpeg")):
			raise AssertionError("Only JPG or JPEG formats are supported.")
		if not os.path.exists(path):
			raise AssertionError("File not found", path)
		image = Image.open(path)
		if image is None:
			raise AssertionError("Failed to load image.")
		print_rows_first_elem(ft_load(path), 0)
		# image.show()
		
		zoomedImg = image.crop((400, 100, 800, 600))
		grayScaleImage = zoomedImg.convert('L')
		grayScaleImage.show()
		print_rows_first_elem(np.array(grayScaleImage), 1)
		plt.imshow(zoomedImg)
		plt.title("Zoomed Image")
		plt.axis('on')
		plt.show()
	except AssertionError as error:
		print(AssertionError.__name__ + ":", error)
	
if __name__ == '__main__':
	main()