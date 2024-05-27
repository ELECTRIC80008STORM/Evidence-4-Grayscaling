## Description

The problem I selected is grayscaling images. Grayscaling involves breaking down each pixel of an image into its RGB values. Once you have these values, you apply a mathematical formula to combine them into a single grayscale value. The formula you choose depends on the type of grayscaling you want to perform.

Nowadays, grayscaling is used for many different purposes, some of which are listed below (Shreenath, 2023):

- **Simplifying images as an intermediate step in image processing**: Complex images can challenge machine learning algorithms. By stripping away color, these algorithms can focus only on the essential features of the image, with the added benefit of smaller file sizes.
- **Printing**: Grayscaling is used to reduce costs while maintaining the original quality of the image.
- **Medical Imaging**: It eliminates sources of distraction, allowing both algorithms and people to focus on the details and structures they are meant to see.
- **Artistic and Aesthetic Reasons**: Grayscaling can be used for artistic purposes because it often looks aesthetically pleasing.

I chose this problem to understand the roots of modern grayscaling and to apply my knowledge of functional programming in a tangible way.


## Models

*The diagram will be added in a future*


## Implementation

The solution was implemented in Python 3 with the help of four Python modules, two of which are OpenCV and NumPy. These modules need to be installed before running the code.

**OpenCV**: This module is used to read, display, and save the images the app handles.
- It can be installed in Ubuntu with the following command:
  ```bash
  $ sudo apt-get install python3-opencv
  ```
- Here is a guide to install it on other operating systems: [Guide](https://docs.opencv.org/4.x/da/df6/tutorial_py_table_of_contents_setup.html)

**NumPy**: This module is used to create the array where the modified image data is stored.
- It can be installed in Ubuntu with the following command:
  ```bash
  $ sudo apt install python3-numpy
  ```
- Here is a guide to install it on other operating systems: [Guide](https://numpy.org/install/)

Once these modules are installed, you can use the grayscaling app (through the `grayscaling.py` file) with the provided examples or add your own as the app explains.
