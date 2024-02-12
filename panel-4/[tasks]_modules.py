my_text = '''
THIS iS               
  a TEST  
      strIng
   !
'''

# (1) 
# You have this text and it has some problems. You remember that you recently wrote a function that does exactly what you need. So that you don't have to write it again, you can now simply import it from your files.
# The function you need is called clean and it is in a file called clean_text.py. You can find it in the same directory as this file. 

# Add the following to the head of your file (above "my_text"):
# import clean_text
# Then, use the function clean_text.clean() below this comment to clean the text and print the result. Note: the clean function takes a string as input and returns the preprocessed string.


# (2)
# You can also import the clean function directly from the file. This way you don't have to use the module name when calling the function.
# Add the following to the head of your file:
# from clean_text import clean
# Then, use the function clean below this comment to clean the text and print the result. Note: the clean function takes a string as input and returns the preprocessed string.


# (3)
# You can also import the clean function directly from the file and rename it.
# Add the following to the head of your file:
# from clean_text import clean as cl
# Then, use the function cl below this comment to clean the text and print the result.
# Note: This task is more useful for when you have a long function name and you want to use a shorter name.


##########################################################################################################################################################################################

# (4)
# Now you have practiced how to work with your own modules and import them. Of course, you can also import modules that you have not written yourself.
# Python comes with a rich standard library, which includes a wide range of modules and packages. You can find information about the standard library in the official Python documentation: https://docs.python.org/3/library/.
# A famous module is "random", which returns a randomized number: https://docs.python.org/3/library/random.html

# Below you have a little function "guess_the_game". It takes a random number as a parameter and the player have to type in a guess.
# If the guess is right, the game ends. Else the player gets a hint, if the number is too low or too high.
# For this you should pass a random number with the "random" module of Python. 
# a) Import the module at the top of the header: `import random`. You can simply write it under the other module.
# b) To create any number between 1 and 10, use the function .randint() of random: `random.randint(a, b)` where a is 1 and b = 10. Store the result in a variable.
# c) Call the function guess_the_number with your created variable as a parameter.


def guess_the_number(random_number):
    guessed_number = 0
    
    print("Welcome to Guess the Number Game!")
    
    while guessed_number != random_number:
        # Ask the user to guess the number
      guessed_number = input("Enter your guess (between 1 and 10): ")
      guessed_number = int(guessed_number)
        
      if guessed_number == random_number:
         print(f"Congratulations!")
      elif guessed_number < random_number:
         print("Too low! Try again.")
      else:
         print("Too high! Try again.")


##########################################################################################################################################################################################

# (5)
# In addition to the Python Standard Library, there are also external libraries. PyPI is a website that provides such projects created by the community: https://pypi.org
# You can then install these libraries on your system, e.g. with `pip`
# In addition to the Python Standard Library, there are also external libraries. PyPI is a website that provides such projects created by the community. You can then install these libraries on your system, e.g. with `pip`. 

# For this task, we will install the "colorama" library as an example: https://pypi.org/project/colorama/. This library colors text in the console output. This is not very useful, but a nice little project to show how importing external libraries works.

# a) Install colorama. You can find out how to do this in the documentation.
# Hint: You have to use your terminal below to install libraries. It always starts with `python - m pip [library name]`. In many cases it is also sufficient if you only enter `pip install [library name]`.
# b) In our case, we only want the init and Fore modules. Accordingly, you can import the modules "init, Fore" in the header. Remember: the notation is `from [library] import [modules]`.
# c) Initialize colorama to activate the colors in the console. For this you just need to write "init()" (https://github.com/tartley/colorama?tab=readme-ov-file#usage). Write it below the import statements. 
# d) Write the function "greet_user()". Create a variable "greeting" inside. You want to change the color of the terminal text: https://github.com/tartley/colorama?tab=readme-ov-file#usage. 
# So type in `Fore.GREEN` (you can also use one of the other colors) + the string "Hello and welcome to our python workshop!"
# e) Print greetings (as a part of the function)
# f) Call  greet_user below. 
