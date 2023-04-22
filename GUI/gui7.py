import tkinter as tk
import random

def test():

    mylist = ["apple", "banana", "cherry"]
    num = (random.randint(0, 2))
    print(num)
    word = mylist[num]

    return word

class Counter:
    def __init__(self, master):
        self.master = master
        self.counter = 0
        self.label = tk.Label(self.master, text=str(self.counter), font=("Arial", 20))
        self.label.pack(side=tk.LEFT)

        # add image to the frame
        self.img = tk.PhotoImage(file="testphoto.png")
        self.img_label = tk.Label(self.master, image=self.img)
        self.img_label.pack(side=tk.RIGHT, anchor=tk.E)

        # add status label to the frame
        #self.status = ["Charged", "Idle", "Discharge"]
        #self.status = test()
        #self.status_index = 1
        self.status_label = tk.Label(self.master, text=test(), font=("Arial", 20))
        self.status_label.pack()

        # add user input text box to the frame
        self.input_label = tk.Label(self.master, text="User Input:", font=("Arial", 14))
        self.input_label.pack(pady=(20, 5))

        self.input_var = tk.StringVar()
        self.input_var.trace_add('write', self.update_input_label)

        self.input_entry = tk.Entry(self.master, textvariable=self.input_var, font=("Arial", 14))
        self.input_entry.pack()

        self.start_counting()

    def start_counting(self):
        self.counter += 1
        if self.counter > 10:
            self.counter = 0
        self.label.config(text=str(self.counter))
        self.update_status_label()
        self.master.after(1000, self.start_counting)

    def update_status_label(self):
        """self.status_index += 1
        if self.status_index > 2:
            self.status_index = 0"""
        self.status_label.config(text=test())

    def update_input_label(self, *args):
        self.input_label.config(text=f"User Input: {self.input_var.get()}")

root = tk.Tk()
root.title("Counter")

frame = tk.Frame(root)
frame.pack()

counter = Counter(frame)

root.mainloop()
