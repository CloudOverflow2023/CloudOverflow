import tkinter as tk
from PIL import ImageTk, Image
import time
import random

from duck_curve import main_output



counter = 0
# Define the image file paths
image_files = ['discharge.png', 'charging.png', 'full.png']
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
    print(main_output)

n=0
while n < 24:
    #update_image(random.randint(0, 2))
    n=n+1
    print(n)
    input("")
    if main_output[n][1] == 'can discharge':
        update_image(2)
    elif main_output[n][1] == 'can charge':
        update_image(0)
    elif main_output[n][1] == 'idling':
        update_image(1)
    else:
        print("Something went wrong!")

    image_label.pack()
    #time.sleep(5)


# Pack the image label into the window
#image_label.pack()

# Start the tkinter event loop

#window.mainloop()

