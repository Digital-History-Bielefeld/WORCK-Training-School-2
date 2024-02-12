# Panel 5: Introduction to Natural Language Processing (NLP)

NLP is a very broad term to describe methods, which process text. Text is an unstructured data type and is sequential (not parallel).

## Glossary

- **Corpus** Collection of documents
- **Document** Collection of tokens
- **Token** Collection of characters and usually base unity
- **Word Types** Distinct tokens in the corpus
- **Vocabulary** All word types in the corpus

## Preprocessing

Preparing the text for further processing by multiple methods to reduce the vocabulary size, remove noise, maybe add additional information and split documents into shorter spans to be processed.

### Methods

- **Sentence-splitting and Tokenization** Convert the string into lists of sentences and tokens that can be used as input for an ML-pipeline.
- **Normalization** Reduces vocabulary size by casing, lemmatization, noise removal and stop word removal.

  - *Casing* Decide if it makes sense to lowercase the text
  - *Lemmatization* Transforming the words into their base form
  - *Noise removal* Remove punctuation and special characters
  - *Stop Word removal* Remove words that do not carry information

###  Python Libraries for Preprocessing

- **Natural Language Toolkit (NLTK)** [nltk.org](https://nltk.org) - has good tokenizers and stemmers, huge stopword lists, multiple languages
- **spaCy** [spacy.io](https://spacy.io) - simple usage and very performant, has good models for 18 languages
- **flarNLP** [flair Tutorial](https://flairnlp.github.io/docs/intro) - very performant with good community models, strong at character based level (good for historic text)

##  Vectorization and Language Models

With vectorization math can be done with text, it is easier to learn language patterns, and things can be calculated (like similarity of words). But vectors must be contextualized and validated!

**Language Models** are trained to *embed* text, which means vectorizing it on document, sentence, token, subtoken or character level. Ideally the embeddings of words are trained dependent on their context.

## Tagging

Based on Language Models for your texts, you can train **taggers**. Those can mark and index entities. Most often used taggers in NLP are **Named Entity Recognizer (NER)** and **Part-of-Speech (PoS) tagger**.

###  Named Entity Recognizer (NER-tagger)

Identifiy key informations of your text on a semantical level. Entities are classified in a set of predefined categories. An entity can be more than one token (like *New York*).

Often used categories are:

- **PER** for Person
- **ORG** for Organization
- **LOC** for Location

### Part-of-Speech (PoS-tagger)

Recognition of the syntactic word type of each token. They have to work contextualized.

Examples of tags:

- **NOUN**
- **PNOUN** proper noun - like a name or location
- **VERB**
- **PUNCT** punctuation
- **ADJ** adjective