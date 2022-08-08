from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")  # Alternatively: my_label["text"] = "New Text"
# my_label.pack(side="left")
# my_label.place(x=150, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

# Button
button = Button(text="Button", command=button_clicked)  # Naming, not calling function. No need ()
button.grid(column=1, row=1)

# New Button
button = Button(text="New Button")
button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=3)



# Must be at the very end
window.mainloop()
