# Importing the logo from art file
from art_ceaser_cipher import logo

# Defining list of alphabets
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction): # Defining function for Ceaser Cipher
    """ This is a simple cipher game to encode- decode messages. 
    It affects only the alphabets. Other characters like spaces, 
    numbers and symbols stays the same"""
    end_text = "" # Defining a variable end_text for strings
    if cipher_direction == "decode": # Condition for decoding
        shift_amount *= -1 # Shift decrement
    for char in start_text: # For loop to loop ove rthe start_text variable
        if char in alphabet: # If condition for each char in alphabet
            position = alphabet.index(char) # position variable definition
            new_position = position + shift_amount # new_position variable with shift increment
            end_text += alphabet[new_position] # end_text definition
        else:
            end_text += char # The condition with else
        
    print(f"Here's the {cipher_direction}d result: {end_text}") # Printing the cipher

print(logo) # printing the logo from the art module

should_continue = True # An intermediate variable for the while loop

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n") # User input
    text = input("Type your message:\n").lower() # User input
    shift = int(input("Type the shift number:\n")) # User input

    shift = shift % 26 # To prevent out of range error with the list
        
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction) # ceaser function call
    result = input("Type 'yes to continue and 'no' to exit the cipher: \n") # result variable to take user inout about continuing the game
    if result == "no": # if clause for the result input
        should_continue = False # change of should_continue variable
        print("Goodbye!") # printing final message at the exit
        # Program ends!

            


