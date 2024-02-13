# Import necessary libraries
''' Your code here'''


# Define configuration variables
''' Your code here'''


# A function to perform OCR on images.
# Hint: `some_function()` is just a placeholder, change it according to the README.md
#       and don't forget to specify it's parameters.
def some_function():
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
    ''' Your code here'''

    ##########################################################################
    # Find all supported images (JPEG and PNG) in the input directory        #
    # - Create a list to store the image file names that should be processed #
    # - Loop over all files in the input directory                           #
    # - Skip files that are not supported                                    #
    #   (you can use the file extension for that: .jpg, .png)                #
    # - Add supported images to the list                                     #
    # - Print a message if no processable images were found                  #
    ##########################################################################
    ''' Your code here'''

    ##########################################################################
    # Process the images                                                     #
    # - Loop over all images in the list                                     #
    # - Load the image as PIL Image                                          #
    # - Perform OCR using pytesseract and get the result as a string         #
    # - Save the result as a txt file                                        #
    # - Close the image                                                      #
    ##########################################################################
    ''' Your code here'''


# Call the function
''' Your code here '''
