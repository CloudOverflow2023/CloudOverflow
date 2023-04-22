#Import the required library
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
#Create an instance of tkinter frame
win= Tk()
#Set the geometry
win.geometry("1000x1000")
#Define function to update the image
def update_image():
   canvas.itemconfig(image_container,image=img2)
#Create a canvas and add the image into it
canvas= Canvas(win, width=650, height= 350)
canvas.pack()
#Create a button to update the canvas image
button= ttk.Button(win, text="Update",
command=lambda:update_image())
button.pack()
#Open an Image in a Variable
img1= PhotoImage(file="testphoto.png")
img2= PhotoImage(file="testphoto2.png")
img3= PhotoImage(file="testphoto3.png")
#Add image to the canvas
image_container =canvas.create_image(0,0, anchor="nw",image=img1)

for n in range (0,4):
   print(n)
   input("Test:")
   update_image()
win.mainloop()
