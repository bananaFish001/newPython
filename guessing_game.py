import random

# Library that we use in order to choose
# on random words from a list of words

name = input("What is your name? ")
# Here the user is asked to enter the name first

print("Good Luck ! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

# Function will choose one random
# word from this list of words
word = random.choice(words)

print("Guess the characters")

guesses = ''

# Any number of turns can be used here
turns = 12

while turns > 0:
    # Counts the number of times a user fails
    failed = 0

    # All characters from the input
    # word taking one at a time.
    for char in word:
        # Comparing that character with
        # the character in guesses
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")

            # For every failure 1 will be
            # incremented in failure
            failed += 1

    if failed == 0:
        # User will win the game if failure is 0
        # and 'You Win' will be given as output
        print("\nYou Win")
        # This prints the correct word
        print("The word is:", word)
        break

    # If user has input the wrong alphabet then
    # it will ask user to enter another alphabet
    print()
    guess = input("Guess a character: ")

    # Every input character will be stored in guesses
    guesses += guess

    # Check input with the character in word
    if guess not in word:
        turns -= 1

        # If the character doesn’t match the word
        # then “Wrong” will be given as output
        print("Wrong")

        # This will print the number of
        # turns left for the user
        print("You have", turns, 'more guesses')

    if turns == 0:
        print("You Lose")

