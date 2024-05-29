## Description

The problem I selected is grayscaling images. Grayscaling involves breaking down each pixel of an image into its RGB values. Once you have these values, you apply a mathematical formula to combine them into a single grayscale value. The formula you choose depends on the type of grayscaling you want to perform.

Nowadays, grayscaling is used for many different purposes, some of which are listed below (Shreenath, 2023):

- **Simplifying images as an intermediate step in image processing**: Complex images can challenge machine learning algorithms. By stripping away color, these algorithms can focus only on the essential features of the image, with the added benefit of smaller file sizes.
- **Printing**: Grayscaling is used to reduce costs while maintaining the original quality of the image.
- **Medical Imaging**: It eliminates sources of distraction, allowing both algorithms and people to focus on the details and structures they are meant to see.
- **Artistic and Aesthetic Reasons**: Grayscaling can be used for artistic purposes because it often looks aesthetically pleasing.

I chose this problem to understand the roots of modern grayscaling and to apply my knowledge of functional programming in a tangible way.


## Models

To apply grayscaling, it is important to first understand how image data is usually stored. The inspiration for the diagrams was taken from Bharmal M. 's (2023) medium article about Gray Scaling with the Algorithms.

### Color Images

In the case of color images, the channel values of each pixel are stored in a three-dimensional array. These channel values represent the intensity of the colors (typically Red, Green, and Blue) for each pixel. For example, a pixel might have the values `[255, 0, 0]`, which would display as bright red.

To understand this better, consider Figure 1, which illustrates the three color channels (Red, Green, Blue) of a color image. Each pixel in the image has three values corresponding to these channels.

![Color Image Channels](https://github.com/ELECTRIC80008STORM/Evidence-4-Grayscaling/blob/main/Color%20Image%20Data%20Representation%20Diagram.png)

*Figure 1: Color Image Channels (adapted from Harmal, 2023)*

### Grayscale Images

For grayscale images, there is no need to store separate channel values for colors. Instead, the intensity (or luminosity) of each pixel is stored in a two-dimensional array. This single value represents the brightness of the pixel, ranging from black to white.

To understand this better, consider Figure 2, which illustrates the single channel of a grayscale image. Each pixel in the image has one value representing the intensity of the gray color.

![Grayscale Image Channels](https://github.com/ELECTRIC80008STORM/Evidence-4-Grayscaling/blob/main/Grayscale%20Image%20Data%20Representation%20Diagram.png)

*Figure 2: Grayscale Image Channels*

### Conversion Process

To convert a color image to a grayscale image, we can apply a mathematical formula to each set of color channels that define the pixels. This is where the functional programming paradigm shines. By using a function like `map` which lets us apply a function for each item iterated, we can easily apply the formula to each pixel.
This formula combines the red, green, and blue values into a single luminosity value. The formula I’m going to use is the next one (_with the result being truncated to stored it as an integer_):
$\ \text{luminosity} = 0.299 \times R + 0.587 \times G + 0.114 \times B \$.
By applying this formula to each pixel, we transform the three color values into a single luminosity value, resulting in the grayscale version of the image.

As an example we can consider the first and last pixel in _Figure 1_. Which would be converted to their luminosity value through the function mentioned before, these new calculated values are shown in _Figure 2_. 

Here is the example of how the function applied to each pixel would help us obtained the luminosity values:

**Pixel A:**
$\ 0.299 \times 244 + 0.587 \times 3 + 0.114 \times 5 = 75.287 \rightarrow 75 \$

**Pixel B:**
$\ 0.299 \times 0 + 0.587 \times 53 + 0.114 \times 72 = 39.319 \rightarrow 39 \$

Now, applying this to each pixel would help us transform the original image matrix into the grayscale two dimensional matrix with the correct values.

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
