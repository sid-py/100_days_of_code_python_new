sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

words_in_sentence = sentence.split(" ")
print(words_in_sentence)

result = {word: len(word) for word in words_in_sentence}


print(result)