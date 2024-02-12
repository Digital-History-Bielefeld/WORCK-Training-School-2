# (1) import clean_text
# (2) from clean_text import clean
from clean_text import clean as cl
import random
from colorama import init, Fore

# (5) 
init(autoreset=True)

my_text = '''
THIS iS               
  a TEST  
      strIng
   !
'''

# (1) clean_text.clean(my_text)
# (2) clean(my_text)
cl(my_text)

##########################################################################################################################################################################################


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

# Creates a random int with the random.randint(a,b) function
random_int =  random.randint(1,10)
# Calls the function guess_the_number with your random_int
guess_the_number(random_int)

##########################################################################################################################################################################################


# Type into your terminal: pip install colorama


def greet_user():
    greeting = Fore.GREEN + "Hello and welcome to our python workshop!"
    print(greeting)


greet_user()

