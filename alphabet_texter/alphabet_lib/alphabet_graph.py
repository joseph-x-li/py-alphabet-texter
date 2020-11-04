import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class AlphabetGraph(tk.Frame):
    frame_height = 3  # inches
    x_scale = 4
    bar_color = "blue"

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
        self._ylim = ylim
        self._interval = max(100, interval)
        self._dpi = dpi
        self._make_internals(parent, dpi, key, ylim, interval)

    def _make_internals(self, parent, dpi, key, ylim, interval):
        self.key = key
        self.key_len = len(key)
        self.times = [0.0 for _ in range(self.key_len - 1)]
        self._x = (list(key))[1:]
        self._figure, self._ax = plt.subplots(
            figsize=(self.key_len / self.x_scale, self.frame_height), dpi=dpi
        )
        # self._ax is an matplotlib.axes.Axes object
        self._canvas = FigureCanvasTkAgg(self._figure, master=self)
        self._canvas.get_tk_widget().pack(fill="both", expand=True)

        # str necessary to prevent scalar x-axis
        xticks = [str(i) for i in range(self.key_len - 1)]

        self._barcontainer = self._ax.bar(
            x=xticks, height=self.times, color=self.bar_color
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
        for rect, height in zip(self._barcontainer.patches, self.times):
            rect.set_height(height)
        return self._barcontainer.patches

    def set_times(self, times):
        """Sets times on the time graph.

        Args:
            times (List[float]): List of length self.key_len with non-negative times 
            for each interval.
        """
        self.times = times

    def set_key(self, new_key):
        self._canvas.destroy()
        self._make_internals(
            self._parent, self._dpi, new_key, self._ylim, self._interval
        )

    def reset(self):
        """Resets all times to 0.0.
        """
        self.times = [0.0 for _ in range(self.key_len - 1)]


def main():
    root = tk.Tk()
    AlphabetGraph(root, dpi=100, key="1123 455").pack(
        side="top", fill="both", expand=True
    )
    root.mainloop()


if __name__ == "__main__":
    main()
