import soundmeter
import tkinter as tk
import time

class App():
    def __init__(self):
        self.spl = soundmeter.soundmeter()

        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.pack()
        self.root.title('Lärm')
        self.update_clock()
        self.root.mainloop()
        

    def update_clock(self):
        pegel = self.spl.get_spl()
        now = str(pegel)+" dBA"
        self.label.configure(text=now, font=('Helvetica', 100))
        if pegel > 75:
            self.label.configure(bg='red')
            self.root.configure(bg='red')
        else:
            self.label.configure(bg='green')
            self.root.configure(bg='green')
        self.root.after(500, self.update_clock)

app=App()