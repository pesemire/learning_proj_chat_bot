# Install NLTK (Natural Language Toolkit)
NLTK is a platform for building Python programs to work with human language data. In this chapter, we introduce how to install and use the package. 

open bash
```
pip install nltk
```

open python
```python
import nltk
nltk.download()
```
choose 'book' and click download.

## View all text
```python
from nltk.book import *
```

## Searching a word
location.concordance("word")
```python
text1.concordance("ship")
```
return all sentences which include word "ship"

## Searching a synonym 
location.similar("word")
```python
text1.similar("ship")
```
return all synonyms of the word "ship"

## Localizing a word
location.dispersion_plot([term1,term2,term3,...,termn])

## Word frequency
```python
img = FreqDist(location)
img.plot(50, cumulative = True)
```

# Two approaches of NLP
1. rule-based
2. stat-based

We will follow the second approach. 


