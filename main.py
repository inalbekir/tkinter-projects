from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("miles to kilometer converter")
window.config(padx=100, pady=100)

miles_input = Entry(width=7)
miles_input.grid(columns=1, row=0)

miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(columns=1, row=1)






window.mainloop()