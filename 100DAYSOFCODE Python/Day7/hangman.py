# Day7 of 100DaysOfPython
# importing the random module
import random
# importing the hangman_word module
import hangman_word
# importing the hangman_art module
import hangman_art

# Updating the word list to use the 'word_list' from hangman_words.py
chosen_word = random.choice(hangman_word.word_list)
# obtaining the length of the chosen word
word_length = len(chosen_word)
# creating a variable called 'end_of_game' and setting it to False
end_of_game = False
# creating a variable called 'lives' and setting it to 6
lives = 6

#Importing the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)


#print(f'Pssst, the solution is {chosen_word}.')

#Creating an empty list called 'display'.
display = []
# For each letter in the chosen_word, add a "_" to 'display'.
for _ in range(word_length):
    # adding a "_" to the display list
    display += "_"
# While end_of_game is not equal to False, the game will continue running.
while not end_of_game:
    # asking the user to guess a letter
    guess = input("Guess a letter: ").lower()
    
    #Check guessed letter
    for position in range(word_length):
        # obtaining the letter at the current position
        letter = chosen_word[position]
        # if the letter at the current position is equal to the letter guessed by the user
        if letter == guess:
            # if the letter is in the display list print the letter
            if letter in display:
              print(f"You've already guessed {letter}")
            else:
              display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"{guess} is not in the word")
        lives -= 1
        # if the user has no more lives, the game ends
        if lives == 0:
            # end the game
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # printing the stages from hangman_art.py
    print(hangman_art.stages[lives])