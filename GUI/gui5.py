import tkinter as tk

class Counter:
    def __init__(self, master):
        self.master = master
        self.counter = 0
        self.label = tk.Label(self.master, text=str(self.counter), font=("Arial", 20))
        self.label.pack(side=tk.LEFT)

        # add image to the frame
        self.img = tk.PhotoImage(file="testphoto.png")
        self.img_label = tk.Label(self.master, image=self.img)
        self.img_label.pack(side=tk.RIGHT)

        # add status label to the frame
        self.status = ["Charged", "Idle", "Discharge"]
        self.status_index = 0
        self.status_label = tk.Label(self.master, text=self.status[self.status_index], font=("Arial", 20))
        self.status_label.pack()

        self.start_counting()

    def start_counting(self):
        self.counter += 1
        if self.counter > 10:
            self.counter = 0
        self.label.config(text=str(self.counter))
        self.update_status_label()
        self.master.after(1000, self.start_counting)

    def update_status_label(self):
        self.status_index += 1
        if self.status_index > 2:
            self.status_index = 0
        self.status_label.config(text=self.status[self.status_index])

root = tk.Tk()
root.title("Counter")

frame = tk.Frame(root)
frame.pack()

counter = Counter(frame)

root.mainloop()
