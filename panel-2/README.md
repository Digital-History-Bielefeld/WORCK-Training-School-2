# Panel 2: Python Basics I.1

### Basic vocabulary

Before we start with the first Python program, we should clarify some basic terms. These are the basic vocabulary of Python:

- **Expression**: An expression is a combination of values, variables, operators, and calls to functions. Expressions need to be evaluated. In the example above, `number_1 + number_2` is an expression.
- **Value**: A value is one of the basic things a program works with. For example, the strings `"Hello, i am a Python program that adds to numbers."`, `"The first number is: "`, `"The second number is: "`, and `"The sum is: "` are all values.
- **Variable**: A variable is a container for a value. It can be used to store data. In the example above, `number_1` and `number_2` are variables. 
- **Operator**: An operator is a special symbol that represents a simple computation like addition, multiplication, or string concatenation. In the example above, `+` is an operator.
- **Data type**: A data type is a category for values, and every value belongs to exactly one data type. In the example above, the data type of `number_1` and `number_2` is an integer, the data type of the strings is a string.

### Errors

When you write a program, you will make errors. Errors can be of different types. The most common types of errors are:
- **Syntax errors**: These are errors where the parser finds an incorrect statement. It will not execute the code. These are errors you will get when you make a typo or forget to add a closing bracket, for example.
- **Runtime errors**: These are errors that happen when the program is running. These are also called exceptions. These are errors you will get when you try to access a variable that is not defined, for example.
- **Semantic errors**: These are errors in logic. These are errors you will get when you write a program that is syntactically correct and runs, but does not do what you intended it to do.

Errors are normal and they are a part of the learning process. You should not be afraid of making errors. You should read the error messages carefully and try to understand what they are telling you. This is the best way to learn from it. So no worries!


### Variables
You can store values in variables with an **assignment statement**. An assignment statement consists of a variable name, an equal sign (called the assignment operator), and the value to be stored. If you want to store the value `10` in the variable `number_1`, you can do this with the following code:

```python
number_1 = 10
```
You can overwrite the value of a variable by assigning a new value to it. If you want to store the value `20` in the variable `number_1`, you can do this with the following code:

```python
number_1 = 10
print(number_1) # Output: 10
number_1 = 20
print(number_1) # Output: 20
```

The naming of a variable is very important. You should always choose a name that describes the content of the variable. The name of a variable can contain letters, numbers, and underscores. It must start with a letter or an underscore. It is case-sensitive, so `number_1` and `Number_1` are two different variables.

```python
Number_1 = 10
print(number_1) # Output: 10
number_1 = 20
print(Number_1) # Output: 10
```

You can work with variables as you would with values. You can use them in expressions, and you can pass them to functions. In the example above, we used the variables `number_1` and `number_2` in the expression `number_1 + number_2`.

### Data types

- **Integers**: Integers (ints) are whole numbers. In the example above, `10` and `20` are integers.
- **Floating-point numbers**: Floating-point numbers (floats) are numbers with a decimal point. For example, `1.43` and `10.0` are floats.
- **Strings**: Strings (str) are sequences of characters. In the example above, `"Hello, i am a Python program that adds to numbers."`, `"The first number is: "`, `"The second number is: "`, and `"The sum is: "` are all strings.
- **Booleans**: Booleans (bools) are either `True` or `False`. In the example above, `True` and `False` are booleans.

### Operators


| Operator | Operation                         | Example   | Result |
| -------- | --------------------------------- | --------- | ------ |
| +        | Addition                          | `2 + 2`   | `4`    |
| -        | Substraction                      | `5 - 2`   | `3`    |
| *        | Multiplication                    | `5 * 2`   | `10`   |
| /        | Division                          | `14 / 4`  | `3.5`  |
| //       | Integer division/floored quotient | `14 // 4` | `3`    |
| %        | Modulus                           | `25 % 7`  | `4`    |
| **       | Exponent                          | `2 ** 4`  | `16`   |

### Comments

You can add comments to your code. Comments are ignored by the Python interpreter. They are used to explain what the code does. You can add a comment by using the `#` symbol. Everything after the `#` symbol is ignored by the Python interpreter.

```python
# This is a comment
print("Hello, World!") # This is also a comment
```

### Python Built-in Functions

Python has many built-in functions. These functions are always available, so you can use them in your programs directly. Some of the most important built-in functions are:

- `print()`: Prints the given object to the standard output device (screen) or to the text stream file.
- `input()`: Reads a line from input, converts it to a string (stripping a trailing newline), and returns that.
- `len()`: Returns the length (the number of items) of an object.
- `type()`: Returns the type of the object.
- `int()`: Returns an integer object from any number or string.
- `float()`: Returns a floating-point object from any number or string.
- `str()`: Returns a string object from any number or string.


### Lists and Tuples

To store multiple values in one variable, you can use lists and tuples. A list is a collection which is ordered and **changeable**. In Python lists are written with square brackets. You have many possibilities to work with lists. You can add, remove, or change elements. 

```python
# List
fruits = ["apple", "banana", "cherry"]
print(fruits) # Output: ["apple", "banana", "cherry"]
```

Tuples are almost identical to lists, but written with parentheses instead of square brackets. The main difference is that tuples are **immutable**. This means that you can't change the elements of a tuple once it has been assigned. This is good for storing values that should not be changed, such as days of the week or dates on a calendar.

```python	
# Tuple
fruits = ("apple", "banana", "cherry")
print(fruits) # Output: ("apple", "banana", "cherry")
```






