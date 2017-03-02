#!/usr/bin/python/
# -*- coding:utf-8 -*-
import codecs, unicodedata, re, glob, os


def les10mots(texte):
	freqmots={}
	for mot in texte.split():
		freqmots[mot]=freqmots.get(mot,0)+1
	return sorted(freqmots,key=freqmots.get)[-10:]
def nbr10mots(texte):
    languesSimilaires={}
    les10inconnus=les10mots(texte)
    for f in os.listdir("textesLangues"):
        les10train=les10mots(open("textesLangues/"+f).read())
        languesSimilaires[f[:2]]= len(set(les10train)&set(les10inconnus))
    return max(languesSimilaires, key=languesSimilaires.get)

def texteFreqMot(texte):
    motFreq={}
    mots=texte.split()
    for mot in mots:
        motFreq[mot]=motFreq.get(mot,0)+1/len(mots)
    return motFreq
def distanceFreq(freq1, freq2):
    distance=0
    for mot in set(freq1) | set(freq2):
        distance+=abs(freq1.get(mot, 0) - freq2.get(mot, 0))
    return distance/2
def distancemots(texte):
    codedistance={}
    freqInconnues=texteFreqMot(texte)
    for f in os.listdir("textesLangues"):
        freq=texteFreqMot(open("textesLangues/"+f).read())
        codedistance[f[:2]]=distanceFreq(freqInconnues,freq)
    return min(codedistance,key=codedistance.get)

def ngrams(texte, n):
    return [ texte[i:i+n] for i in range(len(texte)-n+1) ]
def texteFreqNgram(texte, n):
    ngramsfreq={}
    ngs=ngrams(texte, n)
    for ng in ngs:
        ngramsfreq[ng]=ngramsfreq.get(ng,0)+1/len(ngs)
    return ngramsfreq
def distanceNgram(texte,n):
    langueDistances={}
    freqInconnues = texteFreqNgram(texte, n)
    for f in os.listdir("textesLangues"):
        if f[0]==".": continue
        freqActuelles = texteFreqNgram(open("textesLangues/"+f).read(), n)
        langueDistances[f[:2]] = distanceFreq(freqActuelles, freqInconnues)
    return min(langueDistances, key=langueDistances.get)
def distance1gram(texte):
    return distanceNgram(texte,1)
def distance2gram(texte):
    return distanceNgram(texte,2)
def distance3gram(texte):
    return distanceNgram(texte,3)
def distance4gram(texte):
    return distanceNgram(texte,4)
def distance5gram(texte):
    return distanceNgram(texte,5)

algos=[nbr10mots,distancemots,distance1gram,distance2gram,distance3gram,distance4gram,distance5gram]
def testerTout():
    for alg in algos:
        print("Algo", alg.__name__)
        for fichiertest in os.listdir("inconnuLangues"):
            codereel=fichiertest[:2]
            codeobtenu=alg(open("inconnuLangues/"+fichiertest).read())
            print(fichiertest,codereel,codeobtenu,codereel==codeobtenu)

#testerTout()


def longueurQualite(nbCar):
    """
    elle prend un nombre de caractère
    elle teste les algos dans liste algos
    elle rend le taux de reussite de chaque algo
    """
    dictAlgoReussite={} #dic nom de algo et float de taux réussite
    for alg in algos:
        #print ("Algo", alg.__name__)
        resultats=[]
        for fichiertest in os.listdir("inconnuLangues"):
            codereel=fichiertest[:2]
            texte=open("inconnuLangues/"+fichiertest).read()
            len(texte)//nbCar
            codeobtenu=alg(open("inconnuLangues/"+fichiertest).read()[:nbCar])
            resultats+=[codereel==codeobtenu]
        dictAlgoReussite[alg.__name__]=sum(resultats)/len(resultats)
    return dictAlgoReussite

print(longueurQualite(1000))
