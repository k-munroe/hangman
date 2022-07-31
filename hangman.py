import random
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.random(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Please guess a letter:\n").lower

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letters in chosen_word:
    for guessed_letter in guess:
        if guess[guessed_letter] == chosen_word[letters]:
            print("You guessed right!")
        else:
            print("You guessed incorrectly :(")