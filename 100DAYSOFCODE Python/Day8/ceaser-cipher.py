# Day8 100DaysOfPython
# Ceaser Cipher
import art
# created a list called alphabet that contains all the letters of the English alphabet.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caeser(direction, text, shift):
      letters = []
      # creating a for loop that loops through each letter in the text
      for letter in text:
             # creating a variable called letter_index that stores the index of the letter in the alphabet list
            letter_index = alphabet.index(letter)
            if direction == "encode":
                  # creating an if statement that checks if the letter is in the alphabet list
                  if letter in alphabet:
                        # creating an if statement that checks if the shift is greater than 26
                        if shift > 26:
                              print("The shift number is too high. It has to be less than 26.")
                              # asking the user to input the shift number again
                              shift = int(input("Type the shift number again:\n"))
                        # creating a variable called new_position that stores the sum of the letter_index and the shift
                        new_position = shift + letter_index
                          # creating an if statement that checks if the new_position is less than or equal to the length of the alphabet list
                        if new_position <= len(alphabet):
                          # if the if statement is true, then the letter at the new_position in the alphabet list is added to the letters list
                          letters += alphabet[new_position]
                          # creating an else statement that runs if the if statement is false
                        else:
                          # creating an if statement that checks if the shift is greater than 26
                          if shift > 26:
                                # if the if statement is true, then the user is asked to input the shift number again
                                print("The shift number is too high. It has to be less than 26.")
                                # asking the user to input the shift number again
                                shift = int(input("Type the shift number again:\n"))
                          # if the else statement runs, then the letter at the new_position - the length of the alphabet list is added to the letters list
                          letters += alphabet[shift - ((len(alphabet) - 1) - letter_index) - 1]

                  else:
                        # if the letter is not in the alphabet list, then it is added to the letters list
                        letters += letter 
            # creating an else statement that runs if the direction is not encode
            elif direction == "decode":
                  # creating an if statement that checks if the letter is in the alphabet list
                  if letter in alphabet:
                        # creating an if statement that checks if the shift is greater than 26
                      if shift > 26:
                            # if the if statement is true, then the user is asked to input the shift number again
                            print("The shift number is too high. It has to be less than 26.")
                            #  asking the user to input the shift number again
                            shift = int(input("Type the shift number again:\n"))
                      # creating a variable called new_position that stores the difference of the letter_index and the shift
                      new_position = letter_index - shift
                      # selecting the letter at the new_position in the alphabet list and adding it to the letters list
                      letters += alphabet[new_position]
                  else:
                        # if the letter is not in the alphabet list, then it is added to the letters list
                        letters += letter
            # creating a variable called decoded_text that stores the joined letters list
            final_text = "".join(letters)
      # printing the direction and the final text which is either encoded or decoded
      print(f"The {direction}d is {final_text}")
# calling the caeser function and passing in the direction, text and shift as arguments
# displaying the caeser art to the user
print(art.logo)
# creating a variable called response that stores the string "yes"
response = "yes"
# creating a while loop that runs while the response is equal to "yes"
while response == "yes":
      # asking the user to choose between encoding or decoding
      direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
      # asking the user to input the text they want to encrypt or decrypt
      text = input("Type your message:\n").lower()
      # asking the user to input the shift number they want to use
      shift = int(input("Type the shift number:\n"))
      # creating a function called encrypt that takes the 'text' and 'shift' as inputs.                                       
      caeser(direction, text, shift)
      # asking the user if they want to go again
      response = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n").lower()
print("Thanks for using the Ceaser Cipher. Goodbye!")