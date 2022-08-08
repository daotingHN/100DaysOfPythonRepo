from tkinter import *


def calculate_clicked():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_conversion_label.config(text=f"{km}")



window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=15, pady=15)

# Labels
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

km_conversion_label = Label(text=0)
km_conversion_label.grid(column=1, row=1)

# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Button
button = Button(text="Calculate", command=calculate_clicked)
button.grid(column=1, row=2)


# Must be at the very end
window.mainloop()

