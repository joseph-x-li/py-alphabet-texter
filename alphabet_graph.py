import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation


class AlphabetGraph(tk.Frame):
    def __init__(self, parent, figsize, dpi, *args, color="blue", ytop=0.5, interval=100, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._parent = parent
        
        #private data members
        interval = max(100, interval)
        self._times = [0.0 for _ in range(25)]
        self._x = [chr(i) for i in range(98, 123)]
        self._figure, self._ax = plt.subplots(figsize=figsize, dpi=dpi)
        #self._ax is an matplotlib.axes.Axes object
        self._canvas = FigureCanvasTkAgg(self._figure, master=self)
        self._canvas.get_tk_widget().pack(fill="both", expand=True)
        
        self._barcontainer = self._ax.bar(self._x, self._times, color=color)
        #^ is a tuple containing (patches, errorbar), where patches is a list of rectangle objects (where rectangles are artists)
        
        self._ax.set_xlabel("Time To Press")
        self._ax.set_ylabel("Seconds")
        self._ax.set_ylim(bottom=0, top=ytop)
        self._figure.tight_layout()
        
        #animation, 10ms frame speed
        self._anim = FuncAnimation(self._figure, 
                                   self._animate, 
                                   init_func=self._init,
                                   interval=interval, 
                                   blit=True)
    
    def _init(self):
        return self._animate(0)
    
    def _animate(self, i):
        for rect, height in zip(self._barcontainer.patches, self._times):
            rect.set_height(height)
        return self._barcontainer.patches
        
    def set_times(self, times):
        assert(len(times) == 25)
        self._times = times
        return
    
    def reset(self):  #equivalent to setting all times to 0.0
        self._times = [0.0 for _ in range(25)]
        return

        
def main():
    root = tk.Tk()
    AlphabetGraph(root, figsize=(4, 3), dpi=100).pack(side="top", fill="both", expand=True)
    root.mainloop(), 

if __name__ == "__main__":
    main()