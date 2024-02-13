# Image Processing with the Python Imaging Library

In this exercise, you will learn how to process images using Python. You will be working with the Python Imaging Library (PIL), which provides you various image editing capabilities.

## Objective

Your task is to write a Python script that splits JPEG and PNG image files vertically into two pieces. The images are located in a specified input directory, and the split images should be saved in a specified output directory. The split position sould be defined as a fraction (some value between 0 and 1).

## Steps

- **Setup your environment**: Install the `pillow` (formerly known as PIL) libraries with pip.
  - In the *Explorer view*: Right click on the `group_1` directory > Open in Integrated Terminal
  - In the *Terminal view*: Type `pip install pillow`

- **Create a new Python file**: Create a new Python file named `script.py`.
  - In the *Explorer view*: Right click on the `group_2` directory > New File...

- **Import necessary libraries**: At the top of your file, import the necessary libraries:
```python
from PIL import Image
from math import floor
```

- **Define configuration variables**: Underneath the import statements define the following variables:
```python
INPUT_DIRECTORY = 'images/input'
OUTPUT_DIRECTORY = 'images/output'
SPLIT_POSITION = 0.5
```

- **Define your function**: Define a function named `split_images_vertically` that takes three parameters: `input_directory`, `output_directory`, and `split_position`. This function should do the following:
  - Sanity checks
    - Check if the input directory exists
      - If not, print an error message and return
    - Check if the output directory exists
      - If not, create the output directory
    - Check if the output directory is empty
      - If not, print an error message and return
  - Find all supported images (JPEG and PNG) in the input directory
    - Create a list to store the image file names that should be processed
    - Loop over all files in the input directory
    - Skip files that are not supported (you can use the file extension for that: .jpg, .png)
    - Add supported images to a list
    - Print a message if no processable images were found
  - Process the images
    - Loop over all images in the list
    - Load the image as PIL Image
    - Get the width and height of the image
    - Calculate the split position in pixels
    - Split the image vertically
    - Save the splitted images
    - Close the image

- **Call your function**: At the end of your script, call your function with the configuration variables as arguments.

- **Run your script**: Execute your script.
  - In the *Terminal view*: Type `python script.py`

## Expected Outcome

After running your script, you should see the split images in your specified output directory.

## Hints

- To check if directories exist, take a look in the Python built in `os.path` module
- To construct a path to a file, you can use string concatenation.
- To load an image, take a look at the `Image` module from the Pillow (PIL) library.
- There is no dedicated image splitting function in PIL. Instead, two image sections must be cut out of the image individually. Have a look at PIL's `crop()` method.
- The split position in pixels can be calculated with this formula: imageWidth * split_position
  - make sure that you **round the result**, there are no half pixels
- To save an image, use the `save()` method of a PIL Image object.
- To close an image, use the `close()` method of a PIL Image object.

<hr>

Remember, the goal is to understand how to manipulate images using Python. Don't worry if you don't get it right the first time. Keep trying and happy coding!
