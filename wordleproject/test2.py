import csv
# might not work on not windows because of the backslash
with open('wordleproject/word-bank.csv', newline='') as wordleCSV:
    words = csv.reader(wordleCSV, delimiter='\n', quotechar=' ')
    dataTable = list(words)
    # making csv a list to call
def bankCheck():
    # i is to pick a word from dataTable
    i = int(input("Enter a number between 0 and 2316"))
    while i > 0:
        print("".join(dataTable[i]))
        i = int(input())


def wordInput(x):
    brokeWord = list(userWord)
    print(brokeWord)

# use a loop to look for strings that contain a specific letter 
for letter in dataTable:
    pass

# use a list/dict and list.append to keep a list of possible words that it could be 

if __name__ == "__main__":
    userWord = str(input("Enter "))
    wordInput(userWord)
    bankCheck()





""" enter green letters 
    enter position of green letter (1-5)

    enter yellow letters
    enter position of yellow letters (1-5)

    enter grey letters that are not in the word 
    
"""

""" grey letters

"""

""" yellow letters
"""