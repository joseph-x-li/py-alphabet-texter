import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class AlphabetGraph(tk.Frame):
    FRAME_HEIGHT = 3  # inches
    X_SCALE = 4
    BAR_COLOR = "blue"

    def __init__(self, parent, dpi, key, *args, ylim=0.5, interval=100, **kwargs):
        """Initializes AlphabetGraph object.

        Args:
            parent (tk.Frame): parent tkinter frame.
            dpi (int): Dots-per-inch of resulting object.
            key (string): Comparison string.
            ylim (float, optional): Y-limit of resulting graph. Defaults to 0.5.
            interval (int, optional): Update interval, in milliseconds. 
                Values below 100 will default to 100. Defaults to 100.
        """
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._parent = parent

        # private data members
        interval = max(100, interval)
        self.key = key
        self.key_len = len(key)
        self._times = [0.2 for _ in range(self.key_len - 1)]
        self._x = (list(key))[1:]
        self._figure, self._ax = plt.subplots(
            figsize=(self.key_len / self.X_SCALE, self.FRAME_HEIGHT), dpi=dpi
        )
        # self._ax is an matplotlib.axes.Axes object
        self._canvas = FigureCanvasTkAgg(self._figure, master=self)
        self._canvas.get_tk_widget().pack(fill="both", expand=True)

        xticks = [
            str(i) for i in range(self.key_len - 1)
        ]  # str necessary to prevent number line x-axis
        self._barcontainer = self._ax.bar(
            x=xticks, height=self._times, color=self.BAR_COLOR
        )
        # ^ is a tuple containing (patches, errorbar), where patches is a list
        # of rectangle objects (where rectangles are artists)
        
        self._ax.set_xticklabels(self._x) 
        self._ax.set_xlabel("Time To Press")
        self._ax.set_ylabel("Seconds")
        self._ax.set_ylim(bottom=0, top=ylim)
        self._figure.tight_layout()

        self._anim = FuncAnimation(
            self._figure,
            self._animate,
            init_func=self._init,
            interval=interval,
            blit=True,
        )

    def _init(self):
        return self._animate(0)

    def _animate(self, i):
        for rect, height in zip(self._barcontainer.patches, self._times):
            rect.set_height(height)
        return self._barcontainer.patches

    def set_times(self, times):
        """Sets times on the time graph.

        Args:
            times (List[float]): List of length self.key_len with non-negative times 
            for each interval.
        """
        self._times = times

    def reset(self):
        """Resets all times to 0.0.
        """
        self._times = [0.0 for _ in range(self.key_len - 1)]


def main():
    root = tk.Tk()
    AlphabetGraph(root, dpi=100, key="a b c d e").pack(
        side="top", fill="both", expand=True
    )
    root.mainloop()


if __name__ == "__main__":
    main()
