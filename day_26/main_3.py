with open(r"C:\Users\2kjph5\OneDrive - Merit Automotive Electronics Systems, S.L\03-Miscellaneous\Studies\Learning\python\100_days_of_code_python_new\day_26\file1.txt") as file1:
    file_1_data = file1.readlines()
   
    
with open(r"C:\Users\2kjph5\OneDrive - Merit Automotive Electronics Systems, S.L\03-Miscellaneous\Studies\Learning\python\100_days_of_code_python_new\day_26\file2.txt") as file2:
    file_2_data = file2.readlines()


result = [int(n) for n in file_1_data if n in file_2_data]


# Write your code above 👆

print(result)