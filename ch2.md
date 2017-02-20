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

