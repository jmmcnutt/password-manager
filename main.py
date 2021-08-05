from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "!", "@", "#", "$", "%", "^", "&",
                "*", "(", ")", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                'X', 'Y', 'Z']

    password = ""

    for i in range(10):
        new_char = random.choice(alphabet)
        password += str(new_char)

    password_entry.delete(0, END)
    password_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    saved_website = website_entry.get()
    saved_email = email_entry.get()
    saved_password = password_entry.get()

    if len(saved_password) == 0 or len(saved_email) == 0 or len(saved_website) == 0:
        messagebox.showerror("Oops", "Please fill in all fields")
    else:

        is_ok = messagebox.askokcancel(title=saved_website,
                                       message=f"These are the details you have entered: \nEmail: {saved_email} "
                                               f"\nPassword: {saved_password} \nIs it ok to save?")

        if is_ok:
            with open("password.txt", mode="a") as file:
                file.write(f"\n{saved_website} | {saved_email} | {saved_password}")

            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img, )
canvas.grid(column=1, row=0, )

# website label

website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="e", pady=(2, 2))

# Email/Username label

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky="e", pady=(2, 2))

# Password label

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="e", pady=(2, 2))

# Website Entry

website_entry = Entry(width=51)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# Email/Username Entry

email_entry = Entry(width=51)
email_entry.grid(column=1, row=2, columnspan=2)


# Password Entry

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

# Password Button

password_button = Button(text="Generate Password", width=14, command=password_generator)
password_button.grid(column=2, row=3, sticky="w", padx=(1, 0))

# Add Button

Add_button = Button(text="Add", width=25, command=save)
Add_button.grid(column=0, row=4, columnspan=3, pady=(4, 2))

window.mainloop()
