import tkinter as tk

from tkinter import Text, Label, Button



root = tk.Tk()

# specify size of window.
root.geometry("250x170")

# Create text widget and specify size.
T = Text(root, height = 5, width = 52)

# Create label
l = Label(root, text = "Power Chart")
l.config(font =("Courier", 14))

Fact = """A man can be arrested in
Italy for wearing a skirt in public."""
#root.update()

Fact = """test 2"""


l.pack()
T.pack()


# Insert The Fact.
T.insert(tk.END, Fact)

tk.mainloop()