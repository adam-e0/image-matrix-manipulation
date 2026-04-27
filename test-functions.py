from PIL import Image

import functions as imageFuncs

imageFuncs.processImage(Image.open("./images/ipadmini.png"), 0.5).show()
