import tkinter as tk
from PIL import Image, ImageTk

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

# Create the tkinter window and start the app
root = tk.Tk()
app = PhotoLoopApp(root)
root.mainloop()
