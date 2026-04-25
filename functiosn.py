import numpy as np
from PIL import Image


def getImage(inputPath):
    img = Image.open(inputPath)
    return img


def processImage(inputPath, freqCutOff):
    img = Image.open(inputPath)
    print(f"Successfully loaded: {inputPath}")
    print(f"Format: {img.format}")
    print(f"Size: {img.size}")
    print(f"Mode: {img.mode}")
    imgArr = np.array(img)
    imgFft = np.fft.fft2(imgArr)

    # Add here

    print(imgFft)


processImage("./images/flower.jpg", 0.5)
