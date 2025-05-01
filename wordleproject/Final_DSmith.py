import csv
# use pip to install colorama via "pip install colorama"
# if that messes anything up try running this file in a folder with a virtual environment (make sure to include the given .csv file)
import colorama
from colorama import Fore, Style
from os import system, name
# from time import sleep # didnt end up using this for clearing


def clearPrint():
    if name == 'nt': # for windows
        _ = system('cls')
    else: # for not windows
        _ = system('clear')
    print(Fore.GREEN + "--- Dylan's Wordle Word Finder (～￣▽￣)～ ---" + Fore.RESET)

def loadBank(filename):
    with open(filename, 'r', newline='') as f:
        return [row[0].lower() for row in csv.reader(f) if row]
    # copied this from the python documentation to load a csv file into a list 

def filterWords(word_bank, green, yellow, gray):
    filtered = []
    for word in word_bank:
        # Check green letters
        # use enumerate to get the index of the letter in the word
        if any(g and word[i] != g for i, g in enumerate(green)):
            continue # use continue instead of break or pass or whatever because i want to check all the letters/words
        # Check gray letters
        if any(letter in word for letter in gray):
            continue # we dont care about the gray letters
        # Check yellow letters
        yellow_fail = False
        for i, yellows in enumerate(yellow):
            for y in yellows:
                if word[i] == y or y not in word:
                    yellow_fail = True
                    break
            if yellow_fail:
                break
        if yellow_fail:
            continue
        filtered.append(word)
    return filtered

def menu():
    print(f'\033]8;;https://www.nytimes.com/games/wordle/index.html\033\\Ctrl Click Me to Play Wordle!\033]8;;\033\\') # googled this formatting so i can have a hyperlink to the website
    print("Welcome to my Wordle Word Finder!")
    print("When Playing, enter a 5 letter word. Then enter your feedback.")
    print(Fore.GREEN + "g for green, " + Fore.YELLOW + "y for yellow," + Fore.WHITE + " and w for wrong/gray letters." + Fore.RESET)
    print(f'Press 1 to begin, or press any other key to quit. Type "Exit" at anytime to exit the program.')
    choice = input("Enter your choice: ")
    if choice == "1":
        main()
    elif choice != "1":
        print(Fore.BLUE + "Ciao!")
        exit()

def main():
    word_bank = loadBank('wordleproject/wordBank.csv') # change this if the csv file or path isn't right -- copy relative path to the csv file from ide -- make sure to open folder rather than just the .py file
    green = [''] * 5
    yellow = [set() for i in range(5)]
    gray = set() # making this a set and not a list prevents duplicates
    wordUnknown = True
    clearPrint()
# indefinite until i find my word
    while wordUnknown:
        guess = input("Enter guess:\n").lower() # make all lowercase so it doesn't break
        feedback = input("Enter feedback (" + Fore.GREEN + "g/green, " + Fore.YELLOW + "y/yellow, " + Fore.WHITE + "w/wrong" + Fore.RESET + "):\n").lower()
        if guess == "exit" or feedback == "exit":
            print(Fore.BLUE + "Ciao!")
            wordUnknown = False
            break
        if len(guess) != 5 or len(feedback) != 5:
            print(Fore.RED + "Invalid input. " + Fore.RESET + "Please enter a 5-letter word and feedback.")
            continue
        for i, (greens, fb) in enumerate(zip(guess, feedback)): # use zip to use both lists at once and use enumerate to get the index
            if fb == 'g':
                green[i] = greens
            elif fb == 'y':
                yellow[i].add(greens)
            elif fb == 'w':
                gray.add(greens)
        word_bank = filterWords(word_bank, green, yellow, gray)
        if len(word_bank) == 1:
            clearPrint()
            print(f'Found word: "{word_bank[0]}"')
            print(Fore.GREEN + "Congrats! You found the wordle!")
            wordUnknown = False
            break
        if len(word_bank) == 0:
            clearPrint()
            print(Fore.RED + "No possible matches.") # sometimes it returns no matches even if there should be some so i just exit the program to reset the lists
            print("Rerun Program and Try Again!" + Fore.RESET)
            wordUnknown = False
            break
        print(f"Possible matches:")
        print(f"{", ".join(word_bank[:10])}{'...' if len(word_bank) > 15 else ''}") # the elipses indicates theres more words. use .join to make it pretty

if __name__ == "__main__":
    clearPrint()
    menu()



""" Sources: 

most of my colorama knowledge came from calc 1 bc of the python projects we did this semester
https://www.w3schools.com/python/ref_func_zip.asp
https://www.w3schools.com/python/ref_func_set.asp
https://www.w3schools.com/python/ref_func_enumerate.asp
https://docs.python.org/3/library/csv.html
https://www.geeksforgeeks.org/clear-screen-python/

https://wordleunlimited.org/ - for testing
https://www.nytimes.com/games/wordle/index.html
"""