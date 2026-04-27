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

<table style="width:100%">
  <tr>
    <td style="width:50%"><img src="images/earth.jpg" alt="Earth - Original"></td>
    <td style="width:50%"><img src="images/examples/earth-compressed.png" alt="Earth - Compressed"></td>
  </tr>
</table>

### Image Rotation

The following example demonstrates the image rotation feature using a photograph of a flower:

<table style="width:100%">
  <tr>
    <td style="width:50%"><img src="images/flower.jpg" alt="Flower - Original"></td>
    <td style="width:50%"><img src="images/examples/flower-rotated.png" alt="Flower - Rotated"></td>
  </tr>
</table>

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
