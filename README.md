# CS-4395-Natural-Language-Processing
### *Michael Menjivar*
Repository for CS 4395 assignments/projects.

## Assignment Zero - GitHub Portfolio setup
Link to [Assignment 0](CS_4395_-_Assignment_0.pdf).

## Assignment 1 - Python Text Processing
Link to [Assignment 1](Homework1_msm180010.py) and assignment instructions [here](Completed-Assignments/Assignment_1).

The program reads in a .csv file, processes the employee information stored in said file, stores information in a pickle file, and reads/outputs formatted data from the pickle file.

To run: download the .py file, place the .csv file with the employee data in a folder named "data", and move data to the directory where the .py file is stored. Make sure that the Natural Language Tool Kit (NLTK) is installed on your device before running in the Terminal/Command Line.
Then, run the .py file with the command "python [.py file] data/[.csv file]", where [.py file] is the name of the Python file you run and [.csv file] is the file with the employee data as a sysarg (system argument). If no data file is used as a sysarg, an error will be returned.

While the simplicity of Python syntax makes text processing simpler, there are certain issues I had while implementing this program that stuck out to me as Python specific. Mainly, how I was unable to easily iterate directly through a String in the same manner as an Array in other languages, making inserting characters (specifically '-' while formatting phone numbers) slightly more complex. However, the process was mostly straightforward seeing as Python has the same tools available in other programming languages, namely Regular Expressions.

I personally learned from this assignment that Strings in Python are immutable, meaning that they cannot be directly manipulated like in other languages (Java, C++, etc). I will have to keep this in mind for future assignments.

## Assignment 2 - NLTK Exploration

Link to [Assignment 2](Homework2_msm180010.pdf) and assignment instructions [here](Assignment_2.pdf).

In this assignment, we were introduced to various NLTK functionalities through the use of Google Colab, namely tokenization (word_tokenize() and sent_tokenize()), functions for Text() objects, stemming, and lemmatization.

## Assignment 3 - NLP Application Basics and Word Guessing Game

Link to [Assignment 3](Homework3_msm180010.pdf) and assignment instructions [here](Assignment_3.pdf).

In the first part of this project, we calculated the lexical diversity of a text (which can be found [here](anat19.txt) and performed several operations on the text which included lemmatization and Part of Speech (POS) tagging to find all unique nouns in the text and the number of times each noun appeared in the text.

In the subsequent part of the this project, we utilized the top 50 most frequent nouns from the text to create a word guessing game similar to Hangman or Wheel of Fortune. The user is prompted to input one letter at a time, and their score goes up or down depending on if the letter is in the word or not, respectively. When their score dips below zero, the game is over. The user must attempt to correctly solve as many words as possible.
