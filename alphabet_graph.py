import tkinter as tk

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class WidthError(Exception):
    """Raised when a list of the wrong length is passed to set_times

    Attributes:
        given -- the given width of the list
        correct -- the correct width of the list
        message -- explanation of the error
    """

    def __init__(self, given, correct, message=""):
        self.message = message
        self.given = given
        self.correct = correct
        super().__init__(self.message)


class AlphabetGraph(tk.Frame):
    FRAME_HEIGHT = 3
    X_SCALE = 5

    def __init__(
        self, parent, dpi, key, *args, color="blue", ytop=0.5, interval=100, **kwargs
    ):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._parent = parent

        # private data members
        interval = max(100, interval)
        self.key = key
        self.key_len = len(key)
        self._times = [0.0 for _ in range(self.key_len - 1)]
        self._x = list(key)[1:]
        self._figure, self._ax = plt.subplots(
            figsize=(self.key_len / self.X_SCALE, self.FRAME_HEIGHT), dpi=dpi
        )
        # self._ax is an matplotlib.axes.Axes object
        self._canvas = FigureCanvasTkAgg(self._figure, master=self)
        self._canvas.get_tk_widget().pack(fill="both", expand=True)

        self._barcontainer = self._ax.bar(self._x, self._times, color=color)
        # ^ is a tuple containing (patches, errorbar), where patches is a list
        # of rectangle objects (where rectangles are artists)

        self._ax.set_xlabel("Time To Press")
        self._ax.set_ylabel("Seconds")
        self._ax.set_ylim(bottom=0, top=ytop)
        self._figure.tight_layout()

        # animation, 10ms frame speed
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
        self._times = times
        return

    def reset(self):
        self._times = [0.0 for _ in range(self.key_len - 1)]
        return


def main():
    root = tk.Tk()
    AlphabetGraph(root, dpi=100, key="abpqrstuvwxyz").pack(
        side="top", fill="both", expand=True
    )
    root.mainloop()


if __name__ == "__main__":
    main()
