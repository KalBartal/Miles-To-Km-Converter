from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)


def button_clicked():
    new_text = round(float(entry.get()) * 1.6)
    result.config(text=new_text)


# Entries
entry = Entry(width=10)
# Add some text to begin with
entry.insert(END, string="0")
# Gets text in entry
print(entry.get())
entry.grid(column=1, row=0)

# Labels
is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)
is_equal_to.config(padx=5, pady=5)

miles = Label(text="Miles")
miles.grid(column=2, row=0)
miles.config(padx=5, pady=5)

result = Label(text="0")
result.grid(column=1, row=1)
result.config(padx=5, pady=5)

km = Label(text="km")
km.grid(column=2, row=1)
km.config(padx=5, pady=5)

# Button
calculate_button = Button(text="calculate", command=button_clicked)
calculate_button.grid(column=1, row=2)

window.mainloop()
