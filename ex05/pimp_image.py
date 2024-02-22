from load_image import ft_load
from PIL import Image
import numpy as np

def	ft_invert(array):
	image = 255 - array
	Image.fromarray(image).show()

def	ft_red(array):
	redChannel = array[:, :, 0]
	image = np.zeros_like(array)
	image[:, :, 0] = redChannel
	Image.fromarray(image).show()

def	ft_green(array):
	greenChannel = array[:, :, 1]
	image = array.copy()
	image[:, :, 0] = 0
	image[:, :, 2] = 0
	image[:, :, 1] = greenChannel
	Image.fromarray(image).show()

def	ft_blue(array):
	blueChannel = array[:, :, 2]
	image = np.zeros_like(array)
	image[:, :, 2] = blueChannel
	Image.fromarray(image).show()

def	ft_grey(array):
    redChannel = array[:, :, 0] / 3
    greenChannel = array[:, :, 1] / 3
    blueChannel = array[:, :, 2] / 3
    greyChannel = redChannel + greenChannel + blueChannel
    greyImage = np.stack([greyChannel, greyChannel, greyChannel], axis=2)
    Image.fromarray(greyImage.astype(np.uint8)).show()

if __name__ == '__main__':
	array = ft_load('1.jpg')
	ft_grey(array)