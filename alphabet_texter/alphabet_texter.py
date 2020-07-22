import tkinter as tk

from alphabet_lib import alphabet_display
from alphabet_lib import alphabet_graph
from alphabet_lib import alphabet_utils

import random  # for string shuffling


class AlphabetTexter(tk.Frame):
    MASTER_FONT = "Menlo"
    KEY_DICT = {
        "(A-Z)": "abcdefghijklmnopqrstuvwxyz",
        "(Z-A)": "zyxwvutsrqponmlkjihgfedcba",
        "(A-Z), With Spaces": "a b c d e f g h i j k l m n o p q r s t u v w x y z",
        "(Z-A), With Spaces": "z y x w v u t s r q p o n m l k j i h g f e d c b a",
        "Random": None,
    }
    KEY_OPTIONS = [
        "(A-Z)",
        "(Z-A)",
        "(A-Z), With Spaces",
        "(Z-A), With Spaces",
        "Random",
    ]

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(
            self,
            parent,
            *args,
            bg="red",
            highlightthickness=1,
            highlightbackground="black",
            **kwargs,
        )
        self._parent = parent

        self.au = alphabet_utils.AlphabetUtils(key=self.KEY_DICT["(A-Z)"])
        self.make_internals(self)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

    def make_internals(self, parent_frame):
        self.title = tk.Label(
            parent_frame,
            text="Alphabet Texter: Python Edition",
            font=(self.MASTER_FONT, 24),
            bg="green",
            relief="ridge",
        )
        self.title.grid(row=0, column=0, sticky="news", ipady=5, ipadx=5)

        self.graph = alphabet_graph.AlphabetGraph(
            parent_frame, dpi=100, key=self.KEY_DICT["(A-Z)"], interval=150,
        )
        self.graph.grid(row=1, column=0, sticky="news")

        self.display = alphabet_display.AlphabetDisplay(
            parent_frame, key=self.KEY_DICT["(A-Z)"]
        )
        self.display.grid(row=2, column=0, sticky="ns", ipadx=5, ipady=5)

        self.input_var = tk.StringVar()
        self.input_var.trace("w", self.on_keystroke)

        self.text_entry = tk.Entry(
            parent_frame, textvariable=self.input_var, font=self.MASTER_FONT, width=26
        )
        self.text_entry.grid(row=3, column=0, sticky="ns")
        self.text_entry.focus()

        self.util_frame = tk.Frame(parent_frame, bg="yellow")
        self.util_frame.grid(row=4, column=0, sticky="news")
        for i in range(3):
            self.util_frame.grid_columnconfigure(i, weight=1)

        self.previous_time_label = tk.Label(
            self.util_frame, text=f"Recent Time: -", font=self.MASTER_FONT, bg="purple"
        )
        self.previous_time_label.grid(row=0, column=0, sticky="nws")

        self.best_time_label = tk.Label(
            self.util_frame, text=f"Best Time: -", font=self.MASTER_FONT, bg="orange"
        )
        self.best_time_label.grid(row=0, column=1, sticky="nws")

        self.key_selection = tk.StringVar()
        self.key_selection.set(self.KEY_OPTIONS[0])
        self.key_menu = tk.OptionMenu(
            self.util_frame,
            self.key_selection,
            *self.KEY_OPTIONS,
            command=self.on_set_key,
        )
        self.key_menu.grid(row=0, column=2, sticky="ns")

        self.reset_button = tk.Button(
            self.util_frame,
            text="Reset",
            font=self.MASTER_FONT,
            command=self.on_reset,
            bg="yellow",
        )
        self.reset_button.grid(row=0, column=3, sticky="news")

        self.about_me = tk.Label(
            parent_frame,
            text="Joseph X Li, 2020",
            font=(self.MASTER_FONT, 8),
            bg="blue",
        )
        self.about_me.grid(row=5, column=0, sticky="nes", ipady=5)

    def on_keystroke(self, *args):
        inp = self.input_var.get()
        correct, letter_states, time_array = self.au.tell(inp)
        self.display.set_colors(letter_states, len(inp))
        time_array = [(round(t, 5) if t >= 0.0 else 0.0) for t in time_array]
        self.graph.set_times(time_array)
        if correct:
            self.text_entry.config(state="disabled")
            self._set_displays()
        return

    def _set_displays(self):
        recent_time, best_time = self.au.get_scores()
        self.previous_time_label.config(text=f"Recent Time: {recent_time}")
        self.best_time_label.config(text=f"Best Time: {best_time}")

    def on_reset(self):
        self.au.reset()
        self.text_entry.config(state="normal")
        self.text_entry.delete(0, "end")
        self.display.reset()
        self.graph.reset()

    def on_set_key(self, event):
        new_key = self.KEY_DICT[self.key_selection.get()]
        if new_key is None:
            new_key = list(self.KEY_DICT["(A-Z)"])
            random.shuffle(new_key)
            new_key = "".join(new_key)
        self.graph.destroy()
        self.graph = alphabet_graph.AlphabetGraph(
            self, dpi=100, key=new_key, interval=150,
        )
        self.graph.grid(row=1, column=0, sticky="news")
        self.au.set_key(new_key)
        self.au.reset_scores()
        self.display.set_key(new_key)
        self.on_reset()
        self._set_displays()


def main():
    root = tk.Tk()
    root.title("py-alphabet-texter")
    at = AlphabetTexter(root).pack(side="top", fill="both", expand=True)
    root.mainloop()


if __name__ == "__main__":
    main()
