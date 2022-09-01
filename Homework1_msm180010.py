
# CS 4395.001 - Assginment 1
# Michael Menjivar, msm180010

import sys
import os
import re
import pickle

class Person:
    last = ""
    first = ""
    mi = ''
    id = ""
    phone = ""

    def __init__(self, last, first, mi, id, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.id = id
        self.phone = phone
    def display(self):
        print("Employee id: " + self.id)
        print("\t" + self.first + " " + self.mi + " " + self.last)
        print("\t" + self.phone + "\n")

def processFile(filePath):

    # Open file and create a list with each line from file.
    current_dir: str = os.getcwd()
    dataFile = open(os.path.join(current_dir, filepath), 'r')
    dataFileLines = dataFile.readlines()

    # Remove newLine(s)
    for line in dataFileLines:
        line = line.strip("\n")
        # print(str(count) + ": " + line)

    # Remove first line
    dataFileLines.pop(0)

    # Split lines by comma and add into new list.
    splitList = []
    for line in dataFileLines:
        splitList.append(line.split(","))

    # Iterate through each line from the data file, process, and add to dict
    employees = dict()
    for line in splitList:

        # Capitalize First and Last name
        line[0] = line[0].capitalize()
        line[1] = line[1].capitalize()

        # Check for Middle initial; capitalize if present, else subsiture for 'X'.
        if line[2]:
            line[2] = line[2].upper()
        else:
            line[2] = 'X'

        # Modify ID if formatted incorrectly using Regex.
        while not re.search("^[A-Z]{2}[0-9]{4}$", line[3]):
            print("ID invalid: " + line[3])
            print("ID is two letters followed by 4 digits")
            line[3] = input("Please enter a valid id: ").strip("\n")
            line[3].capitalize()
        line[3] = line[3].strip("\n")

        # Modify Phone Number if formatted incorrectly using Regex.
        while not re.search("^\d{3}((\-\d{3}\-)|(\.\d{3}\.)|(\s\d{3}\s)|(\d{3}))\d{4}$", line[4]):
            print("Phone " + line[4].strip() + " is invalid")
            print("Enter phone number in form 123-456-7890")
            line[4] = input("Enter phone number: ").strip("\n")
        line[4] = line[4].strip("\n")

        # Reformat Phone number to match 123-456-7890 format (dashes) if already in acceptable format
        if "-" not in line[4] and "." not in line[4] and ' ' not in line[4]:  # Check if Phone is just numbers
            count = 0
            newPhone = ""
            for digit in line[4]:
                newPhone += digit
                if count == 2 or count == 5:
                    newPhone += '-'
                count+=1
            line[4] = newPhone
        elif '-' not in line[4]:   # If phone contains characters other than numbers...
            splitPhoneList = []
            if '.' in line[4]:  # split on periods
                splitPhoneList = line[4].split(".")

            elif ' ' in line[4]:   # split on whitespace
                splitPhoneList = line[4].split(" ")

            temp = ""
            temp = temp + splitPhoneList[0] + '-' + splitPhoneList[1] + '-' + splitPhoneList[2]
            line[4] = temp

        # Create Person object using data from each Line
        newPerson = Person(line[0],line[1],line[2],line[3],line[4])

        # Add Person to dict if not a duplicate
        if newPerson.id not in employees:
            employees.update({newPerson.id:newPerson})
        else:
            print("Duplicate ID error. Employee with ID [ " + newPerson.id + " ] already exists.")

    return employees

if __name__ == '__main__':
    if len(sys.argv) < 2:
        # No sysarg given to open data file.
        print('Please enter a filename as a system arg')
    else:
        # Process, reformat, and write data to a dict.
        filepath = sys.argv[1]
        employees = processFile(filepath)

        # Pickle data; write to file.
        pickle.dump(employees, open('employees.p', 'wb'))

        # Unpickle data; read from file.
        employees_in = pickle.load(open('employees.p', 'rb'))

        # Display employee information.
        print("\n\nEmployee list:\n")
        for key,value in employees_in.items():
            value.display()





