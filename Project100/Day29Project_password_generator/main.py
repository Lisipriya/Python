from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter = [choice(letters) for char in range(randint(6, 8))]
    symbol = [choice(symbols) for char in range(randint(2, 4))]
    number = [choice(numbers) for char in range(randint(2, 4))]

    password_list = letter + symbol + numbers
    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website_entry.get()
    mail = email_entry.get()
    pwd = password_entry.get()
    pop_up = bool

    if len(web) == 0 or len(mail) == 0 or len(pwd) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")

    else:
        confirmation_msg = f"These are the details entered\n Email Id/Username: {mail} \n Password: {pwd}"
        pop_up = messagebox.askokcancel(title=web, message=confirmation_msg)


    if pop_up:
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        f = open("data.txt", "a")
        f.write(f"{web} | {mail} | {pwd}\n")
        f.close()


# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("Password Generator")
windows.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_label = Label(text="Email Id/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.insert(0, "test@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=17)
password_entry.place(x=111, y=247)

generate_pwd_button = Button(text="Generate Password", command=password_generator)
generate_pwd_button.place(x=217, y=245)
# generate_pwd_button.grid(row=3, column=2)

add_button = Button(text="Add", width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2)

windows.mainloop()
