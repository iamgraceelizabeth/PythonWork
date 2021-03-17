## This program allows a user to work with vocabulary words.
# @author: Grace Merry
from random import randint

def main() :
    vocabWords = {}
    getWords(vocabWords, "vocabWords.txt")

    # Menu options
    ADD_WORD = 1
    REMOVE_WORD = 2
    LIST_WORDS = 3
    LIST_WORDS_BY_LETTER = 4
    QUIZ_WORD = 5
    EXIT = 6

    # Continue to process requests until the user decides to exit.
    userChoice = 0
    while (userChoice != EXIT) :
        # Display the menu choices
        print("1) Add word and definition")
        print("2) Remove word")
        print("3) List all words")
        print("4) List words with same first letter")
        print("5) Quiz word")
        print("6) Exit")
        
        # **Prompt for and store the user's choice into userChoice.
        userChoice = int(input("Your chocie: "))
        
        # Depending upon the choice, either add a student/ grade, remove
        # a student, or list all students with their grades in sorted order
        # by their name
        if (userChoice == ADD_WORD) :
            # **Call the addWord function with the vocabulary word list
            addWord(vocabWords)

        elif (userChoice == REMOVE_WORD) :
            # **Call the removeWord function with the vocabulary word list
            removeWord(vocabWords)

        elif (userChoice == LIST_WORDS) :
            # **Call the listWords function with the vocabulary word list
            listWords(vocabWords)
         
        elif (userChoice == LIST_WORDS_BY_LETTER) :
            # **Prompt for and retrieve the letter from the user
            letter = input("Which letter? ")
            
            # **Call the listWordsByLetter function with the 
            # vocabulary word list and the the letter    
            listWordsByLetter(vocabWords, letter)
            
        elif (userChoice == QUIZ_WORD) :            
            # **Call the quizWord function with the vocabulary word list
            quizWord(vocabWords)
            
            
        # Wait until the user wishes to see the menu again    
        if (userChoice != EXIT) :    
            input("\nPress enter to continue")
            print()            
    
    # **Call the storeWords function with the vocabulary word list
    # and the filename "vocabWordsNew.txt"
    storeWords(vocabWords, "vocabWordsNew.txt")
    print("Goodbye")

# **addWord prompts for a new word and defintion and places
# the pair into the vocabularly words list
# @param parWords The current dictionary of vocabulary words
def addWord(parWords):
    newWord = input("Word: ")
    parWords[newWord] = input("Definition: ")
    print("%s added to the list." % (newWord))
        
# **removeWord prompts for a word and removes it from the vocabulary
# words list if it exists, else the user is notified that the word does
# not exist in the list.
# @param parWords The current dictionary of vocabulary words
def removeWord(parWords):
    remove = input("Word to remove: ").lower()
    if remove in parWords:
        parWords.pop(remove)
        print(f"{remove} removed from the list")
    else:
        print(f"{remove} does not exist in the list.")
            
# **listWords displays all the words and their definitions
# in ascending sorted order by words. The format is word: definition
# @param parWords The current dictionary of vocabulary words    
def listWords(parWords):
    for word in sorted(parWords):
        print("%s: %s" % (word, parWords[word]))
        
# **listWordsByLetter displays all the words that being with a particular
# letter and their definitions in sorted order by words. 
# The format is word: definition
# @param parWords The current dictionary of vocabulary words
# @param parLetter The letter which the words must start with
def listWordsByLetter(parWords, parLetters):
    for word in sorted(parWords):
        if word[0] == parLetters:
            print("%s: %s" % (word, parWords[word]))

# **quizWord presents a randomly selected definition to the user, gives a
# hint as to which letter it starts with, and provides up to 3 tries for the
# correct word to be answered. The correct word is displayed if the word
# was not guessed in three tries.
# @param parWords The current dictionary of vocabulary words 
def quizWord(parWords):
    # Set the max number of tries
    MAX_TRIES = 3
    
    # Create a list of only the dictonary's keys
    wordKeys = list(sorted(parWords))
    
    # Generate a random index from the list of keys, get the key at that index, 
    # and get the keys definition
    randomWordIndex = randint(0, len(wordKeys) - 1)
    randomWordKey = wordKeys[randomWordIndex]
    definition = parWords[randomWordKey]
    
    # Start guessing with the limit of tries set in MAX_TRIES
    for i in range(0, MAX_TRIES):
        print("Definition:", definition)
        guess = input("What is the " \
                      f"word? (Begins with {randomWordKey[0]}): ").lower()
        # Display if the users guess was correct or incorrect. If the guess was 
        # incorrect after MAX_TRIES print what the word was.
        i+=1
        if i == 3 and randomWordKey.lower() != guess:
            print("The correct word was:", randomWordKey)
        elif randomWordKey.lower() != guess:
            print("Incorrect")        
        elif randomWordKey.lower() == guess:
            print("Correct")
            break
            
# **storeWords stores the vocabulary list back to file
# The assumed file format for each line is:
# word=defintion
# @param parWords The dictionary of word/definition pairs to store
# @pararm outFileName The name of the file where the new words are stored    
def storeWords(parWords, outFileName):
    outFile = open(outFileName, "w")
    for line in parWords:
        outFile.write(str(line) + "=" + parWords[line] +"\n")
    outFile.close()
    
# getWords retrieves the set of words and their definitions from file
# The assumed file format for each line is:
# word=defintion
# @param parWords Empty dictionary that will store the word/definition pairs
# @param inFilename The name of the file to read
def getWords(parWords, inFileName) :
    inFile = open(inFileName, "r")
    
    # For each line in the file, if it is a valid line with more than
    # one character, strip the trailing newline character,  parse it on
    # the =, and store into the dictionary
    for line in inFile :
        if (len(line) > 1) :
            line = line.rstrip()
            (word, definition) = line.split("=")
            parWords[word] = definition
    
    inFile.close()
    
main()