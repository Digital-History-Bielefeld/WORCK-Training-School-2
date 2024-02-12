# Import necessary libraries
from math import floor
from PIL import Image
import os


# Define configuration variables
INPUT_DIRECTORY = 'images/input'
OUTPUT_DIRECTORY = 'images/output'
SPLIT_POSITION = 0.5


# A function to split images vertically.
def split_images_vertically(input_directory, output_directory, split_position):
    ##########################################################################
    # Sanity checks:                                                         #
    # - Check if the input directory exists                                  #
    #   - If not, print an error message and return                          #
    # - Check if the output directory exists                                 #
    #   - If not, create the output directory                                #
    # - Check if the output directory is empty                               #
    #   - If not, print an error message and return                          #
    # - Check if the language is supported                                   #
    #   - If not, print an error message and return                          #
    ##########################################################################
    # Check if the input directory exists
    if not os.path.exists(input_directory):
        # Print an error message and return
        print('Input directory "' + input_directory + '" does not exist!')
        return

    # Check if the output directory exists
    if not os.path.exists(output_directory):
        # Create the output directory
        os.makedirs(output_directory)

    # Check if the output directory is empty
    if len(os.listdir(output_directory)) != 0:
        # Print an error message and return
        print('Output directory "' + output_directory + '" is not empty!')
        return

    ##########################################################################
    # Find all supported images (JPEG and PNG) in the input directory        #
    # - Create a list to store the image file names that should be processed #
    # - Loop over all files in the input directory                           #
    # - Skip files that are not supported                                    #
    #   (you can use the file extension for that: .jpg, .png)                #
    # - Add supported images to the list                                     #
    # - Print a message if no processable images were found                  #
    ##########################################################################
    # Create a list to store the image file names that should be processed
    images_to_process = []

    # Loop over all files in the input directory
    for image_filename in os.listdir(input_directory):
        # Skip files that are not supported
        if not image_filename.endswith(('.jpg', '.png')):
            continue

        # Add supported images to the list
        images_to_process.append(image_filename)

    # Alternatively, we can use a list comprehension to do the same thing
    # images_to_process = [
    #     image_filename for image_filename
    #     in os.listdir(input_directory)
    #     if image_filename.endswith(('.jpg', '.png'))
    # ]

    # Print a message if no processable images were found and return
    if len(images_to_process) == 0:
        print('No images to process!')
        return

    ##########################################################################
    # Process the images                                                     #
    # - Loop over all images in the list                                     #
    # - Load the image as PIL Image                                          #
    # - Get the width and height of the image                                #
    # - Calculate the split position in pixels                               #
    # - Split the image vertically                                           #
    # - Save the splitted images                                             #
    # - Close the image                                                      #
    ##########################################################################
    # Loop over all images in the list
    for image_filename in images_to_process:
        # Load the image as PIL Image
        image_path = input_directory + '/' + image_filename
        image = Image.open(image_path)

        # Get the width and height of the image
        width = image.width
        height = image.height

        # Calculate the split position in pixels
        split_position_in_px = floor(width * split_position)

        # Split the image vertically
        left_image = image.crop((0, 0, split_position_in_px, height))
        right_image = image.crop((split_position_in_px, 0, width, height))

        # Save the splitted images
        left_image_path = output_directory + '/' + 'left_' + image_filename
        left_image.save(left_image_path)

        right_image_path = output_directory + '/' + 'right_' + image_filename
        right_image.save(right_image_path)

        # Close the image
        image.close()


# Call the function
split_images_vertically(INPUT_DIRECTORY, OUTPUT_DIRECTORY, SPLIT_POSITION)
