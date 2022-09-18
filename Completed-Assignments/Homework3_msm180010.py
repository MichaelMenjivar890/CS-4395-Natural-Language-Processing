# CS 4395.001 - Assginment 3
# Michael Menjivar, msm180010

import sys
import os
from random import randint

import nltk.corpus
from nltk import *
from nltk.corpus import stopwords


def preProcessText(raw_text):
    # Tokenize raw text (get tokenList).
    textFile = Text(word_tokenize(raw_text.lower()))
    tokenList = textFile.tokens

    # Reduce tokens to alpha, non-stop words, and words longer than 5 characters (get wordList).
    tempList = []
    stopWords = set(stopwords.words('english'))
    tempList = [token for token in tokenList if token.isalpha() and token not in stopWords and len(token) > 5]
    wordList = tempList

    # Lemmatize tokens, then keep only unique lemmas (get lemmaList).
    lemmatizer = WordNetLemmatizer()
    tempList = [lemmatizer.lemmatize(token) for token in wordList]
    lemmaList = set(tempList)

    # Get Part of Speech (POS) of each lemma, and print first 20 lemmas with POS (get posList).
    posList = pos_tag(lemmaList)
    print("First 20 lemmas with POS:\n\n" + str(posList[:20]) + "\n")

    # Create list of lemmas that are nouns (get nounList).
    nounList = [lemma[0] for lemma in posList if lemma[1] == 'NN']

    # Compare number of tokens with number of nouns.
    print("Number of tokens: " + str(len(wordList)) + "\n")
    print("Number of nouns: " + str(len(nounList)) + "\n")

    return wordList, nounList

def guessingGame(nounList):

    playerScore = 5
    wordsFinished = 0
    playerGuess = ''
    correctWord = ''
    lettersGuessed = ''
    wordCompleted = True

    # Prompt user to play word guessing game.
    print("\n[ Let's play a word guessing game! ]\n")

    # Choose initial word at random from top 50 most common nouns in list.
    correctWord = nounList[randint(0,49)]

    # Initiate word guessing game.
    while True:

        # Print current guessing progress
        wordCompleted = True
        for letter in correctWord:
            if letter in lettersGuessed:
                print(letter, end=' ')
            else:
                print('_', end=' ')
                wordCompleted = False

        # Check if player has finished guessing word correctly.
        if wordCompleted is True:
            print("\nYou solved it!\n")
            print("[ Current Score: " + str(playerScore) + ' ]\n')
            wordsFinished+=1

            # Reset game and change word to be guessed to a different word.
            tempWord = nounList[randint(0,49)]
            while tempWord == correctWord:
                tempWord = nounList[randint(0,49)]
            correctWord = tempWord
            lettersGuessed = ''
        # If user has not completed word yet:
        else:
            # Let user guess a letter in the word
            playerGuess = input("\nGuess a letter: ")

            # Check for correct formatting.
            while len(playerGuess) != 1 or playerGuess in lettersGuessed:
                if len(playerGuess) != 1:
                    playerGuess = input("You did not enter a letter. Please enter a letter: ")
                else:
                    playerGuess = input("You already used that letter. Guess a different letter: ")

            lettersGuessed += playerGuess   # Add letter to string of letters already inputted by user.

            # If user inputs '!', stop guessing game.
            if playerGuess == '!':
                break

            # Check to see if user's guess is in the word.
            if playerGuess in correctWord:
                playerScore += 1
                print("Correct! Your score is now " + str(playerScore) + "\n")
            else:
                playerScore -= 1
                if playerScore > -1:
                    print("Sorry, guess again. Your score is now " + str(playerScore) + "\n")

                # If the user's score falls below 0, the game is over.
                if playerScore < 0:
                    print("\n[ Game over! Better luck next time ]")
                    print("[ The word was: " + correctWord + " ]")
                    print("[ Total words completed: " + str(wordsFinished) + " ]\n")
                    break


if __name__ == '__main__':
    # User must input a system argument.
    if len(sys.argv) < 2:
        # No sysarg given to open data file.
        print('\nERROR: No sysarg detected.\nPlease enter a filename as a sysarg.')
    else:
        # Open file and read in as raw text.
        fileName = sys.argv[1]
        current_dir: str = os.getcwd()
        dataFile = open(os.path.join(current_dir, fileName), 'r')
        raw_text = dataFile.read()

        # Tokenize raw text.
        textFile = Text(word_tokenize(raw_text))

        # Calculate lexical diversity.
        text_list = textFile.tokens  # Put tokens into list
        text_set = set(text_list)  # Create set of items in list (remove duplicates)
        listCount = len(text_list)  # Total number of tokens
        setCount = len(text_set)  # Total number of UNIQUE tokens

        lexicalDiversity = setCount / listCount

        # Print lexical diversity.
        print("\nLexical diversity of the text: " + str(round(lexicalDiversity, 2)) + "\n")

        # Preprocess text.
        tokens, nouns = preProcessText(raw_text)

        # Create dict to hold nouns and counts, sort dict into list, and print 50 most commons words.
        nounCounts = {noun: tokens.count(noun) for noun in nouns}
        nounCountDict = {}
        nounCountDict = sorted(nounCounts.items(), key=lambda kv: kv[1])
        nounCountDict.reverse()
        print("50 most common words in the text, and their count: \n")
        print(nounCountDict[:50])

        # Save top 50 words into list
        x=0
        nounList = []
        for key, value in nounCountDict:
            if x < 50:
                nounList.append(key)
            x += 1

        # Initiate word guessing game.
        guessingGame(nounList)