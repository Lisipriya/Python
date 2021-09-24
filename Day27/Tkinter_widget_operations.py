from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def button_refresh():
    label.config(text="This is new text")

def button_click():
    label.config(text=input.get())
    # button.config(text="Click to refresh", command=button_refresh)

button = Button(text="Click Me", command=button_click)
button.pack()

#Input
input = Entry(width=10)
input.pack()

#Text
text = Text(height=4, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Lisi Priya here I am learning python for 100 days")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=1, to=10, width=3, command= spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#CheckBox
def checkbox_used():
    # Prints 1 if On button checked, otherwise 0.
    print(check_state.get())

#variable to hold on to checked state, 0 is off, 1 is on.
check_state = IntVar()
check_box = Checkbutton(text="Is clicked", variable=check_state, command=checkbox_used)
# check_state.get()
check_box.pack()

#RadioButton
def radiobutton_used():
    print(radio_button_state.get())

#Variable to hold on to which radio button value is checked.
radio_button_state = IntVar()
radio_button1 = Radiobutton(text="Option 1", value=1, variable=radio_button_state, command=radiobutton_used)
radio_button2 = Radiobutton(text="Option 2", value=2, variable=radio_button_state, command=radiobutton_used)

radio_button1.pack()
radio_button2.pack()

#ListBox
def list_box_used(event):
    # Gets current selection from listbox
    print(list_box.get(list_box.curselection()))

list_box = Listbox(height=5)
names = ["lisi", "adhiyan", "visnu", "devi", "pandiarajan"]
for items in names:
    list_box.insert(names.index(items), items)
list_box.bind("<<ListboxSelect>>", list_box_used)
list_box.pack()


window.mainloop()
