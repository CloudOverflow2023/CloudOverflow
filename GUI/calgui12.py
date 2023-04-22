import tkinter as tk
from PIL import ImageTk, Image
import time
import random



counter = 0
# Define the image file paths
image_files = ['testphoto.png', 'testphoto2.png', 'testphoto3.png']
# Define the delay between image changes in milliseconds
delay = 1000

# Create the tkinter window
window = tk.Tk()

# Load the images using Pillow
images = [ImageTk.PhotoImage(Image.open(filename)) for filename in image_files]

# Create the label for the image
image_label = tk.Label(window)

# Define the function to update the image
def update_image(index):
    # Update the image label with the current image
    image_label.configure(image=images[index])
    # Schedule the next image update after the specified delay
    #window.after(delay, update_image, (index + 1) % len(images))

# Start the image loop

n=0
while n < 24:
    update_image(random.randint(0, 2))
    n=n+1
    print(n)
    input("")
    image_label.pack()
    #time.sleep(5)


# Pack the image label into the window
#image_label.pack()

# Start the tkinter event loop

#window.mainloop()

