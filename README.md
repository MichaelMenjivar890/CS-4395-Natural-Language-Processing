# CS-4395-Natural-Language-Processing
### *Michael Menjivar*
Repository for CS 4395 assignments/projects.

## Assignment Zero
Link to [Assignment 0 - Porfolio Setup](CS_4395_-_Assignment_0.pdf).

## Assignment 1
Link to [Assignment 1 - Portfolio Assignment 1](Homework1_msm180010.py).

The program reads in a .csv file, processes the employee information stored in said file, stores information in a pickle file, and reads/outputs formatted data from the pickle file.

To run: download the .py file, place the .csv file with the employee data in a folder named "data", and move data to the directory where the .py file is stored. Make sure that the Natural Language Tool Kit (NLTK) is installed on your device before running in the Terminal/Command Line.
Then, run the .py file with the command "python [.py file] data/[.csv file]", where [.py file] is the name of the Python file you run and [.csv file] is the file with the employee data as a sysarg (system argument). If no data file is used as a sysarg, an error will be returned.

While the simplicity of Python syntax makes text processing simpler, there are certain issues I had while implementing this program that stuck out to me as Python specific. Mainly, how I was unable to easily iterate directly through a String in the same manner as an Array in other languages, making inserting characters (specifically '-' while formatting phone numbers) slightly more complex. However, the process was mostly straightforward seeing as Python has the same tools available in other programming languages, namely Regular Expressions.

I personally learned from this assignment that Strings in Python are immutable, meaning that they cannot be directly manipulated like in other languages (Java, C++, etc). I will have to keep this in mind for future assignments.
