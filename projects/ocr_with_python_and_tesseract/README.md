# Optical Character Recognition with Python and Tesseract-OCR

In this exercise, you will learn how to process images using Python and Tesseract. Tesseract is a flexible Optical Character Recognition (OCR) software for various operating systems.

## Objective

Your task is to write a Python script that can perform OCR on JPEG and PNG image files. It should scan an input directory for supported images, perform OCR using [pytesseract](https://pypi.org/project/pytesseract), and save the results as text files (one per image) in an output directory.

## Steps

- **Install Tesseract-OCR system package**: Use the `install-tesseract-ocr.sh` script provided within the `group_2` directory:
  - In the *Explorer view*: Right click on the `group_2` directory > Open in Integrated Terminal
  - In the *Terminal view*: Type `./install-tesseract-ocr.sh`
  - Don't close the *Terminal view* you will need it again ;)

- **Setup your environment**: Install the `pytesseract` and `pillow` (formerly known as PIL) libraries with pip.
  - In the *Terminal view*: Type `pip install pillow pytesseract`

- **Create a new Python file**: Create a new Python file named `script.py`.
  - In the *Explorer view*: Right click on the `group_2` directory > New File...

- **Import necessary libraries**: At the top of your file, import the necessary libraries:
```python
from PIL import Image
import os
import pytesseract
```

- **Define configuration variables**: Underneath the import statements define the following variables:
```python
INPUT_DIRECTORY = 'images/input'
OUTPUT_DIRECTORY = 'images/output'
LANGUAGE = 'eng'
```

- **Define your function**: Define a function named `ocr_with_tesseract` that takes three parameters: `input_directory`, `output_directory`, and `language`. This function should do the following:
  - Sanity checks
    - Check if the input directory exists
      - If not, print an error message and return
    - Check if the output directory exists
      - If not, create the output directory
    - Check if the output directory is empty
      - If not, print an error message and return
    - Check if the language is available with pytesseract
      - If not, print an error message and return
  - Find all supported images (JPEG and PNG) in the input directory
    - Create a list to store the image file names that should be processed
    - Loop over all files in the input directory
    - Skip files that are not supported (you can use the file extension for that: .jpg, .png)
    - Add supported images to the list
    - Print a message if no processable images were found
  - Process the images
    - Loop over all images in the list
    - Load the image as PIL Image
    - Perform OCR using pytesseract and get the result as a string
    - Save the result as a txt file
    - Close the image

- **Call your function**: At the end of your script, call your function with the configuration variables as arguments.

- **Run your script**: Execute your script.
  - In the *Terminal view*: Type `python script.py`

## Expected Outcome

After running your script, you should see the extracted text and pdf files in your specified output directory.

## Hints

- To check if directories exist, take a look in the Python built in `os.path` module
- To construct a path to a file, you can use string concatenation.
- To load an image, take a look at the `Image` module from the Pillow (PIL) library.
- To extract text from an image using pytesseract, you can use its `image_to_string()` method.
- To save the results you should use the Python built in `open` function in conjunction with the `with` keyword.
  - The file handle can be used to `write()` something in the file

<hr>

Remember, the goal is to understand how to manipulate images and extract text from them using Python and Tesseract. Don't worry if you don't get it right the first time. Keep trying and happy coding!
