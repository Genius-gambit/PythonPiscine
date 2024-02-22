from PIL import Image
import sys
import os
import matplotlib.pyplot as plt

def	cropImage(image: Image) -> Image:
    cropSize = min(image.width, image.height)
    cropLeft = (image.width - cropSize) // 2
    cropTop = (image.height - cropSize) // 2
    cropRight = cropLeft + cropSize
    cropBottom = cropTop + cropSize
    return image.crop((cropLeft, cropTop, cropRight, cropBottom))

def	transposeImage(image: Image) -> Image:
    width, height = image.size
    transposedImage = Image.new("RGB", (height, width))
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            transposedImage.putpixel((y, x), pixel)
    return transposedImage

def	main():
    try:
        path = sys.argv[1]
        if not path.lower().endswith(('jpg', 'jpeg')):
            raise AssertionError("Only JPG and JPEG formats are supported.")
        if not os.path.exists(path):
            raise AssertionError("File not found:", path)
        image = Image.open(path)
        if image is None:
            raise AssertionError("Failed to load image.")
        image.show()
        transposedImage = transposeImage(cropImage(image))
        transposedImage.show()
        square_crop = cropImage(image)
        mirroredImage = image.transpose(Image.FLIP_LEFT_RIGHT)
        mirroredImage.show()
        
        plt.imshow(mirroredImage)
        plt.title("Mirror Image")
        plt.axis('on')
        plt.show()
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)

if __name__ == '__main__':
    main()