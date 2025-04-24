import csv
with open('wordleproject/word-bank.csv', newline='') as wordleCSV:
    words = csv.reader(wordleCSV, delimiter='\n', quotechar=' ')
#    dataTable = list(words)


    # making csv a list to call
# test function to print out any word
# def bankCheck():
#     # i is to pick a word from dataTable
#     i = int(input("Enter a number between 0 and 2316"))
#     while i > 0:
#         print("".join(dataTable[i]))
#         i = int(input())
dataTable = ['hello', 'world', 'tests', 'words', 'child', 'place', 'tanks']

invalidLetters = []
invalidInput = ""
while invalidInput != "quit":
    invalidInput = str(input("Enter a letter that is not in the word: "))
    if invalidInput == "quit":
        break
    else:
        invalidLetters.append(invalidInput)
        print(invalidLetters)

def removeGreyWords():
    for word in dataTable:
        for letter in invalidLetters:
            if letter in word:
                dataTable[dataTable.index(word)] = ''
    while "" in dataTable:
        dataTable.remove("")
    print(dataTable)

removeGreyWords()