import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation


class AlphabetGraph(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        

if __name__ == "__main__":
    root = tk.Tk()
    AlphabetGraph(root).pack(side="top", fill="both", expand=True)
    root.mainloop()