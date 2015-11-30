#!/usr/bin/python
from __future__ import division
import re
import heapq

#Initialise variable
unigramMap = {}
bigramMap = {}
trigramMap = {}
previousWord = ""
prevPreviousWord = ""

#This functions takes the previous two words and total number of words count in arguement and returns the best 5 words which has the highest probability of occuring
#I am comparing only with last two word using Markov's assumption

def printNextWord(word, secondWord, wordCount):
	#Creating a heap to store the words in maximum probability order
	heapProb = []
	
	#Traverse through the bigramMap to find all keys which starts with the secondWord passed
	for keys in bigramMap.keys() :
		if keys[0] == secondWord :
			if((word, secondWord, keys[1]) in trigramMap) :
				prob = trigramMap[word, secondWord, keys[1]]/bigramMap[word,secondWord] + bigramMap[keys]/unigramMap[secondWord] + unigramMap[keys[1]]/wordCount
				#Store first five keys in heap
				if len(heapProb) < 5 :
					heapq.heappush(heapProb, (prob, keys))
				#Now after first five if the new prob is greater than smallest remove the smallest and insert the new one
				else :
					smallestProb,smallestKeys = heapProb[0]
					if smallestProb < prob :
						heapProb[0] = (prob, keys)
						heapq.heapify(heapProb)
	
	keysArray = []
	i = 0

	#Get top words with maximum probaility
	while len(heapProb) > 0 : 
		prob,keys = heapq.heappop(heapProb)
		print prob
		keysArray.insert(i, keys)
		i = i+1

	return keysArray[::-1]
			

with open('unlabeledTrainDataSmall.tsv','r') as f:
	wordCount = 0
	
	#Traverse through the sample file to generate unigram, bigram and trigram maps
	for line in f:
		previousWord = ""
		prevPreviousWord = ""
		for word in line.split():
			#Remove special case and convert word in lowecase characters
			word = re.sub('[^A-Za-z0-9]+', '', word)
			word = word.lower()
			
			if word in unigramMap :
				unigramMap[word] += 1
				if (previousWord,word) in bigramMap :
					bigramMap[previousWord,word] += 1
					if (prevPreviousWord, previousWord, word) in trigramMap :
						trigramMap[prevPreviousWord, previousWord, word] += 1
					else :
						if prevPreviousWord != "" :
							trigramMap[prevPreviousWord, previousWord, word] = 1
				else:
					if previousWord != "":
						bigramMap[previousWord,word] = 1
						if prevPreviousWord != "" :
							trigramMap[prevPreviousWord, previousWord, word] = 1
			else:
				unigramMap[word] = 1
				if previousWord != "":
					bigramMap[previousWord,word] = 1
					if prevPreviousWord != "" :
						trigramMap[prevPreviousWord, previousWord, word] = 1

			wordCount = wordCount + 1
			prevPreviousWord = previousWord
			previousWord = word

#Take user input, clean the input, remove special characters, make it lowercase as our model is trained for those data only
word = raw_input('Enter first word : ')
word = re.sub('[^A-Za-z0-9]+', '', word)
word = word.lower()

#This loop will keep printing the next word by looking at the previous two entries
while True : 
	secondWord = raw_input('Enter next word : ')
	keysArray = printNextWord(word, secondWord, wordCount)
	word = secondWord
	print keysArray

