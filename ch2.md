# Corpus and Voc Resource

## Corpus included in NLTK
1. webtext: online text corpus, including chats and messages
2. brown: sorted by 500 different kinds of text
3. reuters: news and press text
4. inaugural: inaugural speech text, including speech text from 55 presidents
5. gutenberg: text from gutenberg project

## listing a corpus in NLTK
nltk.corpus.name_of_the_corpus.fileids()

```python
nltk.corpus.gutenberg.fileids()
```

return all file ids in the corpus

```python
nltk.corpus.gutenberg.raw('chesterton-brown.txt')
```

return chesterton-brown.txt as raw text

```python
nltk.corpus.gutenberg.raw('chesterton-brown.txt')
```

return list of words in chesterton-brown.txt

```python
nltk.corpus.gutenberg.sents('chesterton-brown.txt')
```
return list of sentences in chesterton-brown.txt

## Loading a corpus in NLTK
```python
from nltk.corpus import PlaintextCorpusReader
corpus_root = '/tmp' # or other location if you want to specify one corpus
wordlists = PlaintextCorpusReader(corpus_root, '.*')
wordlists.fileids()
```

## Conditional Frequency Distribution
Show the frequency of word under different categories.
```python
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import nltk
from nltk.corpus import brown #brown is sorted by categories

genre_word = [(genre, word) 
             for genre in brown.categories()
             for word in brown.words(categories=genre)
             ]
# genre = all categories in brown, word = word list in **a** certain category
# (genre,word) is a pair of category and voc

cfd = nltk.ConditionalFreqDist(genre_word) #create a conditional freqency distribution

cfd.plot(conditions=[cat_1,cat_2,...,cat_n], samples = [u'term1', u'term2', ..., u'term_n']) #create a plot
