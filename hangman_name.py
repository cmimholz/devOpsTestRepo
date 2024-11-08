HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
# TODO: Where should we load the packages

import random

def get_random_number(x):
    # Create a list from 0 to x
    numbers = list(range(x + 1))
    # Select a random element from the list
    return random.choice(numbers)

# Define the word bank as a constant outside the function
WORDS = (
    'ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 
    'cobra', 'cougar', 'coyote', 'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle', 
    'ferret', 'fox', 'frog', 'goat', 'goose', 'hawk', 'lion', 'lizard', 'llama', 
    'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt', 'otter', 'owl', 'panda', 
    'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven', 'rhino', 'salmon', 
    'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider', 'stork', 'swan', 
    'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel', 'whale', 'wolf', 'wombat', 
    'zebra'
)

def get_word():
    """Return a random word from the WORDS tuple."""
    return random.choice(WORDS)

def get_letter_indixes(word):
    indices = {}
    for index, letter in enumerate(word):
        if letter in indices:
            indices[letter].append(index)
        else:
            indices[letter] = index
    return indices

def main():
    print("Welcome to the HANGMAN Game:")

    counter = 0
    word = get_word()
    print(f"We just selected a word for u: {word}")
    

    letters = list(word)
    word_length = len(letters)
    unique_lettters = sorted(unique_letters)
    word_completed_counter = 0

    state = True
    while state == True:
        print("Current Status:")
        print(HANGMANPICS[counter])
        letter = input("Enter a letter\n").lower()

        if letter in letters:
            print("SUCCESSFUL")
        elif counter == word_length:
            print("YOU JUST DIED")
            print(HANGMANPICS[counter])
            print(f"The correct word was {word}")
            state = False
        elif word_completed_counter == len(unique_lettters):
            print("YOU WON")
            print() #TODO: Print state of word
        else:
            print("WRONG CHOICE")
            counter += 1


if __name__ == "__main__":
    main()
