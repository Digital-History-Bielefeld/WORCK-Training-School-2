import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string
import os

nltk.download('stopwords')
nltk.download('wordnet')

example_text = '''
Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. 
The sky is pinkish-blue. You shouldn't eat cardboard.
'''

#############################################
### Task Block 2: Familiarizing with NLTK ###
#############################################

# Task 4
tokens = word_tokenize(example_text)
print(tokens)

# Task 5
def remove_stop_words(tokens):
    stop_words = set(stopwords.words('english'))
    filtered_tokens = []
    for token in tokens:
        if token not in stop_words:
            filtered_tokens.append(token)
    # You could write it even shorter:
    # filtered_tokens = [token for token in tokens if token not in stop_words]
    return filtered_tokens

filtered_tokens = remove_stop_words(tokens)
print(filtered_tokens)

# Task 6
def remove_punctuation(tokens):
    filtered_tokens = []
    for token in tokens:
        if token not in string.punctuation:
            filtered_tokens.append(token)
    # You could write it even shorter:
    # filtered_tokens = [token for token in tokens if token not in string.punctuation]
    return filtered_tokens

filtered_tokens = remove_punctuation(filtered_tokens)
print(filtered_tokens)

# Task 7
def stemming(tokens):
    ps = PorterStemmer()
    stemmed_tokens = []
    for token in tokens:
        stemmed_tokens.append(ps.stem(token))
    return stemmed_tokens

#stemmed_tokens = stemming(filtered_tokens)
#print(stemmed_tokens)

# Task 8

def lemmatization(tokens):
    wnl = WordNetLemmatizer()
    lemmatized_tokens = []
    for token in tokens:
        lemmatized_tokens.append(wnl.lemmatize(token))
    return lemmatized_tokens

lemmatized_tokens = lemmatization(filtered_tokens)
print(lemmatized_tokens)

#############################################
### Task Block 3: Real-world Example ###
#############################################

# Task 9
def preprocessed_txt_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = remove_stop_words(tokens)
    tokens = remove_punctuation(tokens)
    tokens = lemmatization(tokens)

    new_file_path = file_path.replace('.txt', '_preprocessed.txt')
    
    with open(new_file_path, 'w') as file:
        file.write(' '.join(tokens))

#preprocessed_txt_file('projects/group_4/txt-files/alice_1.txt')

# Task 10
def preprocessed_folder(folder_path):
    for file in os.listdir(folder_path):
        if file.endswith('.txt'):
            file_path = folder_path + '/' + file
            preprocessed_txt_file(file_path)

preprocessed_folder('projects/group_4/txt-files')
