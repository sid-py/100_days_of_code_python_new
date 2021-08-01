import pandas as pd
# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


nato_data = pd.read_csv(r"day_26\NATO_project\nato_phonetic_alphabet.csv")

# print(nato_data)

#TODO 1. Create a dictionary in this format:
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
print(nato_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter the word: ").upper()

output_list = [nato_dict[letter] for letter in word]

print(output_list)

