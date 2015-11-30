#!/usr/bin/python

import constants
import random

#Todo
#Create a map of letter versus their position

#Done 
#Print total number of attempts left for the user, Show him the actual movie word with xxxxxxx
#Ask user to start with a letter
#Function to check if the letter is there in the word 
#Maintain a count of number of characters in word for proper finish
#If letter is there in the word display corrected word else send some mocking message and show old word
#Display count left too
#Keep incrementing count
#Prepare a constant file to manage how much count is allowed
#If current count exceeds allowed print that the player lost otherwise on whatever count the word is guessed print word and number of attempts

def getCharactersLeft(movieCharList) :
	charactersLeft = 0
	for i in movieCharList :
		if(i != " ") :
			charactersLeft = charactersLeft + 1
	return charactersLeft

def getStarredMovieList(movieCharList) :
	for i in movieCharList :
		if(i == " ") :
			starredMovieCharList.append(" ")
		else :
			starredMovieCharList.append("*")
	return starredMovieCharList

def getMovieName (movieFile):
	lines = [line.rstrip('\n') for line in open(movieFile)]
	randomNum = random.randint(0, len(lines) - 1)

	return lines[randomNum]

def getPositionOfCharacterGivenInMovieName(character, movieCharList):
	posList = []
	for i, char in enumerate(movieCharList, start=0):
		if(char == character):
			posList.append(i)

	return posList

def askForInput(countGuesses, alreadyUsedCharacters):
	askInput = "Enter your " + ordinal(countGuesses+1) + " guess : "
	guess = raw_input(askInput)
	guess = guess.lower()

	for i in alreadyUsedCharacters : 
		if (i == guess) :
			print "Dude, you have already attempted for ",guess
			guess = askForInput(countGuesses, alreadyUsedCharacters)
			guess = guess.lower()

	return guess

ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])

movieName = getMovieName("movie-name.txt")
movieCharList = list(movieName)
starredMovieCharList = []
movieLength = len(movieName)
starredMovieCharList = getStarredMovieList(movieCharList)
countAttempts = 0
countFailAttempts = constants.ALLOWED_COUNT
charactersLeft = getCharactersLeft(movieCharList)
alreadyUsedCharacters = []

print "Hello bitch. How are you today. Your movie is ", movieLength, " characters long. Movie name is ",''.join(starredMovieCharList)
print "You have ",countFailAttempts, " attempts left"


while(countFailAttempts > 0) :
	guess = askForInput(countAttempts, alreadyUsedCharacters)
	alreadyUsedCharacters.append(guess)
	posList = getPositionOfCharacterGivenInMovieName(guess, movieCharList)

	if(len(posList) == 0 ):
		countAttempts = countAttempts + 1
		countFailAttempts = countFailAttempts - 1
		if(countFailAttempts != 0) :
			print " Sorry bitch, you fucked up one attempt, total attempts left : ",countFailAttempts
		else :
			print " Sorry bitch, you fucked up big time. No more attempts left. Movie is '",movieName,"'. Better luck next time !!"
	else :
		charactersLeft = charactersLeft - len(posList)
		countAttempts = countAttempts + 1
		for i in posList :
			starredMovieCharList[i] = guess

		if(charactersLeft == 0):
			print " Yayy bitch, you guessed the movie, movie is '", ''.join(starredMovieCharList), "' total attempts used : ", countAttempts
			break
		else :
			print " Sexy guess, modified movie name is ", ''.join(starredMovieCharList), " total attempts left : ",countFailAttempts


