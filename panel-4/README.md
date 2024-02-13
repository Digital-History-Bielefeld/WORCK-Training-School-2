# Panel 3

## Functions

In programming, a function is a reusable block of code that performs a specific task. It is like a mini-program within a larger program. Functions help organize code, improve code reusability, and make it easier to understand and maintain. Before lerning something about functions, what they are good for and how they work, let's take a look at the following situation where we just use our current knowledge.

Imagine you want to write a program that encrypts and decrypts text. The encryption method should be really simple, each character in a given string should be replaced by the next character according to its Unicode value.

Unicode associates characters, signs and all kind of symbols with numbers:
- Latin Alphabet (Uppercase): `A = 65, B = 66, ..., Z = 90`
- Latin Alphabet (Lowercase): `a = 97, b = 98, ..., z = 122`

Our program would encode the text "AB" to "BC" or "abc" to "bcd". With the scenario set, let's take a look at the implementation in Python.

```python
text_1 = "hello"

print("The unprocessed text")
print(text_1)

text_1_encrypted = ""
for character in text_1:
    # Convert the current character to it's unicode value
    character_as_number = ord(character)
    # Add one to the number, the result is the next character (as a number) in Unicode alphabet
    encrypted_character_as_number = character_as_number + 1
    # Convert the new number back to a character (this is now encrypted)
    encrypted_character = chr(encrypted_character_as_number)
    # Add the encrypted character to our encrypted string
    text_1_encrypted = text_1_encrypted + encrypted_character

print("The encrypted text")
print(text_1_encrypted)

text_1_decrypted = ""
for character in text_1_encrypted:
    # Convert the current character to it's unicode value
    character_as_number = ord(character)
    # Substract one from the number, the result is the previous character (as a number) in Unicode alphabet
    decrypted_character_as_number = character_as_number - 1
    # Convert the new number back to a character (this is now decrypted)
    decrypted_character = chr(decrypted_character_as_number)
    # Add the decrypted character to our decrypted string
    text_1_decrypted = text_1_decrypted + decrypted_character

print("The decrypted text")
print(text_1_decrypted)

text_2 = "hello WORCK"
print("The unprocessed text")
print(text_2)

text_2_encrypted = ""
for character in text_2:
    character_as_number = ord(character)
    encrypted_character_as_number = character_as_number + 1
    encrypted_character = chr(encrypted_character_as_number)
    text_2_encrypted = text_2_encrypted + encrypted_character

print("The encrypted text")
print(text_2_encrypted)

text_2_decrypted = ""
for character in text_2_encrypted:
    character_as_number = ord(character)
    decrypted_character_as_number = character_as_number - 1
    decrypted_character = chr(decrypted_character_as_number)
    text_2_decrypted = text_2_decrypted + decrypted_character

print("The decrypted text")
print(text_2_decrypted)
```

As you can see the encryption/decryption code is repeating itself a lot, especially if you want to perform it multiple times within one program. This leads to a long program which is hard to read.

Let's reimplement our code with functions. In Python, you can define a function using the `def` keyword, followed by the function name and parentheses. Any input parameters are specified within the parentheses. Here's an example of our simple encryption/decryption functionality:

```python
def encrypt(text):
    encrypted_text = ""
    for character in text:
        character_as_number = ord(character)
        encrypted_character_as_number = character_as_number + 1
        encrypted_character = chr(encrypted_character_as_number)
        encrypted_text = encrypted_text + encrypted_character
    return encrypted_text
```

In this example, `encrypt` is the function name, and it takes one parameter `text`. Inside the function, we calculate the encrypted text and store it in the `encrypted_text` variable. Finally, we use the `return` statement to send the result back to the caller.

To use this function, you can call it by its name and provide the required arguments:

```python
encrypted_text = encrypt("hello WORCK")
print(encrypted_text) # "ifmmp!XPSDL"
```

Here, we call the `encrypt` function with the argument `"hello WORCK"`. The function performs the encryption and returns the result, which is then stored in the `encrypted_text` variable. Finally, we print the result.

And now the missing decrypt function, the principles are the same as for the encrypt function.

```python
def decrypt(encrypted_text):
    decrypted_text = ""
    for character in encrypted_text:
        character_as_number = ord(character)
        decrypted_character_as_number = character_as_number - 1
        decrypted_character = chr(decrypted_character_as_number)
        decrypted_text = decrypted_text + decrypted_character
    return decrypted_text
```

And here is hwo to call it.

```python
decrypted_text = decrypt("ifmmp!XPSDL")
print(decrypted_text) # "hello WORCK"
```

### Multiple parameters

Now that you know how to write and use a function, let's make our implementation a bit more flexible by adding a second parameter to our function which defines the character offset.

```python
def offset_text(text, character_offset):
    offset_text = ""
    for character in text:
        character_as_number = ord(character)
        offset_character_as_number = character_as_number + character_offset
        offset_character = chr(offset_character_as_number)
        offset_text = offset_text + offset_character
    return offset_text
```

To use this function, you can call it by its name and provide the required arguments:

```python
hello_worck = "hello WORCK"

encrypted_text = offset_text(hello_worck, 1)
print(encrypted_text) # "ifmmp!XPSDL"

decrypted_text = offset_text(encrypted_text, -1)
print(decrypted_text) # "hello WORCK"
```

### Optional parameters

Functions can also have optional parameters with default values, allowing you to provide different behavior based on the input. Here's our offset_text example with the `character_offset` as an optional parameter:

```python
def offset_text(text, character_offset=1):
    offset_text = ""
    for character in text:
        character_as_number = ord(character)
        offset_character_as_number = character_as_number + character_offset
        offset_character = chr(offset_character_as_number)
        offset_text = offset_text + offset_character
    return offset_text

hello_worck = "hello WORCK"

# Using the default character_offset of 1
encrypted_text = offset_text(hello_worck)
print(encrypted_text)  # "ifmmp!XPSDL"

# Custom character_offset of 3
encrypted_text = offset_text(hello_worck, character_offset=3)
print(encrypted_text)  # "khoor#ZRUFN"
```

In this code, the `offset_text` function has an optional parameter `character_offset` with a default value of `1`. If no argument for this parameter is provided, it will use the default value. Otherwise, it will use the provided value.

### Multiple return values

Functions can also return multiple values. Here's an example...

```python
def some_function_name(text):
    encrypted_text = offset_text(text)
    return encrypted_text
    encrypted_text_2 = offset_text(text, character_offset=3)
    return encrypted_text_2

hello_worck = "hello WORCK"
result = some_function_name(hello_worck)
print(result)  # ifmmp!XPSDL
```

... on how to **not** do it. The function returns only one value and that is because a function execution ends as soon as a return statement is reached. Code that comes after that won't be executed.

So let's take a look at how can actually return multiple values.

```python
def some_function_name(text):
    encrypted_text = offset_text(text)
    encrypted_text_2 = offset_text(text, character_offset=3)
    return [encrypted_text, encrypted_text_2]

hello_worck = "hello WORCK"
result = some_function_name(hello_worck)
print(result)  # ["ifmmp!XPSDL", "khoor#ZRUFN"]
print(result[0])  # ifmmp!XPSDL
print(result[1])  # "khoor#ZRUFN"
```

In this example, the function returns both the `encrypted_text` and `encrypted_text_2` variables as a list. We can capture the returned values in a variable (`result` in this case) and access them individually.

These are just a few examples of how functions work in Python. They are an essential concept in programming and can greatly enhance the structure and functionality of your code.



## Classes and Objects

In programming, a class is a blueprint or a template for creating objects. Objects are instances of a class, and classes define the properties (`attributes`) and behaviors (`methods`) that the objects can have. Classes provide a way to structure and organize code in an object-oriented programming (OOP) paradigm.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print("My name is " + self.name + " and i'm " + self.age + " years old")
```

**Object**:

An instance of a class. It is a concrete realization of the blueprint defined by the class.
Objects have their own set of attributes and can execute the methods defined in the class.

```python
# Create an instance of the class `Person` and save it in a variable called `max`
max = Person("max", 25)
```

**Attributes**:

```python
print(max.age)  # Will print "25"
```

These are variables that store data within a class.
They represent the characteristics or properties of an object.


**Methods**:

These are functions defined within a class that perform actions or provide functionality.
Methods represent the behaviors of an object.

```python
max.introduce()
```

### One more example

In this example, `Car` is a class that defines the blueprint for a car. `my_car` is an object (instance) of the `Car` class, and you can access its `attributes` and call its `methods`.

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def honk(self):
        print("Beep! Beep!")

# Creating an instance of the Car class
my_car = Car("Toyota", "Camry", 2022)

# Accessing attributes
print(f"My car is a {my_car.year} {my_car.make} {my_car.model}")

# Calling methods
my_car.accelerate()
print(f"Current speed: {my_car.speed} mph")

my_car.brake()
print(f"Current speed after braking: {my_car.speed} mph")

my_car.honk()
```

### To sum thing up...

In summary, a class defines a general template with attributes and methods, while an object is a specific instance created from that template with specific values for those attributes. Classes provide a way to structure code and model relationships between different entities, while objects represent actual instances of those entities in the program.

## One more thing... Inheritance

Class inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (subclass or derived class) to inherit attributes and methods from an existing class (superclass or base class). This promotes code reuse, extensibility, and the creation of a hierarchy of classes.

### Basic Example
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal makes a sound.")

class Cat(Animal):
    # Derived class code
    def speak(self):
        print("Meow!")

class Dog(Animal):
    # Derived class code
    def speak(self):
        print("Wuff, Wuff!")


some_animal = Animal("Rex")
cat_emma = Cat("Emma")
dog_olaf = Dog("Olaf")

some_animal.speak()  # Will print "The animal makes a sound."
cat_emma.speak()  # Will print "Meow!"
dog_olaf.speak()  # Will print "Wuff, Wuff!"
```


## Inheritance and super operator

The `super()` operator in Python is used to refer to the superclass or base class from within a subclass. It allows the subclass to access and invoke methods or attributes defined in the superclass.

In the example code provided, the `super().__init__(color)` line in the Rectangle class calls the `__init__()` method of the Shape class, allowing the Rectangle class to inherit and initialize the color attribute from the Shape class. This promotes code reuse and avoids duplicating code that is already defined in the superclass.

By using `super()`, you can easily extend and customize the behavior of the superclass in the subclass without explicitly referencing the superclass name. This makes the code more maintainable and flexible, especially when dealing with multiple levels of inheritance.

### Example using super()
```python
class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Creating instances of the Rectangle and Circle classes
rectangle = Rectangle("blue", 5, 3)
circle = Circle("red", 4)

# Accessing attributes and calling methods
print(f"The area of the rectangle is: {rectangle.area()}")
print(f"The perimeter of the rectangle is: {rectangle.perimeter()}")

print(f"The area of the circle is: {circle.area()}")
print(f"The perimeter of the circle is: {circle.perimeter()}")
```

## Understanding  Modules, Packages, and Libraries in Python

By mastering modules, packages, and libraries, you can leverage the power of Python's extensive ecosystem to efficiently build and maintain your projects.

- **Modules:** In Python, a module is a file containing Python definitions and statements. It allows you to organize code logically. You can use modules to break down large programs into smaller, more manageable parts.

- **Packages:** A package is a way of organizing related modules into a single directory hierarchy. It helps in maintaining a clean and structured project by grouping modules together.

- **Libraries:** The term "library" is often used interchangeably with "module" or "package."  A library is a broader term that encompasses modules and packages. A library may consist of one or more modules and packages that work together to provide a set of functionalities. It usually refers to a collection of modules or packages that serve a specific purpose, making it easier for developers to reuse code.

### Where do I find them?

- **Python Standard Library:** Python comes with a rich standard library, which includes a wide range of modules and packages. You can find information about the standard library in the official Python documentation: [Python Standard Library](https://docs.python.org/3/library/).

- **External Libraries:** There are many external libraries created by the Python community to extend Python's capabilities. You can find these on the Python Package Index (PyPI) at [https://pypi.org/](https://pypi.org/). Popular tools like `pip` help you easily install and manage external libraries.

### How do I work with them?

1. **Importing Modules:**

   ```python
   # Importing a module
   import module_name
   
   # Importing specific functions/classes from a module
   from module_name import function_name, class_name
   ```

2. **Importing Packages:**

   ```python
   # Importing a module from a package
   from package_name import module_name
   
   # Importing a specific function/class from a module in a package
   from package_name.module_name import function_name, class_name
   ```

3. **Installing External Libraries:**

   - Use `pip` to install external libraries:

     ```bash
     pip install library_name
     ```

4. **Using External Libraries:**

   - After installation, import the library in your Python script or interactive session and use its functionalities.

   ```python
   # Importing an external library
   import library_name
   
   # Using functions/classes from the library
   library_name.function_name()
   ```

Remember to check the documentation for each module, package, or library to understand its usage and available functionalities.
