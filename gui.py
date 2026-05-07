import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import functions as imageFuncs


class ImageMatrixApp:
    # Runs automatically when the app is created
    def __init__(self, root):
        self.root = root
        self.root.title("Image Matrix Manipulation")
        self.root.geometry("900x600")

        # Store original and working image; photoImage kept as instance var to prevent garbage collection
        self.originalImage = None
        self.displayImage = None
        self.photoImage = None

        self.setupLayout()

    def setupLayout(self):
        # Left control panel
        self.controlFrame = tk.Frame(self.root, width=250, padx=15, pady=15)
        self.controlFrame.pack(side=tk.LEFT, fill=tk.Y)

        # Right image display area
        self.imageFrame = tk.Frame(self.root, padx=15, pady=15)
        self.imageFrame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        # Upload button
        self.uploadButton = tk.Button(
            self.controlFrame, text="Upload Image", command=self.uploadImage
        )
        self.uploadButton.pack(fill=tk.X, pady=10)

        # Dropdown label
        self.operationLabel = tk.Label(self.controlFrame, text="Select Operation:")
        self.operationLabel.pack(anchor="w", pady=(20, 5))

        # Dropdown menu
        self.operationChoice = tk.StringVar()
        self.operationDropdown = ttk.Combobox(
            self.controlFrame, textvariable=self.operationChoice, state="readonly"
        )
        self.operationDropdown["values"] = [
            "Image Compression",
            "Rotation",
        ]
        self.operationDropdown.current(0)
        self.operationDropdown.pack(fill=tk.X)

        # Slider label
        self.sliderLabel = tk.Label(self.controlFrame, text="Amount:")
        self.sliderLabel.pack(anchor="w", pady=(30, 5))

        # Slider (0-100, maps to particular operation range in applyOperation)
        self.blurSlider = tk.Scale(
            self.controlFrame,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            command=self.updateSlider,
        )
        self.blurSlider.set(1)
        self.blurSlider.pack(fill=tk.X)

        # Apply button
        self.applyButton = tk.Button(
            self.controlFrame, text="Apply Operation", command=self.applyOperation
        )
        self.applyButton.pack(fill=tk.X, pady=30)

        # Credits
        self.creatorLabel = tk.Label(
            self.controlFrame,
            text="Created By: Adam Ettachfini, Sophie Kawi, and Zolbayar Batmunkh",
            font=("Arial", 8),
            wraplength=220,
            justify="left",
        )
        self.creatorLabel.pack(side=tk.BOTTOM, anchor="w", pady=10)

        # Image display area (shows a placeholder text until an image is uploaded)
        self.imageLabel = tk.Label(
            self.imageFrame,
            text="Upload an image to begin",
            bg="lightgray",
        )
        self.imageLabel.pack(expand=True)

    def uploadImage(self):
        # Open file picker and load the selected image
        filePath = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg *.jpeg *.png"), ("All Files", "*.*")]
        )

        if filePath:
            # Scale image on load and convert to RGB
            self.originalImage = imageFuncs.scaleImage(
                Image.open(filePath), 700
            ).convert("RGB")

            # Keep a copy so we don't overwrite the original
            self.displayImage = self.originalImage.copy()

            self.showImage(self.displayImage)

    def showImage(self, image):
        # Resize a copy to fit the display area without modifying the actual image data
        imageCopy = image.copy()
        imageCopy.thumbnail((1200, 800))

        self.photoImage = ImageTk.PhotoImage(imageCopy)
        self.imageLabel.config(image=self.photoImage, text="", bg=self.root.cget("bg"))

    def updateSlider(self, value):
        print(f"Slider value: {value}")

    def applyOperation(self):
        selectedOperation = self.operationChoice.get()
        sliderValue = self.blurSlider.get()

        print(f"Selected operation: {selectedOperation}")
        print(f"Slider value: {sliderValue}")

        if self.displayImage is None:
            print("No image uploaded yet.")
            return

        if selectedOperation == "Image Compression":
            # Map slider (0-100) to a 0.0-1.0 frequency cutoff
            self.displayImage = imageFuncs.processImage(
                self.originalImage, (sliderValue / 100)
            )
        elif selectedOperation == "Rotation":
            # Map slider (0-100) to a 0 to 2*pi rotation in radians
            self.displayImage = imageFuncs.rotateImage(
                self.originalImage, (sliderValue / 100 * (2 * 3.14159))
            )
        else:
            print("No function applied")

        self.showImage(self.displayImage)


def main():
    root = tk.Tk()
    app = ImageMatrixApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()