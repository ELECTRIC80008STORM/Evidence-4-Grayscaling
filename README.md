## Description

The problem I selected is grayscaling images. Grayscaling involves breaking down each pixel of an image into its RGB values. Once you have these values, you apply a mathematical formula to combine them into a single grayscale value. The formula you choose depends on the type of grayscaling you want to perform.

Nowadays, grayscaling is used for many different purposes, some of which are listed below (Shreenath, 2023):

- **Simplifying images as an intermediate step in image processing**: Complex images can challenge machine learning algorithms. By stripping away color, these algorithms can focus only on the essential features of the image, with the added benefit of smaller file sizes.
- **Printing**: Grayscaling is used to reduce costs while maintaining the original quality of the image.
- **Medical Imaging**: It eliminates sources of distraction, allowing both algorithms and people to focus on the details and structures they are meant to see.
- **Artistic and Aesthetic Reasons**: Grayscaling can be used for artistic purposes because it often looks aesthetically pleasing.

I chose this problem to understand the roots of modern grayscaling and to apply my knowledge of functional programming in a tangible way.


## Models

To apply grayscaling, it is important to first understand how image data is usually stored.

### Color Images

In the case of color images, the channel values of each pixel are stored in a three-dimensional array. These channel values represent the intensity of the colors (typically Red, Green, and Blue) for each pixel. For example, a pixel might have the values `[255, 0, 0]`, which would display as bright red.

### Grayscale Images

For grayscale images, there is no need to store separate channel values for colors. Instead, the intensity (or luminosity) of each pixel is stored in a two-dimensional array. This single value represents the brightness of the pixel, ranging from black to white.

### Conversion Process

To convert a color image to a grayscale image, we can apply a mathematical formula to each set of color channels that define the pixels. This is where the functional programming paradigm shines. By using a function like `map` which lets us apply a function for each item iterated, we can easily apply the formula to each pixel.
This formula combines the red, green, and blue values into a single luminosity value. The formula I’m going to use is the next one:
$\ \text{luminosity} = 0.299 \times R + 0.587 \times G + 0.114 \times B \$.
By applying this formula to each pixel, we transform the three color values into a single luminosity value, resulting in the grayscale version of the image.

More about the implementation is going to be shown in the next section.


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


## Tests

The `tests.py` file contains all of the test cases.
