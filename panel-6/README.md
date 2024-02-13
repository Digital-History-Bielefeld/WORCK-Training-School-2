# Panel 6: Python for Natural Language Processing (NLP)

This should give you an overview over how to use Python for (simple) NLP tasks.
The most simple package to do so is `spacy` (<https://spacy.io>).

There are two tasks on Part-of-Speech tagging and NER-tagging:

- preprocessing text
- NLP basics with spaCy

##  More complex examples

There are two more examples, you don't have to understand the code right away.
They should just show you, what is possible with Python using Machine Learning models processing your data.

### Document Clustering

Having a huge CSV-file (comma-seperated-values) containing tousands of songtexts and their metadata, you can import, and process those songs. Then the data has to be cleaned and you choose some artists, which songtexts you want to cluster. This means, you embed the songtexts - so you get a vector for each songtext (= document).

With a clustering algorithm (you don't have to understand), the document-vectors are put into "groups". The `AgglomerativeClustering` from `sklearn` merges pair of clusters of sample data.

So the visualization at the end shows you, songs which artists are sharing clusters.
It looks a bit mixed, since we had to reduce the vectorization to 2D.
But you can see some patterns.

### Visiualization of embeddings in 3D

There is the Polysemy - a word can mean different things depending on it's context.
With two different Embedding-models - a Glove embedding and a BERT embedding - we do embed words and sentences.
The visualization of the different embeddings are interesting, because you can see, how close which word-vector is to others.
