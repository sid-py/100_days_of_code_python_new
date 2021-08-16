import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_letters = [random.choice(letters) for _ in range(random.randint(8,10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(8,10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(8,10))]

    password_list = password_letters + password_numbers + password_symbols
    # print(password_list)
    random.shuffle(password_list)
    # print(password_list)

    password = "".join(password_list)
    password_entry.insert(0 , password)
    
    pyperclip.copy(password)
    
    





# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven'e left any field empty!")
    
    else:
        try:
            with open(r"day_29\data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        # Error handling
        except FileNotFoundError:
            with open(r"day_29\data.json", "w") as data_file:
                json.dump(new_data, data_file, indent = 4)
            
        else:
            # Updating old data with the new data
            data.update(new_data)
                
            with open(r"day_29\data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent = 4)
        
        finally:        
            web_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
    

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def find_password():
    website = web_entry.get()
    with open(r"day_29\data.json", "r") as data_file:
        # Reading old data
        data = json.load(data_file)
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title = website, message= f" Email: {email} \n Password: {password}")
            
    

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx= 40, pady=40)

canvas = tk.Canvas(width = 200, height = 200, highlightthickness = 0)
lock_img = tk.PhotoImage(file = r"day_29\logo.png")
canvas.create_image(100, 100, image = lock_img)
canvas.grid(column = 1, row = 0)


#Labels

website = tk.Label(text="Website")
website.grid(column = 0, row = 1)

email = tk.Label(text = "Email/Username:")
email.grid(column= 0, row = 2)

password = tk.Label(text = "Password: ")
password.grid(column= 0, row = 3)

#Entries
web_entry = tk.Entry(width=21)
#Add some text to begin with
web_entry.insert(0, string="" )
#Gets text in web_entry
print(web_entry.get())
web_entry.grid(column=1, row=1,)
web_entry.focus()

email_entry = tk.Entry(width=35)
#Add some text to begin with
email_entry.insert(0, string="siddhesh.sule47@gmail.com")
#Gets text in email_entry
print(email_entry.get())
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = tk.Entry(width=21)
#Add some text to begin with
password_entry.insert(0, string="")
#Gets text in password_entry
print(password_entry.get())
password_entry.grid(column=1, row=3)



# Generate passowrd button
password_button = tk.Button(text="Generate Password", command = generate_password)
password_button.grid(column=2, row=3)

# Add button
add_button = tk.Button(text="Add", command = save_data, width=36)
add_button.grid(column=1, row=4, columnspan=2)

# Search button
search_button = tk.Button(text = "Search",width = 14, command= find_password)
search_button.grid(column=2, row = 1)






window.mainloop()
