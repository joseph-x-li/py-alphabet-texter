import tkinter as tk
import alphabet_graph, alphabet_utils, alphabet_display


class AlphabetTexter(tk.Frame):
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

        self.MASTER_FONT = "Menlo"
        self.au = alphabet_utils.AlphabetUtils()
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
            parent_frame, figsize=(4.5, 3), dpi=100, interval=150
        )
        self.graph.grid(row=1, column=0, sticky="news")

        self.display = alphabet_display.AlphabetDisplay(parent_frame)
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

        self.live_graph_box = tk.Checkbutton(self.util_frame)
        self.live_graph_box.grid(row=0, column=2, sticky="nes")

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
        self.about_me.grid(row=5, column=0, sticky="nws", ipady=5)

    def on_keystroke(self, *args):
        inp = self.input_var.get()
        correct, letter_states, time_array = self.au.tell(inp)
        self.display.set_colors(letter_states, len(inp))
        time_array = [(round(t, 5) if t >= 0.0 else 0.0) for t in time_array]
        self.graph.set_times(time_array)
        if correct:
            self.text_entry.config(state="disabled")
            recent_time, best_time = self.au.get_scores()
            self.previous_time_label.config(text=f"Recent Time: {recent_time}")
            self.best_time_label.config(text=f"Best Time: {best_time}")
        return

    def on_reset(self):
        self.au.reset()
        self.text_entry.config(state="normal")
        self.text_entry.delete(0, "end")
        self.display.reset()
        self.graph.reset()


def main():
    root = tk.Tk()
    root.title("py-alphabet-texter")
    at = AlphabetTexter(root).pack(side="top", fill="both", expand=True)
    root.mainloop()


if __name__ == "__main__":
    main()
