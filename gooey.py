# tkinter is Python's built-in library for making simple user interfaces.
# We import it as "tk" so we can write tk.Button, tk.Label, tk.Frame, etc.
import tkinter as tk

# filedialog lets us open a file picker window so the user can choose an image.
# ttk gives us nicer-looking tkinter widgets.
# Here, we use it for the dropdown menu.
from tkinter import filedialog, ttk

# Image lets us open and work with image files.
# ImageTk converts Pillow images into a format tkinter can display.
from PIL import Image, ImageTk

# Import the image functions
import functiosn as imageFuncs


# This class represents the whole application.
# A class keeps all the GUI code organized in one place.
class ImageMatrixApp:
    # __init__ runs automatically when we create an ImageMatrixApp object.
    # root is the main tkinter window.
    def __init__(self, root):
        # Save the main window so other functions can use it.
        self.root = root

        # Set the title shown at the top of the window.
        self.root.title("Image Matrix Manipulation")

        # Set the starting size of the window: width x height.
        self.root.geometry("900x600")

        # This will store the original uploaded image.
        # It starts as None because no image has been uploaded yet.
        self.originalImage = None

        # This will store the image currently being displayed/edited.
        self.displayImage = None

        # This stores the tkinter-compatible version of the image.
        # We keep it as self.photoImage so Python does not delete it from memory.
        self.photoImage = None

        # Build all the buttons, labels, dropdowns, slider, and image area.
        self.setupLayout()

    # This function creates and places everything in the window.
    def setupLayout(self):
        # Main layout frames

        # Create the left control panel.
        # width=250 gives it a fixed starting width.
        # padx and pady add spacing inside the frame.
        self.controlFrame = tk.Frame(self.root, width=250, padx=15, pady=15)

        # Put the control frame on the left side.
        # fill=tk.Y makes it stretch vertically.
        self.controlFrame.pack(side=tk.LEFT, fill=tk.Y)

        # Create the right frame where the image will be displayed.
        self.imageFrame = tk.Frame(self.root, padx=15, pady=15)

        # Put the image frame on the right.
        # expand=True lets it take up extra space.
        # fill=tk.BOTH lets it stretch horizontally and vertically.
        self.imageFrame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        # Upload button !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        # Create a button inside the left control frame.
        # text is what appears on the button.
        # command=self.uploadImage means run uploadImage when clicked.
        self.uploadButton = tk.Button(
            self.controlFrame, text="Upload Image", command=self.uploadImage
        )

        # Put the button on the screen.
        # fill=tk.X makes it stretch horizontally.
        # pady=10 adds vertical spacing.
        self.uploadButton.pack(fill=tk.X, pady=10)

        # Dropdown label !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        # This label tells the user what the dropdown is for.
        self.operationLabel = tk.Label(self.controlFrame, text="Select Operation:")

        # anchor="w" aligns the label to the left.
        # pady=(20, 5) gives 20 pixels above and 5 pixels below.
        self.operationLabel.pack(anchor="w", pady=(20, 5))

        # Dropdown menu !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        # StringVar stores the currently selected dropdown option.
        self.operationChoice = tk.StringVar()

        # Create the dropdown menu.
        # textvariable connects the dropdown to operationChoice.
        # state="readonly" means users can only select options, not type their own.
        self.operationDropdown = ttk.Combobox(
            self.controlFrame, textvariable=self.operationChoice, state="readonly"
        )

        # These are the options shown in the dropdown.
        self.operationDropdown["values"] = [
            "Image Compression",
            "Matrix Addition",
            "Scalar Addition",
            "Transpose",
            "Transformation",
        ]

        # Select the first option by default.
        self.operationDropdown.current(0)
        # Place the dropdown on the screen and stretch it horizontally.
        self.operationDropdown.pack(fill=tk.X)

        # Slider label !!!!!!!!!!!!!!!!!!!!!!!!!!!!

        # This label explains what the slider controls.
        self.sliderLabel = tk.Label(self.controlFrame, text="Amount:")

        # Place the slider label on the left side.
        self.sliderLabel.pack(anchor="w", pady=(30, 5))

        # Slider !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        # Create a horizontal slider.
        # from_=1 means the smallest value is 1.
        # to=20 means the largest value is 20.
        # command=self.updateSlider means updateSlider runs whenever the slider moves.
        self.blurSlider = tk.Scale(
            self.controlFrame,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            command=self.updateSlider,
        )

        # Set the starting slider value to 1.
        self.blurSlider.set(1)

        # Place the slider on the screen and stretch it horizontally.
        self.blurSlider.pack(fill=tk.X)

        # Apply button !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        # This button will eventually apply the selected matrix/image operation.
        # Right now, it mostly prints values and refreshes the image.
        self.applyButton = tk.Button(
            self.controlFrame, text="Apply Operation", command=self.applyOperation
        )

        # Place the Apply button on the screen.
        self.applyButton.pack(fill=tk.X, pady=30)

        # Creator credit text !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        # Create small text at the bottom-left showing the project creators.
        self.creatorLabel = tk.Label(
            self.controlFrame,
            text="Created By: Adam Ettachfini, Sophie Kawi, and Zolbayar Batmunkh",
            font=("Arial", 8),
            wraplength=220,
            justify="left",
        )

        # Put the creator label at the bottom of the left control panel.
        self.creatorLabel.pack(side=tk.BOTTOM, anchor="w", pady=10)

        # Image display area !!!!!!!!!!!!!!!!!!!!!!!!!!!

        # This label is where the image will appear.
        # Before an image is uploaded, it shows default text.
        self.imageLabel = tk.Label(
            self.imageFrame,
            text="Upload an image to begin",
            bg="lightgray",
        )

        # Place the image label in the right frame.
        # expand=True lets it sit nicely in the available space.
        self.imageLabel.pack(expand=True)

    # This function runs when the user clicks "Upload Image".
    def uploadImage(self):
        # Open a file picker window.
        # The filetypes list limits the visible files to images first,
        # but still allows the user to choose all files if needed.
        filePath = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg *.jpeg *.png"), ("All Files", "*.*")]
        )

        # If the user actually selected a file, filePath will not be empty.
        if filePath:
            # Open the selected image and scale it immediately using the scale function.
            # convert("RGB") makes sure every pixel has Red, Green, and Blue values.
            self.originalImage = imageFuncs.scaleImage(
                Image.open(filePath), 500
            ).convert("RGB")

            # Make a copy of the original image to display/edit.
            # This keeps the original safe in case we want a reset button later.
            self.displayImage = self.originalImage.copy()

            # Display the image in the GUI.
            self.showImage(self.displayImage)

    # This function displays an image in the right-side image area.
    def showImage(self, image):
        # Make a copy so resizing for display does not change the real image data.
        imageCopy = image.copy()

        # Resize the image copy so it fits within a large bounding box.
        # thumbnail keeps the image proportions, so it does not look stretched.
        imageCopy.thumbnail((1200, 800))

        # Convert the Pillow image into a tkinter-compatible image.
        self.photoImage = ImageTk.PhotoImage(imageCopy)

        # Update the image label to show the image instead of text.
        self.imageLabel.config(image=self.photoImage, text="", bg=self.root.cget("bg"))

    # This function runs every time the slider moves.
    # For now, it just prints the value so we can confirm it works.
    def updateSlider(self, value):
        print(f"Slider value: {value}")

    # This function runs when the user clicks "Apply Operation".
    def applyOperation(self):
        # Get the currently selected dropdown option.
        selectedOperation = self.operationChoice.get()

        # Get the current slider value.
        sliderValue = self.blurSlider.get()

        # Print these values to the terminal for testing/debugging.
        print(f"Selected operation: {selectedOperation}")
        print(f"Slider value: {sliderValue}")

        # If no image has been uploaded, stop here.
        # This avoids errors from trying to edit a missing image.
        if self.displayImage is None:
            print("No image uploaded yet.")
            return

        # Placeholder for now:
        # Later, this is where we will call image/matrix functions
        # from functiosn.py depending on the selected operation.
        #
        # Example later:

        if selectedOperation == "Image Compression":
            self.displayImage = imageFuncs.processImage(
                self.originalImage, (sliderValue / 100)
            )
        # elif selectedOperation == "Scalar Addition":
        #     self.displayImage = scalarAddition(self.displayImage, sliderValue)

        # Re-display the current image.
        self.showImage(self.displayImage)


# main() starts the program.
def main():
    # Create the main tkinter window.
    root = tk.Tk()

    # Create our app inside the main window.
    app = ImageMatrixApp(root)

    # Keep the window open and listen for user actions.
    # Without this, the window would open and close immediately.
    root.mainloop()


# This checks whether this file is being run directly.
# If we run "python gooey.py", then main() starts.
# If another file imports gooey.py, the app will not automatically open.
if __name__ == "__main__":
    main()
