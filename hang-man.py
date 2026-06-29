"""
This is a typical hangman game
"""

guessed_letters=[]

stickmen_list=[
    """
    ----|
    |   O
    |  \\|/
    |   |
    |  / \\
    """
    ,
    """
    ----|
    |   O
    |  \\|
    |   |
    |  / \\
    """
    ,
   """
    ----|
    |   O
    |   |
    |   |
    |  / \\
    """
    ,
  """
    ----|
    |   O
    |   |
    |   |
    |  / 
    """
    ,
   """
    ----|
    |   O
    |   |
    |   |
    |   
    """
    ,
   """
    ----|
    |   O
    |   |
    | 
    |   
    """,
    """
    ----|
    |   O
    |  
    |   
    |  
    """
]


def initializes_spaces(word: str):
    #sets the "______" spaces for you to guess the word
    size= len(word)
    spaces=["_" for i in range (0, size)]
    return spaces

def draws_game (word: str)->str:
    print(stickmen_list[0])
    print("\n")
    size= len(word)
    start=["_" for i in range (0, size)]
    print(" ".join(start))
    print("\n")
    



def updates(errors: int, spaces: list)->str:
    if(errors < 7):
        #the next play scenario is determined on your accumulated errors
        print(stickmen_list[errors])
        print("\n")
        print(" ".join(spaces))
        print("\n")

def updates_errors(errors:int)->str:
    errors+=1
    print("you got it wrong :/ \n")
    #simply adds an error and tells the user 
    return errors

def updates_game(spaces: list, word: str, caracter: str):
    found=0
    finished = False
    letra_aux = 0
    #distinguishes between a letter guess and a shot at finding the whole word
    if len(caracter)==1: 
        for index, letter in enumerate(word):
            if letter == caracter and (letter not in guessed_letters):
                spaces[index] = letter
                letra_aux = letter
                found =1
        if letra_aux and (letra_aux not in guessed_letters):
            guessed_letters.append(letra_aux)
    else:
        finished = (caracter == word)
    return found, finished

def verifies_if_should_finish(spaces: list, word: str):
    finished = False
    #if the before-spaces are now the word, the game ends
    #the user won
    if list(word) == spaces: 
        finished = True
    return finished
    

def ends_game():
    print ("You Guessed The Word!! Game over :)\n")
    return 0

def start_game():
    errors = 0
    word = input("Pick a word...\n")
    word = word.lower()
    spaces = initializes_spaces(word)
    draws_game(word)
    while(errors < 7):
        letter = input("Try to guess a letter, or the whole word ;) \n")
        letter = letter.lower()
        guessed, finished= updates_game(spaces, word, letter)
        if finished:
            ends_game()
            return 0
        if guessed == 0:
            errors = updates_errors(errors)
        updates(errors, spaces)
        if guessed == 0:
            print("you got it wrong :/")
        else:
            print("thats right! ;D")
        finished = verifies_if_should_finish(spaces, word)
        if finished:
            ends_game()
            return 0

    print("game over, you lost...\n")
    return 0


start_game()



       
