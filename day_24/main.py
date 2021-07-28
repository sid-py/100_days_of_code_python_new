with open(r"""C:\Users\2kjph5\OneDrive - Merit Automotive Electronics Systems, S.L\03-Miscellaneous\Studies\Learning\python\100_days_of_code_python_new\day_24\my_file.txt""", mode= "a") as file:
    file.append("\n I am an Engineer")
    
    
    
    
with open(r"""C:\Users\2kjph5\OneDrive - Merit Automotive Electronics Systems, S.L\03-Miscellaneous\Studies\Learning\python\100_days_of_code_python_new\day_24\my_file.txt""", mode= "r") as file:
    content = file.read()

print(content)
