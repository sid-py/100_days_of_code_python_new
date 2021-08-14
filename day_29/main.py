import tkinter as tk


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    with open(r"day_29\data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password} \n")
    


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
web_entry = tk.Entry(width=35, fg="grey")
#Add some text to begin with
web_entry.insert(0, string="Enter the name of the website" )
#Gets text in web_entry
print(web_entry.get())
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()

email_entry = tk.Entry(width=35, fg = "grey")
#Add some text to begin with
email_entry.insert(0, string="Enter the username/Email")
#Gets text in email_entry
print(email_entry.get())
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = tk.Entry(width=21, fg = "grey")
#Add some text to begin with
password_entry.insert(0, string="Enter the password")
#Gets text in password_entry
print(password_entry.get())
password_entry.grid(column=1, row=3)


#Buttons
def action1():
    print("Do something")

#calls action() when pressed
password_button = tk.Button(text="Generate Password", command=action1)
password_button.grid(column=2, row=3)


#calls action() when pressed
add_button = tk.Button(text="Add", command = save_data, width=36)
add_button.grid(column=1, row=4, columnspan=2)







window.mainloop()
