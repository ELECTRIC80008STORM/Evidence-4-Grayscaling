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


## Analysis

As I explained before, I used a functional paradigm to perform the grayscaling operations on the image pixels. However, due to the large number of pixels some images have, the process isn’t as efficient as it could be. Using a parallel paradigm alongside the functional one would allow the computer to split the operations and distribute the workload, resulting in a more efficient process. The only downside would be a slight increase in the complexity of the code.

### Procedural / Imperative Paradigm

The problem could have been solved by using this paradigm. In it, you directly define the steps the computer needs to follow to achieve the desired result. Using this approach, the implementation of the mathematical formula for grayscaling could be done with iterations using loops. While focusing solely on grayscaling, there wouldn't be much difference between this and the functional paradigm. However, the functional paradigm offers the advantage of modularity. To change the filter or operations applied to the image, you would only need to create and use a new function with the desired filter. This approach avoids modifying existing code and allows multiple functions to be used as needed, providing greater flexibility and reusability compared to having a single piece of code modified for each specific filter.

An example of the implementation with this paradigm is shown below:

```python
def grayscaling(imageData):
    height, width = imageData.shape[:2]
    grayscaleImage = [[0 for x in range(width)] for x in range(height)]
    for i in range(height):
        for j in range(width):
            b, g, r = imageData[i, j]  # Access the pixel and unpack it
            grayscaleValue = int(0.299 * r + 0.587 * g + 0.114 * b)
            grayscaleImage[i, j] = grayscaleValue
    return np.array(grayscaleImage, dtype=np.uint8)
```

### Time Complexity

Most of the functions in my code are aimed at enhancing the user experience rather than directly performing the grayscaling. However, it is essential to analyze the time complexity of all functions to determine the general time complexity of the application.

- **luminosityCalculation(pixel)**: This function applies the luminosity formula to the three channels inside the pixel it receives and returns the value. The number of channels never increases nor do the channel values go above 255. Therefore, its time complexity is the same for all cases:
  - **Time Complexity:**
    - Ω(1)
    - Θ(1)
    - O(1)

- **grayscaling(imageData)**: This function performs four operations:
  1. Extracts dimensions: Accessing an attribute of the array, which is _O(1)_.
  2. Creates the grayscale array: Using list comprehension, it has a time complexity of _O(nm)_, where n and m are the height and width.
  3. Applies the luminosity function: Using the previously explained function on every pixel, it has a complexity of _O(nm)_.
  4. Converts the array to a NumPy array: This operation also has a complexity of _O(nm)_, depending on the size of the array being copied.
  - **Time Complexity:**
    - Ω(nm)
    - Θ(nm)
    - O(nm)

- **clearConsole()**: This function only clears the console screen, as it was probably expected.
  - **Time Complexity:**
    - Ω(1)
    - Θ(1)
    - O(1)

- **checkUserInput(quantityOfOptions)**: This function checks the user input and ensures it is acceptable by trapping the user in a while loop until the input is considered valid.
  - **Time Complexity:**
    - Ω(1): In the best case, where the user enters a valid number immediately.
    - Θ(n): In the average case, where the user enters an invalid number.
    - O(n): In the worst case, where the user enters several invalid numbers.

- **menu()**: This function displays the menu for the user and lists the available options. The number of operations depends on the number of example images, _n_.
  - **Time Complexity:**
    - Ω(n)
    - Θ(n)
    - O(n)

- **resizeImage(image, maxWidth, maxHeight)**: This function resizes the image while maintaining the aspect ratio, ensuring it fits within most users’ screens. It performs the following steps:
  1. Extracts dimensions: As mentioned before, it has a complexity of _O(1)_.
  2. Calculates the scaling factor: Done through a simple operation, it has a complexity of _O(1)_.
  3. Resizes the image: Using OpenCV's `resize` function, it has a complexity of _O(nm)_.
  - **Time Complexity:**
    - Ω(nm)
    - Θ(nm)
    - O(nm)

- **isGrayscale(image)**: This function determines if the image is already grayscaled by checking the dimensions of the image array or if all channels in the first pixel have the same value.
  - **Time Complexity:**
    - Ω(1)
    - Θ(1)
    - O(1)

- **main()**: This function contains the core functionality, including the menu. It allows the user to choose between using an example image or an image added to the folder. Depending on the scenario, it either creates a new grayscale image or displays the existing one. The worst time complexities of the functions and methods used here are given by the image dimensions.
  - **Time Complexity:**
    - Ω(nm)
    - Θ(nm)
    - O(nm)

With this, we obtained that the general complexity for our app, in any case, is going to be of _Θ(nm)_, where _n_ and _m_ are the length of the dimensions of the image array.

