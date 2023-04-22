import tkinter as tk
import random
from PIL import Image, ImageTk

def GetChargeStatus():
    

    mylist = ["apple", "banana", "cherry"]
    num = (random.randint(0, 2))
    print(num)
    word = mylist[num]

    return word

class PhotoLoopApp:
    def __init__(self, master):
        self.master = master
        self.images = []
        self.current_image = 0

        # Load the images
        self.load_images()

        # Create a label to display the images
        self.image_label = tk.Label(self.master)
        self.image_label.pack()

        # Start the loop
        self.loop_images()

    def load_images(self):
        # Load the images using Pillow
        self.images.append(ImageTk.PhotoImage(Image.open("testphoto.png")))
        self.images.append(ImageTk.PhotoImage(Image.open("testphoto2.png")))
        self.images.append(ImageTk.PhotoImage(Image.open("testphoto3.png")))

    def loop_images(self):
        # Display the current image
        self.image_label.config(image=self.images[self.current_image])

        # Increment the current image index
        self.current_image += 1

        # Loop back to the first image if we've reached the end
        if self.current_image >= len(self.images):
            self.current_image = 0

        # Schedule the next iteration of the loop
        self.master.after(2000, self.loop_images)


class Counter:
    def __init__(self, master):
        self.master = master
        self.counter = 0
        self.label = tk.Label(self.master, text=str(self.counter), font=("Arial", 20))
        self.label.pack(side=tk.LEFT)

        
    
        self.status_label = tk.Label(self.master, text=GetChargeStatus(), font=("Arial", 20))
        self.status_label.pack()

        

        self.input_var = tk.StringVar()
        self.input_var.trace_add('write', self.update_input_label)

    
        self.start_counting()

    def start_counting(self):
        self.counter += 1
        if self.counter > 10:
            self.counter = 0
        self.label.config(text=str(self.counter))
        self.update_status_label()
        self.master.after(1000, self.start_counting)

    def update_status_label(self):
        self.status_label.config(text=GetChargeStatus())

    def update_input_label(self, *args):
        self.input_label.config(text=f"User Input: {self.input_var.get()}")

root = tk.Tk()
root.title("Counter")

frame = tk.Frame(root)
frame.pack()

counter = Counter(frame)


app = PhotoLoopApp(root)

root.mainloop()
