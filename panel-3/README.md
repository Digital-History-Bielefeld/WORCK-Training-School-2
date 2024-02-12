# Panel 3: Python Basics I.2

### Dictionaries

A dictionary is a collection which is unordered, changeable, and indexed. In Python dictionaries are written with curly brackets, and they have keys and values. You can access the items of a dictionary by referring to its key name, inside square brackets.

```python
# Dictionary
person = {
  "name": "Inga",
  "language": "python",
  "country": "Germany"
}
print(person) # Output: {'name': 'Inga', 'language': 'python', 'country': 'Germany'}
```

You have many possibilities to work with dictionaries. You can add, remove, or change elements. 

```python
# Add an item to a dictionary
person["age"] = 25
print(person) # Output: {'name': 'Inga', 'language': 'python', 'country': 'Germany', 'age': 27}
 
# Remove an item from a dictionary
person.pop("age")
print(person) # Output: {'name': 'Inga', 'language': 'python', 'country': 'Germany'}

# Change an item in a dictionary
person["country"] = "USA"
print(person) # Output: {'name': 'Inga', 'language': 'python', 'country': 'USA'}

# Get the value of a specific key
print(person["name"]) # Output: Inga

# Get all keys of a dictionary
print(person.keys()) # Output: dict_keys(['name', 'language', 'country'])

# Get all values of a dictionary
print(person.values()) # Output: dict_values(['Inga', 'python', 'USA'])

# Get all items of a dictionary
print(person.items()) # Output: dict_items([('name', 'Inga'), ('language', 'python'), ('country', 'USA')])

# Check if a key exists in a dictionary
if "name" in person:
  print("Yes, 'name' is one of the keys in the person dictionary")

# Or more specific
if "name" in person.keys():
  print("Yes, 'name' is one of the keys in the person dictionary")

if "python" in person.values():
  print("Yes, 'python' is one of the values in the person dictionary")


```



### Flow Control

Flow control statements are used to control the flow of execution in a program. At many points in your program, you may want to make a decision about which block of code to execute next. You can do this with flow control statements. For this you need comparison operators and especially boolean values.

#### Comparison Operators

| Operator | Meaning                  |
| -------- | ------------------------  |
| ==       | Equal                    |
| !=       | Not equal                |
| >        | Greater than             |
| <        | Less than                |
| >=       | Greater than or equal to |
| <=       | Less than or equal to    |

#### Boolean operators

| Operator | Meaning                  |
| -------- | ------------------------  |
| and      | Logical and               |
| or       | Logical or                |
| not      | Logical not               |

**The and operator's truth table:**

| Expression | Evaluates to |
| ---------- | ------------ |
| True and True | True |
| True and False | False |
| False and True | False |
| False and False | False |

**The or operator's truth table:**

| Expression | Evaluates to |
| ---------- | ------------ |
| True or True | True |
| True or False | True |
| False or True | True |
| False or False | False |

**The not operator's truth table:**

| Expression | Evaluates to |
| ---------- | ------------ |
| not True | False |
| not False | True |



#### If-Elif-Else Statements
**if-statement**: The `if` statement is used to check a condition. If the condition is true, a block of code will be executed. If the condition is false, the block of code will be skipped.

```python
if 5 > 2:
  print("Five is greater than two!")
```

**else-statement**: The `else` statement is used to execute a block of code if the condition is false.

```python
if 5 < 2:
  print("Five is less than two!")
else:
  print("Five is not less than two!")
```

**elif-statement**: The `elif` statement is used to check multiple conditions. If the condition is true, the block of code will be executed. If the condition is false, the next condition will be checked.

```python
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
```

#### While Loops
A `while` loop is used to execute a block of code as long as a condition is true.

```python
i = 1
while i < 6:
  print(i)
  i += 1
```

#### For Loops
A `for` loop is used to iterate over a sequence (list, tuple, dictionary, set, or string).

```python
for i in range(6): 
  print(i)

# range() is a built-in function that returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
```

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(x)
```

### Strings

Strings are sequences of characters. You can use strings to represent text data. Strings in Python are surrounded by either single quotation marks, or double quotation marks.

```python
# Single quotation marks
print('Hello')

# Double quotation marks
print("Hello")
```

You have many possibilities to work with strings. You can add, remove, or change elements. 

```python
# String
a = "Hello, World!"

# Get the character at position 1
print(a[1]) # Output: e

# Substring. Get the characters from position 2 to position 5 (not included)
print(a[2:5]) # Output: llo

# The strip() method removes any whitespace from the beginning or the end
b = " Hello, World! "
print(b.strip()) # Output: Hello, World!
print(b.lstrip()) # Output: Hello, World!
print(b.rstrip()) # Output:  Hello, World!

# The lower() method returns the string in lower case
print(a.lower()) # Output: hello, world!

# The upper() method returns the string in upper case
print(a.upper()) # Output: HELLO, WORLD!

# The replace() method replaces a string with another string
print(a.replace("H", "J")) # Output: Jello, World!

# The split() method splits the string into substrings if it finds instances of the separator
print(a.split(",")) # Output: ['Hello', ' World!']

# The len() method returns the length of a string
print(len(a)) # Output: 13

# The in operator checks if a substring is present in a string
print("Hello" in a) # Output: True

# The not in operator checks if a substring is not present in a string
print("Hello" not in a) # Output: False

# You can use the + operator to concatenate two strings
a = "Hello"
b = "World"
c = a + b
print(c) # Output: HelloWorld

# You can also use the string interpolation to concatenate two strings
c = "%s to the %s" % (a, b) 
print(c) # Output: Hello to the World

# You can also use f-strings to concatenate two strings. This is the most modern way to do it.
c = f"{a} to the {b}"
print(c) # Output: Hello to the World

# If you have a list of strings, you can concatenate them with the join() method
fruits = ["apple", "banana", "cherry"]
print(", ".join(fruits)) # Output: apple, banana, cherry

# To escape a character, you can use the backslash
print("We are the so-called \"Vikings\" from the north.") # Output: We are the so-called "Vikings" from the north.

```
