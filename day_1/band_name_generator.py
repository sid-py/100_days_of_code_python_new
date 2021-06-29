#1. Create a greeting for your program.
print(">> Welcome to Band Name generator <<")

#2. Ask the user for the city that they grew up in.
city_name = input("Enter the name of the city you grew up: \n" )
#3. Ask the user for the name of a pet.
pet_name = input("Enter the name of your pet: \n")

#4. Combine the name of their city and pet and show them their band name.
print("The name of your band should be: \n" + city_name.upper() + " " + pet_name.upper())

#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/