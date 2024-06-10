from tkinter import *


window = Tk()

window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)


def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())


button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)


new_button = Button(text="New Button")
new_button.grid(column=2, row=0)


input = Entry(width=10)
input.grid(column=3, row=2)




window.mainloop()

