import tkinter as tk

import tkinter

from PIL import ImageTk, Image  

#image1 = Image.open("testphoto.png")

#image1 = Image.resize((50, 50), Image.ANTIALIAS)


root = tk.Tk()

# Create a photoimage object of the image in the path
image1 = Image.open("testphoto.png")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

# Position image
label1.place(x=10, y=10)
root.mainloop()

