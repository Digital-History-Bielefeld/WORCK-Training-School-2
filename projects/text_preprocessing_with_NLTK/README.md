# Text Preprocessing with NLTK

## Introduction

Welcome to this little project on text preprocessing with NLTK. In this project, we will learn how to preprocess text data using the NLTK library. We will cover the following topics:
- **Tokenization**: Breaking down text into words, phrases, symbols, or other meaningful elements.
- **Stopwords**: Removing common words that will likely appear in any text, such as "the", "is", "in", etc.
- **Stemming**: Reducing words to their root form, such as "processing" to "process".
- **Lemmatization**: Reducing words to their base or root form, such as "running" to "run".

These are the most common text preprocessing techniques used to prepare text data for further analysis. We will also learn how to use these techniques in a real-world example. Let's get started!


## Task Block 1: Starting the Project

### Task 1: Create a new file
- **Create a new Python file**: Create a new Python file named `text_preprocessing.py`.
  - In the *Explorer view*: Right click on the `projects/group_4` directory > New File...

### Task 2: Install NLTK

You should slowly familiarize yourself with understanding the documentation of programming languages, libraries, modules, etc. and implementing their contents. [NLTK](https://www.nltk.org/) is a powerful library for text processing and it is widely used in the industry. It is a good idea to get familiar with it and understand how to use it.

------

#### NLTK - What is it?

> NLTK is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries, and an active discussion forum.<br>
--<cite> [Natural Language Toolkit](https://www.nltk.org/) </cite>

------

- Read the documentation on [NLTK](https://www.nltk.org/install.html) and try to install it via pip in your terminal.
  - Note that you also need to install `numpy.

### Task 3: Import NLTK
Import the NLTK library in your Python file and prepare an example text for text preprocessing.
Use the following example sentence:
```
Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. 
The sky is pinkish-blue. You shouldn't eat cardboard.
```

**Note:** Test as much as possible with the print() function to understand the output of the functions and to understand the behavior of the functions. This is also important to recognize bugs quickly!

**Hints:** 
- Write `pip install nltk` in your terminal to install the NLTK library. Then `pip install numpy` to install numpy.
- Add the import statement `import nltk` to the head of your Python file.

## Task Block 2: Familiarizing with NLTK

### Task 4: Tokenization
NLTK has lots of built-in methods and tools to help you with text preprocessing. One of the most common tasks is tokenization. Tokenization is the process of breaking down text into words, phrases, symbols, or other meaningful elements. Use the `word_tokenize` method to tokenize the example text. Read the documentation on [word_tokenize](https://www.nltk.org/api/nltk.tokenize.html#nltk.tokenize.punkt.PunktLanguageVars.word_tokenize) and try to use it in your Python file.


### Task 5: Stopwords
Stopwords are common words that will likely appear in any text. They are usually removed from the text before further processing. NLTK has a built-in list of stopwords that you can use to remove stopwords from your text. Use the `stopwords` method to remove the stopwords from the tokenized example text. Read the documentation on [stopwords](https://www.nltk.org/howto/corpus.html#word-lists-and-lexicons) from the NLTK website or use this external resource: [Removing stop words with NLTK in Python](https://www.geeksforgeeks.org/removing-stop-words-nltk-python/).
  - Write a function that takes a list of tokens as input and returns a list of tokens without the stopwords.
  - You can use the `nltk.download('stopwords')` method to download the stopwords from the NLTK library.
  - You can make a set of the stopwords. Sets are a type of collection like lists and tuples, but they are unordered and do not allow duplicates. Read the documentation on [sets](https://docs.python.org/3/tutorial/datastructures.html#sets) and try to use it in your Python file with the stopwords.
  - Print the list of stopwords.


### Task 6: Punctuation
You may have noticed that the tokenized example text still contains punctuation. Punctuation is usually removed from the text before further processing. For this you can prepare a list of punctuation marks and remove them from the tokenized example text with a for-loop. Write your code in functions. 
  - You can use the `string` module to get a list of punctuation marks. Read the documentation on [string](https://docs.python.org/3/library/string.html#string.punctuation) and try to use it in your Python file.
  - Remove the punctuation from the tokenized example text.

### Task 7: Stemming
Stemming is the process of reducing words to their root form. NLTK has several stemming algorithms, but we will use the Porter stemming algorithm. Use the `PorterStemmer` method to stem the example text. Read the documentation on [PorterStemmer](https://www.nltk.org/api/nltk.stem.html#nltk.stem.porter.PorterStemmer) and try to use it in your Python file.

### Task 8: Lemmatization
Lemmatization is the process of reducing words to their base or root form. The main difference between lemmatization and stemming is that lemmatization ensures that the root word belongs to the language. Use the `WordNetLemmatizer` method to lemmatize the example text. Read the documentation on [WordNetLemmatizer](https://www.nltk.org/api/nltk.stem.html#nltk.stem.wordnet.WordNetLemmatizer) and try to use it in your Python file.
- Comment out the Porter stemming algorithm. From now on, we will use the lemmatization method.

**Hints:**
*Import statements:*
- You need to import the `word_tokenize` method from the `nltk.tokenize` module on the top of your Python file.
- You need to import the `stopwords` method from the `nltk.corpus` module on the top of your Python file.
- You need to import the `PorterStemmer` and `WortNetLemmatizer` method from the `nltk.stem` module on the top of your Python file.
- You need to import the `string` module on the top of your Python file.
- You need to download the stopwords with the `nltk.download('stopwords')` method.
- You need to download the WordNet with the `nltk.download('wordnet')` method.

*Stopwords:*

- The syntax of a set is `set(your_list)`. You can use the `set` method to create a set of the stopwords: `stopwords.words('english')`.
- You can create an empty list and append the tokens to the list in a for-loop if the token is not in the set of stopwords.

*Punctuation:*
- You can use the `string.punctuation` method to get a list of punctuation marks.
- You can create an empty list and append the tokens to the list in a for-loop if the token is not in the list of punctuation marks.

*Stemming:*
- You can call the `PorterStemmer` method and store it in a variable like this: `ps = PorterStemmer()`.
- You can create an empty list and append the stemmed words to the list in a for-loop. To get the stemmed token you can call the `stem` method on the `PorterStemmer` object like this: `ps.stem(token)`.

*Lemmatization:*
- You can call the `WordNetLemmatizer` method and store it in a variable like this: `wln = WordNetLemmatizer()`. 
- You can create an empty list and append the lemmatized words to the list in a for-loop. To get the lemmatized token you can call the `lemmatize` method on the `WordNetLemmatizer` object like this: `wln.lemmatize(token)`.



## Task Block 3: Real-world Example

### Task 9: Real-world example
Now that you have learned how to use the NLTK library for text preprocessing, it's time to apply these techniques to a real-world example. You can use any text data you like, but for this exercise, we will use the txt-files in the txt-file directory. You can use the `open` method to read the content of the file and then apply the text preprocessing techniques to the content of the file.
- Write a function that takes a file path as input and creates a new file with the preprocessed text.
- Use the open() method to read the content of the file.
- Apply the text preprocessing techniques to the content of the file: tokenization, removing stopwords, removing punctuation, and lemmatization.
- Create a new file path for the preprocessed text and write the preprocessed text to the new file. Replace `.txt` with `_preprocessed.txt`.
- Use the open() method to write the preprocessed text to the new file.
- Test your function with the `alice_1.txt` file.

### Task 10: Work with more than one file
- Create a function that takes a directory path as input and applies the function from Task 9 to all files in the directory.
- The function should get all files in the folder with [os.listdir()](https://docs.python.org/3/library/os.html#os.listdir) of the [python built-in module os(https://docs.python.org/3/library/os.html#module-os)]. Read the documentation to understand how it works.
- Check if the file ends with ".txt"
- If the file ends with ".txt", create a variable "file_path" and store the folder_path, "/" and the file name in it
- Apply the function from Task 9 to the file_path
- Run your function with "projects/group_4/txt-files" as input. Comment out the old function call from Task 9 to avoid confusion.


**Hints:**
- You need to import the `os` module on the top of your Python file.
- You can use the .replace() method to replace the file ending with "_preprocessed.txt".
- You can use the .join() method to join the preprocessed token list to a string and write it to the new file.
- You can use a for-loop to iterate over the files in the directory and apply the function from Task 9 to each file.
- You can use the .endswith() method to check if the file ends with ".txt".
- You can make a new file_path with the folder_path and the file name like this: `file_path = folder_path + "/" + file_name`.

## Congratulations!
You have learned how to preprocess text data using the NLTK library. You have learned how to tokenize text, remove stopwords, remove punctuation, and lemmatize text. You have also learned how to apply these techniques to a real-world example. Great job!
