#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
PLACEHOLDER = "[name]"       

# TODO 1: Open starting_letter and read the contents
with open(r"C:\Users\2kjph5\OneDrive - Merit Automotive Electronics Systems, S.L\03-Miscellaneous\Studies\Learning\python\100_days_of_code_python_new\day_24\Mail Merge Project Start\Input\Names\invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()


    
# TODO 2: Open invited_names and read contents

with open(r"C:\Users\2kjph5\OneDrive - Merit Automotive Electronics Systems, S.L\03-Miscellaneous\Studies\Learning\python\100_days_of_code_python_new\day_24\Mail Merge Project Start\Input\Letters\starting_letter.txt", mode = "r+") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"day_24\Mail Merge Project Start\Output\ReadyToSend\letter_for_{stripped_name}.txt", mode= "w") as completed_letter:
            completed_letter.write(new_letter)
        

     

    

