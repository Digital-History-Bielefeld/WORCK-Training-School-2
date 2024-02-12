'''
This function is used to preprocess the string data. It takes a string as input and returns the preprocessed string.
The preprocessing steps include:
- Converting the string to lowercase
- Splitting the string into a list of strings based on the newline character
- Creating a new empty list of strings
- Stripping the leading and trailing whitespaces from each string in the list and adding it to the new list
- Joining the new list of stripped strings into a single string with space as the separator
- Printing the preprocessed string
'''

def clean(string):
    string = string.lower()
    string_list = string.split('\n')
    new_string_list = []
    for string in string_list:
        new_string_list.append(string.strip())
    string = ' '.join(new_string_list)
    print(string)

