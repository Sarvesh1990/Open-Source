#!/usr/bin/python
import difflib
def printValues(s1, s2):
	for i,s in enumerate(difflib.ndiff(s1, s2)):
		if s[0]==' ': 
			continue
		elif s[0]=='-':
			print(u'Delete "{}" from position {}'.format(s[-1],i))
		elif s[0]=='+':
			print(u'Add "{}" to position {}'.format(s[-1],i))

def levenshtein(s1, s2):
	#Intitialise distance array with zero value
	distance = [[0 for x in range(len(s2)+1)] for x in range(len(s1)+1)] 
	
	#Boundary conditions
	for i, c1 in enumerate(s1, start = 1):
		distance[i][0] = i
	for j, c2 in enumerate(s2, start = 1):
		distance[0][j] = j
	
	#Using dynamic programming calculate minimum edit distance
	for i, c1 in enumerate(s1, start = 1):
		for j, c2 in enumerate(s2, start = 1):
			if(c1 is c2):
				temp = 0
			else:
				temp = 2
			values = [distance[i-1][j]+1, distance[i][j-1]+1, distance[i-1][j-1]+temp]
			distance[i][j] = min(values)
			index = values.index(min(values))
	return distance[len(s1)][len(s2)]

print levenshtein("gmail", "mgail")