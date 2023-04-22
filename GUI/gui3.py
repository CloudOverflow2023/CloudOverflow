import tkinter as tk

class Counter:
    def __init__(self, master):
        self.master = master
        self.counter = 0
        self.label = tk.Label(self.master, text=str(self.counter), font=("Arial", 20))
        self.label.pack()
        self.start_counting()

    def start_counting(self):
        self.counter += 1
        if self.counter > 24:
            self.counter = 0
        self.label.config(text=str(self.counter))
        self.master.after(1000, self.start_counting)

root = tk.Tk()
root.title("Counter")

frame = tk.Frame(root)
frame.pack()

counter = Counter(frame)

root.mainloop()
