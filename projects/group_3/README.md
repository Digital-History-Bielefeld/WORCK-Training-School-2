# Text Preprocessing with Regular Expressions

## Introduction

Welcome to this little text preprocessing project! In this exercise, you will be working on cleaning up a text file containing text mistakes (for example OCR-errors) using Regular Expressions. The goal is to deepen your skills in using Python and use it to clean up your txt files and eliminate errors in them. You will practice importing modules, using for-loops and if-conditions and working with your given file system.

You see a blank file in your folder with the name `regex_project.py`. This is the file in which you will create the project together with your team colleagues. There is also the `txt-files` folder, which contains various txt files. However, these have a problem: many OCR text recognitions - especially for historical languages - still contain many errors. This is a particular hindrance if you want to work with large quantities of files and examine them using computer-aided methods. We humans may understand that "th:5" should mean "this", but common processing programs do not. It is therefore always advisable to clean up your digital data before processing it further. 
Numerous errors have also crept into the data contained in the folder. We want to eliminate these now. Let's start by importing the corresponding library!

## Tasks

### Task 1: Import required module

You should slowly familiarize yourself with understanding the documentation of programming languages, libraries, modules, etc. and implementing their contents. There is also a Python module for regular expressions. [In the documentation](https://docs.python.org/3/howto/regex.html) for this, you find many information about regular expressions and it is also noted how the corresponding module should be imported. So add this to the beginning of your file! 

Note: Test as much as possible with the print() function to understand the output of the functions and to understand the behavior of the functions. This is also important to recognize bugs quickly!

------

#### Regular Expressions - What is this?

Regular Expressions (regex or regexp) are powerful sequences of characters that form a search pattern, used for string manipulation and matching within text. They are widely employed in various fields, including programming, data analysis, and text processing, due to their versatility and efficiency in handling complex search and manipulation tasks. For historians, regular expressions serve as invaluable tools for data cleaning and analysis in digitized historical documents. Historians can leverage regex to efficiently locate and correct OCR errors, extract specific information from large datasets, and identify patterns or trends within historical texts. This not only streamlines the process of working with vast amounts of textual data but also enhances the accuracy and reliability of historical research by ensuring the integrity of digitized documents.

------

Note: If you get stuck, look at the solutions.py file!

### Task 2: Working with some regular expressions

#### Regular  Expressions  Cheat  Sheet

| **Expression** | **Description**                                | **Example**                                |
| -------------- | ---------------------------------------------- | ------------------------------------------ |
| `.`            | Any character except a newline                 | `a.b` matches "axb", "aab", but not "a\nb" |
| `^`            | Start of the string                            | `^abc` matches "abc" at the beginning      |
| `$`            | End of the string                              | `xyz$` matches "xyz" at the end            |
| `*`            | Zero or more occurrences                       | `ab*c` matches "ac", "abc", "abbc"         |
| `+`            | One or more occurrences                        | `ab+c` matches "abc", "abbc", but not "ac" |
| `?`            | Zero or one occurrence                         | `colou?r` matches "color" or "colour"      |
| `{n}`          | Excactly n occurrence                          | `hello{3}` matches "hellooo"               |
| `{n,m}`        | Between n and m occurrences                    | `hello{1,3}` matches "hello", "hellooo" or "hellooo"|
| `\`            | Escape special character                       | `\.txt` matches ".txt"                     |
| `[abc]`           | Character class                                | `[aeiou]` matches any vowel                |
| `[a-z]`        | Range in character class                       | `[a-z]` matches any lowercase letter       |
| `[a-zA-Z]`     | Multiple ranges in character class             | `[a-zA-Z]` matches any letter              |
| `[^abc]`       | Negated character class                        | `[^0-9]` matches any non-digit             |
| `()`           | Grouping                                       | `(abc)+` matches "abc", "abcabc", ...      |
| `\|`           | Alternation                                    | `cat\|dog` matches "cat" or "dog"           |
| `\d`           | Any digit                                      | `\d{2,4}` matches 2 to 4 digits            |
| `\w`           | Any word character (alphanumeric + underscore) | `\w+` matches one or more words            |
| `\s`           | Any whitespace character                       | `\s+` matches one or more spaces           |
| `\b`           | word boundary                                  | `\btest\b`matches the word "test"n not "testing" e.g.        |
| `\D`           | Any non-digit                                  | `\D+` matches one or more non-digits       |
| `\W`           | Any non-word character                         | `\W+` matches one or more non-words        |
| `\S`           | Any non-whitespace character                   | `\S+` matches one or more non-spaces       |
| `\B`           | Non-word boundary                              | `\Btest\B` matches "atestb" but not "test"|
| `\n`           | Newline                                        | `abc\n123` matches "abc" followed by newline and "123" |
| `\t`           | Tab                                            | `abc\t123` matches "abc" followed by tab and "123" |
| `(?i)`         | Case-insensitive                               | `(?i)abc` matches "abc", "AbC", etc.       |
| `(?<=...)`     | Positive lookbehind                            | `(?<=@)\w+` matches word after "@"         |
| `(?=...)`      | Positive lookahead                             | `\d(?=px)` matches digit before "px"       |
| `(?!...)`      | Negative lookahead                             | `\d(?!px)` matches digit not before "px"   |
| `(?<!...)`     | Negative lookbehind                            | `(?<!@)\w+` matches word not after "@"     |
| ``

This cheat sheet provides a quick reference for commonly used regular expressions. Customize and combine these expressions to suit your specific matching needs.

Let's start with a few simple regular expressions to get you used to using them. 

1) Save the sentence "Today - on 2024-02-13 - we are sitting in room X-A2-103 and attending a Python workshop. At 12.00 we finally go to the Mensa." in the variable "example_sentence". 
2) Above we have a cheat sheet that you can use to solve the following tasks. With the function "re.findall()" all matches for a certain pattern can be displayed. **Try it out and filter out all occurrences of one or more digits. Save it in the variable "output" and print it.**

​	Use of the function: 

​	**re.findall()**
This function is used in Python's `re` module to find all occurrences of a pattern in a given string. It returns a list containing all the matches found. The pattern is specified as the first argument, and the second argument is the input string.

​	*Example:*
```python
import re

text = "The cat and the hat sat on the mat."
matches = re.findall(r'\b\w{3}\b', text) # Matches three-letter words
print(matches)
# Output: ['The', 'cat', 'and', 'the', 'hat', 'sat', 'the', 'mat']
```


​	The output in our example should be: `['2024', '02', '13', '2', '103', '12', '00]`

3) Find `[2024-02-13, X-A2-103]`. Use again "re.findall()", save the result in a variable and print it to the console. 

4) Find `['on', 'we', 'are', 'sitting', 'in', 'room', 'and', 'attending', 'a', 'workshop', 'we', 'finally', 'go', 'to', 'the']`.

5) You can also use groups to capture specific parts of a pattern. For example, you can use parentheses to group together parts of a pattern and then access the matched groups. This is useful if you want to find a specific string pattern, but only want to extract a certain part of it. For example, you can use the pattern `r'(\d{4})-(\d{2})-(\d{2})'` to match dates in the format "YYYY-MM-DD" and extract the year, month, and day separately. In or example find the output: `[('X-', 'A2-', '103')]`.

6) Test a little with the given options and familiarize yourself with the patterns to match regular expressions! Are there any more specific things you can filter out? 
You can use the website [Regex 101](https://regex101.com/) and of course the documentation to help you, where you can find even more options and test them out directly.

7) In addition to re.findall(), there are other functions that can be powerful tools when dealing with texts. A few of the most important ones are listed below:

**re.compile()**
This function compiles a regular expression pattern into a regex object, which can be used for matching operations. It improves the efficiency of repeated pattern matching, as the pattern is precompiled and stored.

*Example:*
```python
import re

pattern = re.compile(r'\b\w{3}\b')  # Compile a regex pattern for three-letter words
text = "The cat and the hat sat on the mat."
matches = pattern.findall(text)
print(matches)
# Output: ['The', 'cat', 'and', 'the', 'hat', 'sat', 'the', 'mat']
```

**re.split()**
This function splits a string into a list of substrings based on a specified pattern. It takes two arguments: the pattern and the input string. The substrings are determined by the occurrences of the pattern in the string.

*Example:*
```python
import re

text = "apple, orange, banana, grape"
result = re.split(r',\s*', text) # Split by comma followed by optional whitespace
print(result)
# Output: ['apple', 'orange', 'banana', 'grape']
```

**re.sub()**
The `re.sub()` function is used for replacing occurrences of a pattern with a specified string. It takes three arguments: the pattern to search for, the string to replace the matches, and the input string.

*Example:*
```python
import re

text = "The quick brown fox jumps over the lazy dog."
pattern = re.compile(r'\b\w{5}\b')  # Replace five-letter words with "*****"
result = re.sub(pattern, '*****', text)
print(result)
# Output: "The ***** ***** fox ***** over the lazy dog."
```

**re.search()**
This function searches for the first occurrence of a pattern in a given string. It returns a match object if the pattern is found and `None` otherwise. The pattern and the input string are the two main arguments.

*Example:*
```python
import re

text = "The cat and the hat sat on the mat."
pattern = re.compile(r'\b\w{3}\b')  # Search for the first three-letter word
match = re.search(pattern, text)
print(match.group())
# Output: 'The'
```

Let's practise a few of these things. 

a. Split our example string into sentences.
Output: `['Today - on 2024-02-13 - we are sitting in room X-A2-103 and attending a Python workshop', 'At 12.00 we finally go to the Mensa.']`
b. Now you have our string splitted in two sentences. Now try to change the date **of the first sentence** to 'XXXX-XX-XX'. For this you should work with the output of 6a). Remember that its output is a list and you can work with list via the index.

### Task 3: Working with bigger text strings

You have now become familiar with the basic functions of the re module. Now it's time to apply this knowledge to a larger text-strings.
Save the following text in a multi-line string in the variable "text". 

```
There was noth:ng so VERY remarkable in that; nor d:d 

Alice
think it so VERY much out of the way to hear the Rabbit say to
itself, `Oh dear! Oh dear! I shall be late!' (when she thought
it over afterwards, it occurred to her that she ought to have
wondered at this, but at the t:me it all seemed quite natural);
but when the Rabbit actually TOOK A WATCH OUT OF ITS WAISTCO4T-POCKET, and 
looked at it, and then hurried on, 4lice start-
ed to
her feet, for it flashed across her m:nd that she had never
before seen a rabbit with e:ther a waistcoat-pocket, or a watch to
take out of it, and burn-
ing with curiosity, she ran across the
field after it, and fortunately was just in t:me to see it pop
down a large rabbit-hole
under the hedge.
``` 

You may have noticed that there are some errors in the text. The goal of this task is to write a function that corrects these errors.

1) Can you find the errors in the text? Part of preprocessing data is to look at your text and identify common errors first.
2) Write a function called "clean_text" that takes a string "input_text" as input and returns a new string "cleaned_text".
3) You should strip your text first with the python built-in function "strip()".
4) Now let's write some regular expressions to clean up the text. The errors in the text are as follows:
    - Hyphenation causes problems in many texts. Write a pattern that matches all "-" with a newline after it. Replace all occurrences of this pattern with an empty string.
    - Replace all whitespaces which are more than one with a single space.
    - Replace all occurrences of ":" with "i". This is a bit tricky, don't be afraid to look for clues if you get stuck.
    - Replace all occurrences of "4" with "A".
4) Save the result of the function in a variable and print it to the console.

**Hints:**
- Use the re.sub() function to replace occurrences of a pattern with a specified string.
- Remember the groups in Task 1! 
    - You can use the re.findall() function first to find all occurrences of a pattern and group them in single blocks. You could for example use the pattern `r'(\d{4})-(\d{2})-(\d{2})'` to match dates in the format "YYYY-MM-DD" and extract the year, month, and day separately.
    - Then you can use a for-loop to iterate over the list with matches of findall and use the re.sub() function to replace just one group of the match. For example, you want to change only the month in the date it could look like this:

    ```python
    example_text = "Today is 2023-02-13."
    matches = re.findall(r'(\d{4})(-\d{2})(-\d{2})', example_text)
    for match in matches:
        example_text = re.sub(match[0], '2024', example_text)
    ```
- This is just an example and you can use it to solve the task. It is not the smartest or fastest, but maybe easiest to understand. You could also use the re.compile and .match() functions or you use [the writing](https://docs.python.org/3/library/re.html#re.sub) `r'2024\2\3` in the re.sub() function to let group 2 and 3 unchanged with \2 and \3. 
- RegEx you could use:
    - `\n` for newline
    - `\s` for whitespace
    - `+` for one or more occurrences
    - `*` for zero or more occurrences
    - `\b` for word boundary
    - `\w` for any alphanumeric word character



### Task 4: Working with an external file

You have now written a function that can clean up a text. Now let's apply this function to a file.
In your txt-files folder are files called alice_1.txt. This file also has some errors in it. Let's clean it up using the function you wrote in Task 3 and store the cleaned text in a new file.

1) Write a function called "clean_file" that takes a string "file_path" as input and write its contents in a new file with the [python built-in function open()](https://docs.python.org/3/library/functions.html#open).
2) The function should open the file at the given file path and read the text from the file. 
3) Then apply the "clean_text" function to the text and store it in a new variable.
4) Replace the old file ending ".txt" with "_cleaned.txt".
5) Write the cleaned text to a new file with the new file ending.
6) Run the function with the file path "projects/group_3/txt-files/alice_1.txt" and check if the file is cleaned up.

**Hints:**
- You can use the [python built-in function open()](https://docs.python.org/3/library/functions.html#open) to open a file and read its contents.
- You can use the .replace() function to replace the old file ending with the new one.
- You can use the [python built-in function open()](https://docs.python.org/3/library/functions.html#open) to open a file and write its contents to a new file.


### Task 5: Working with a folder

You have now written a function that can clean up a file. Now let's apply this function to a folder.
For this you can use the function "clean_file" from Task 4 and apply it to all files in the txt-files folder.

1) Write a function called "clean_folder" that takes a string "folder_path" as input and applies the "clean_file" function to all files in the folder.
2) The function should get all files in the folder with [os.listdir()](https://docs.python.org/3/library/os.html#os.listdir) of the [python built-in module os(https://docs.python.org/3/library/os.html#module-os)]. Read the documentation to understand how it works.
4) Check if the file ends with ".txt"
5) If the file ends with ".txt", create a variable "file_path" and store the folder_path, "/" and the file name in it 
6) Then apply the "clean_file" function to the new file path.
7) Run the function with the folder path "projects/group_3/txt-files" and check if the files in the folder are cleaned up. Comment out the old function call from Task 4 to avoid confusion.

**Hints:**
- You can use a for-loop to iterate over the files in the folder.
- You can use the .endswith() function to check if a string ends with a specific ending.

## Congratulations!

You have now learned how to use regular expressions to clean up text files and apply this knowledge to a folder. This is a very important skill for data preprocessing and will be useful in many different contexts.


