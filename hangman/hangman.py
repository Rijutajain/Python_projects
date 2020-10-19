import random

def getWord():
    file= open('wordlist.txt','r')
    words=file.readline().split()
    word=random.choice(words)
    word=word.lower()
    return word

def shouldprint_(word,guessedLetters):
    for char in word:
        if char not in guessedLetters:
            return True
    return False

def isValidInput(guess,guessedLetters):
    if guess in guessedLetters:
        print("you have already guessed it!")
        return False
    elif len(guess)!=1:
        print("you should enter single character!")
        return False
    elif (guess not in ("abcdefghijklmnopqrstuvwxyz") )and guess not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print("you should only enter alphabets!")
        return False
    else:
        return True

def prints(word,guess,guessedLetters):
    for char in word:
        if char in guessedLetters:
            print(char,end=' ')
        else:
            print("_",end=' ')
    if guess not in word:
        print()
        print("letter not in word!")
    print()



def play(word):
    turns=10
    guessedLetters=""
    print("_ "*len(word))
    while turns>0:
        guess=input("Please guess a letter ")
        guess.lower()
        validinput=isValidInput(guess,guessedLetters)
        if validinput==True:
            guessedLetters=guessedLetters+guess
            turns=turns-1
        prints(word,guess,guessedLetters)
        wordisnotcomplete=shouldprint_(word,guessedLetters)
        if wordisnotcomplete==False :
            return True
    return False

def playOutCome(word):
    outcome = play(word)
    if outcome == True:
        print("Congratulations!you won")
    else:
        print("sorry!you lose")


W=getWord()
playOutCome(W)
