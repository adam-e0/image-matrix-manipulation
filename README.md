# image-matrix-manipulation

## Project Description

image-matrix-manipulation is a Python-based application that demonstrates image manipulation techniques using matrix operations and linear algebra concepts. The application provides two primary functions: image compression using Fourier transform frequency cutoff, and image rotation using matrix transformations.

The application is built with a graphical user interface (GUI) using tkinter, making it accessible for users to upload images, apply transformations, and visualize results interactively.

## Features

- **Image Compression**: Utilizes the Fast Fourier Transform (FFT) to compress images by removing high-frequency components. The compression level can be adjusted using a slider.
- **Image Rotation**: Rotates images using matrix transformations with adjustable rotation angles.

## Image Examples

### Image Compression

The following example demonstrates the image compression feature using a photograph of Earth:

| Original                              | Compressed                                                  |
| ------------------------------------- | ----------------------------------------------------------- |
| ![Earth - Original](images/earth.jpg) | ![Earth - Compressed](images/examples/earth-compressed.png) |

### Image Rotation

The following example demonstrates the image rotation feature using a photograph of a flower:

| Original                                | Rotated                                                 |
| --------------------------------------- | ------------------------------------------------------- |
| ![Flower - Original](images/flower.jpg) | ![Flower - Rotated](images/examples/flower-rotated.png) |

## How to Run

Install PIL (Python Image Library):

Windows:

```
pip install Pillow
```

MacOS/Linux:

```
pip3 install Pillow
```

Run the application:

```
python3 gui.py
```

## Technical Details

- **Dependencies**: numpy, Pillow (PIL), tkinter (built-in)
- **Language**: Python 3
- **Interface**: tkinter GUI

The application processes images by converting them to numpy arrays, applying mathematical transformations, and converting the results back to image format for display.
