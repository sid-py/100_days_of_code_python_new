import pandas as pd

nato_data = pd.read_csv(r"day_26\NATO_project\nato_phonetic_alphabet.csv")

# print(nato_data)

#TODO 1. Create a dictionary in this format:
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
print(nato_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    word = input("Enter the word: ").upper()
    try:
        output_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()