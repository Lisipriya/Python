from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)
window.config(padx=100, pady=100)

#Labels
label = Label(text="New Text", font=("Arial", 18, "italic"))
label.grid(column=0, row=0)
# adding extra space
label.config(padx=20, pady=20)

#Buttons
def button_click():
    label.config(text=input.get())

button1 = Button(text="Click Me", command=button_click)
button1.grid(column=1, row=1)

button2 = Button(text="Click Me2", command=button_click)
button2.grid(column=2, row=0)

#Input
input = Entry(width=10)
input.grid(column=3, row=3)

#

window.mainloop()
