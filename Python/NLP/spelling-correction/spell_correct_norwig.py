#!/usr/bin/python
import re, collections
import difflib
import csv

def conversionProbability(s1, s2):
  flag = False
  prob = 0
  for i,s in enumerate(difflib.ndiff(s1, s2)):
    if s[0]==' ': 
      continue
    elif s[0]=='-':
      print(u'Deletex "{}" from position {}'.format(s[-1],i))
      print EditProbabilityMap[s1[i-1] + "|" + s1[i-1]+s1[i]]
      prob += EditProbabilityMap[s1[i-1] + "|" + s1[i-1]+s1[i]]
      flag = True
    elif s[0]=='+':
      print(u'Add "{}" to position {}'.format(s[-1],i))
      if(flag):
        flag = False
        print EditProbabilityMap[s1[i-2] + s2[i-1] + "|" + s1[i-2]]
        prob += EditProbabilityMap[s1[i-2] + s2[i-1] + "|" + s1[i-2]]
      else:
        print s2
        print EditProbabilityMap[s2[i-1] + s2[i] + "|" + s2[i-1]]
        prob += EditProbabilityMap[s2[i-1] + s2[i] + "|" + s2[i-1]]
  print prob

def words(text): return re.findall('[a-z]+', text.lower()) 

def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model

def generateEditProbabilityMap(filename):
  f = open(filename, "r")
  words = f.read().split("\n")
  model = collections.defaultdict(lambda: 0)
  for word in words :
    word = word.split("\t")
    model[word[0]] = int(word[1])
  return model

NWORDS = train(words(file('big.txt').read()))

EditProbabilityMap = generateEditProbabilityMap('ngrams/count_1edit.txt')

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edits1(word):
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   inserts    = [a + c + b     for a, b in splits for c in alphabet]
   return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

def known(words): return set(w for w in words if w in NWORDS)

def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    for candidate in candidates:
      conversionProbability(word, candidate)
    return max(candidates, key=NWORDS.get)

print correct("doc")