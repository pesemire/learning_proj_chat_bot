import nltk.corpus
from nltk.corpus import reuters
#print(str(nltk.corpus.brown).replace('\\\\','/'))


for field in nltk.corpus.reuters.fileids():
    if field.split("/")[0] == "test":
        f = open("../corpus/reuters/test/"+field.split("/")[1]+".txt","w")
    else:
        f = open("../corpus/reuters/train/"+field.split("/")[1]+".txt","w")
    f.write(reuters.raw(field))
    f.close()


