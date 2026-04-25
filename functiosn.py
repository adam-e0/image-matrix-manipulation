from PIL import Image


def processImage(inputPath):
    img = Image.open(inputPath)
    print(f"Successfully loaded: {inputPath}")
    print(f"Format: {img.format}")
    print(f"Size: {img.size}")
    print(f"Mode: {img.mode}")
    new_size = (400, 100)
    resized_img = img.resize(new_size)
    resized_img.show()


processImage("./images/flower.jpg")
