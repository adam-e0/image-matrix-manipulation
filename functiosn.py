import numpy as np
from PIL import Image


def getImage(inputPath):
    img = Image.open(inputPath)
    return img


def scaleImage(img, width):
    return img.resize((width, width * img.size[1] // img.size[0]))


def processImage(img, freqCutOff):
    print(f"Size: {img.size}")
    print(f"Mode: {img.mode}")

    # Convert image into array
    imgArr = np.array(img)
    # Perform the Fourier transform on the image array
    imgFft = np.fft.fft2(imgArr, axes=(0, 1))
    # Shift the Fourier transform
    imgFftShifted = np.fft.fftshift(imgFft, axes=(0, 1))
    # Get array dimensions
    rows = imgArr.shape[0]
    cols = imgArr.shape[1]
    # Create a grid of coordinates for frequency calculation to use the center of the shifted FFT as the origin
    crow = rows // 2
    ccol = cols // 2
    y, x = np.meshgrid(
        np.arange(-crow, rows - crow), np.arange(-ccol, cols - ccol), indexing="ij"
    )
    freqDist = np.sqrt(x**2 + y**2)

    # Using the flattened version of the FFT to sort by frequency for each of the RGB channels
    channels = []
    for c in range(imgArr.shape[2]):
        channel_fft = imgFftShifted[:, :, c]
        flatFft = channel_fft.flatten()
        flatFreq = freqDist.flatten()

        sort_indices = np.argsort(flatFreq)[::-1]
        num_to_cut = int(len(flatFft) * freqCutOff)

        keep_indices = sort_indices[num_to_cut:]

        reconstructed_flat = np.zeros_like(flatFft)
        reconstructed_flat[keep_indices] = flatFft[keep_indices]

        reconstructed_channel = reconstructed_flat.reshape(rows, cols)
        # Inverse shift and inverse FFT
        reconstructed_channel_inv = np.fft.ifftshift(reconstructed_channel, axes=(0, 1))
        reconstructed_channel_final = np.fft.ifft2(
            reconstructed_channel_inv, axes=(0, 1)
        )
        channels.append(reconstructed_channel_final)

    finalArr = np.stack(channels, axis=2)

    # Post-processing: magnitude and conversion to uint8
    finalArrAbs = np.abs(finalArr)

    # Normalize to 0-255
    if finalArrAbs.max() != 0:
        finalArrAbs = (finalArrAbs / finalArrAbs.max()) * 255

    finalImgArr = finalArrAbs.astype(np.uint8)

    # Convert back to Image and save
    resultImg = Image.fromarray(finalImgArr)

    return resultImg
