"""
Grayscale Image Conversion Script

This script reads a color image, converts it to grayscale using the luminosity method,
and then saves the grayscale image and displays both images.
"""

import cv2 as cv
import numpy as np
import os
import time

# Folder paths for the original and grayscale images
originalFolderRoute = "originals/"
grayscaleFolderRoute = "grayscales/"

# List of available example images
availableImages = [
    "japanese-landscape.jpg",
    "ghost-of-tsushima-torii-gate.jpg",
    "rick-and-morty.jpg"
]

# Maximum display size for OpenCV windows
MAX_WIDTH = 1728
MAX_HEIGHT = 972

def luminosityCalculation(pixel):
    """
    Calculates the luminosity of a pixel.

    Parameters:
    pixel (tuple): A tuple representing the BGR values of a pixel.

    Returns:
    int: The grayscale value calculated using the luminosity formula.
    """

    b, g, r = pixel
    
    return int(0.299 * r + 0.587 * g + 0.114 * b)  # Luminosity Mathematical Formula

def grayscaling(imageData):
    """
    Convert a color image to grayscale using a helper function.

    Parameters:
    imageData (numpy.ndarray): A NumPy array representing the color image.

    Returns:
    numpy.ndarray: A NumPy array representing the grayscale image.
    """

    # Extract the size dimensions of the array and unpacks the height and width
    height, width, = imageData.shape[:2]

    # Initialize the grayscale image as a list of lists with list comprehension
    grayscaleImage = [[0 for x in range(width)] for x in range(height)]

    # Apply the luminosity function to each pixel in the image
    for i in range(height):
        grayscaleImage[i] = list(map(luminosityCalculation, imageData[i]))

    # Convert the grayscale image to a NumPy array and return it
    return np.array(grayscaleImage, dtype=np.uint8)

def clearConsole():
    """
    Clears the console screen.

    Parameters:
    None

    Returns:
    None
    """
    
    # Check if the system is Windows or Unix-like and run the appropriate command
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Unix-like (Linux, macOS, etc.)

def checkUserInput(quantityOfOptions):
    """
    Prompt the user to enter a number corresponding to an available option and validate the input.

    Parameters:
    quantityOfOptions (int): The total number of options available.

    Returns:
    int: The validated choice of the user.
    """
    
    while True:
        try:
            choice = int(input("Enter the number of your choice: ")) - 1
            
            if 0 <= choice < quantityOfOptions: # Use chained comparison
                return choice
            else:
                print(f"Invalid choice. Please enter a number between 1 and {quantityOfOptions}.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def menu():
    """
    Display a menu for the user to choose an image.

    Parameters:
    None

    Returns:
    int: The index of the chosen image.
    """

    clearConsole()
    
    # Menu text
    print("You can convert an example image to their grayscale version or convert one of your own!!!\n" +
          "If you choose the latter option, you first need to put your image file (it has to be a jpg, jpeg or png to work)\n" +
          "inside the 'originals' folder.\n")
    time.sleep(5)
    print("IMPORTANT: You can exit both images shown when pressing any key!!!\n")
    print("The grayscale version of the images will be stored in the grayscales folder if it isn't in there yet.")
    time.sleep(5)
    print("Choose an example image to convert to grayscale or convert your own:")
    
    # Simplify listing the options with the enumerate iterator
    for i, imageName in enumerate(availableImages, start = 1):
        print(f"{i}. {imageName}")
    
    print(f"{len(availableImages) + 1}. Use your own image")
    
    return checkUserInput(len(availableImages) + 1)

# Resizing an image using OpenCV
# Reference: LearnOpenCV. (2020, August 25). Image resizing with OpenCV. https://learnopencv.com/image-resizing-with-opencv/
def resizeImage(image, maxWidth, maxHeight):
    """
    Resize the image to fit within the maximum dimensions while maintaining the aspect ratio.

    Parameters:
    image (numpy.ndarray): The image to resize.
    max_width (int): The maximum width.
    max_height (int): The maximum height.

    Returns:
    numpy.ndarray: The resized image.
    """

    height, width = image.shape[:2]
    
    if width > maxWidth or height > maxHeight:
        # Calculate the scaling factor to maintain aspect ratio
        scalingFactor = min(maxWidth / width, maxHeight / height)
        newSize = (int(width * scalingFactor), int(height * scalingFactor))
        return cv.resize(image, newSize, interpolation=cv.INTER_AREA)
    
    return image

# It assumes that if it has three channels and the first pixel is grayscaled, they all are
def isGrayscale(image):
    """
    Check if an image is already grayscaled.

    Parameters:
    image (numpy.ndarray): The image to check.

    Returns:
    bool: True if the image is grayscale, False otherwise.
    """

    # Check if the image has only one channel (already grayscale)
    if len(image.shape) == 2:
        return True
    elif len(image.shape) == 3 and image.shape[2] == 3:
        if (image[0, 0, 0] == image[0, 0, 1] == image[0, 0, 2]): # Check if the three BGR values are equal
            return True
    return False

def main():
    """Main function to execute the script."""

    while True:
        choice = menu()
        if choice < len(availableImages):
            chosenImage = availableImages[choice]
        else:
            clearConsole()

            chosenImage = input("To use your own image after putting it in the 'originals' folder you just have to write its filename here (including the extension): ")
            
            # Check if the user-provided file exists
            if not os.path.exists(originalFolderRoute + chosenImage):
                print(f"The file {chosenImage} does not exist in the 'originals' folder.")
                time.sleep(5)
                continue
            
            # Extract the file extension
            _, fileExtension = os.path.splitext(chosenImage)
            
            if not (fileExtension == ".jpg" or fileExtension == ".jpeg" or fileExtension == ".png"):
                print("Invalid file extension. Only files with a .jpg, .jpeg, or .png extension are accepted.")
                time.sleep(5)
                continue
        
        # Read the chosen image
        img = cv.imread(cv.samples.findFile(originalFolderRoute + chosenImage))

        # Check if the image was read successfully
        if img is None:
            print("Could not read the image. Please try again.")
            time.sleep(3)
            clearConsole()
            continue

        # Check if the image is already grayscale
        if isGrayscale(img):
            print(f"The image {chosenImage} is already grayscaled. Process will be skipped.")
            time.sleep(5)
            continue

        # Extract the file extension
        fileName, fileExtension = os.path.splitext(chosenImage)

        # Convert the image to grayscale
        grayscaleImageFormated = grayscaling(img)

        # Construct the path for the grayscale image
        grayscaleImagePath = f"{grayscaleFolderRoute}{fileName}-grayscale{fileExtension}"

        # Check if the grayscale image already exists
        if os.path.exists(grayscaleImagePath):
            overwrite = input(f"The file {grayscaleImagePath} already exists. Do you want to overwrite it? (y/n): ")
            if overwrite.lower() != 'y':
                print("Skipping the save operation. Displaying the images.")
                time.sleep(4)
                imgResized = resizeImage(img, MAX_WIDTH, MAX_HEIGHT)
                grayscaleImageResized = resizeImage(grayscaleImageFormated, MAX_WIDTH, MAX_HEIGHT)
                cv.imshow("Original Image", imgResized)
                cv.imshow("Grayscale Image", grayscaleImageResized)
                cv.waitKey(0)
                cv.destroyAllWindows()
                # Ask the user if they want to convert another image
                another = input("Do you want to convert another image? (y/n): ")
                if another.lower() != 'y':
                    break
                else:
                    continue    
        
        # Save and display the grayscale image
        time.sleep(4)
        cv.imwrite(grayscaleImagePath, grayscaleImageFormated)
        imgResized = resizeImage(img, MAX_WIDTH, MAX_HEIGHT)
        grayscaleImageResized = resizeImage(grayscaleImageFormated, MAX_WIDTH, MAX_HEIGHT)
        cv.imshow("Original Image", imgResized)
        cv.imshow("Grayscale Image", grayscaleImageResized)
        cv.waitKey(0)
        cv.destroyAllWindows()

        # Ask the user if they want to convert another image
        another = input("Do you want to convert another image? (y/n): ")
        if another.lower() != 'y':
            break

# Detect if the script is being run directly and call main function
if __name__ == "__main__":
    main()
