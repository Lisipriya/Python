from tkinter import *

screen = Tk()
screen.title("Mile to Km Converter")
screen.minsize(width=300, height=50)
screen.config(padx=20, pady=20)


def Miles_to_Km():
    converted_value = float(miles_input.get()) * 1.609
    Km_output.config(text=f"{converted_value}")


miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

miles_input = Entry(width=5)
miles_input.focus()
miles_input.grid(column=1, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

Km_output = Label(text="0")
Km_output.grid(column=1, row=1)

Km_label = Label(text="Km")
Km_label.grid(column=2, row=1)

Calculate_button = Button(text="Calculate", command=Miles_to_Km)
Calculate_button.grid(column=1, row=2)

screen.mainloop()
