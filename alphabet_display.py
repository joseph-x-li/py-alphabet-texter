import tkinter as tk


class AlphabetDisplay(tk.Frame):
    def __init__(self, parent, key, *args, font=("Menlo", 14), **kwargs):
        """Initialize an Alphabet Display object.

        Args:
            parent (tk.Frame): Parent tkinter frame.
            key (string): Input key.
            font (tuple, optional): Display font. Defaults to ("Menlo", 14).
        """
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._parent = parent

        self._key = key
        self._key_len = len(key)
        self._font = font
        self._build_widget()


    def _build_widget(self):
        self._display = tk.Text(self, width=self._key_len, height=1, font=self._font)
        self._display.grid(row=0, column=0, sticky="")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self._display.insert("end", self._key)
        self._display.configure(state="disabled")
        self.reset()
        self._make_tags()


    def _make_tags(self):
        self._display.tag_configure("red", foreground="black", background="red")
        self._display.tag_configure("black", foreground="black", background=None)
        self._display.tag_configure("green", foreground="black", background="green")

    def set_key(self, new_key):
        """Set a new key.

        Args:
            new_key (string): The new key.
        """
        self._key = new_key
        self._key_len = len(new_key)
        self._display.destroy()
        self._build_widget()

    def set_colors(self, correct, max_len):
        """Set colors of text.

        Args:
            correct (List): List of correct characters.
            max_len (int): Length of current user input.
        """
        # removes all tags
        for color in ["red", "green", "black"]:
            self._display.tag_remove(color, "1.0", f"1.{self._key_len}")

        # reapplies tags
        for x in range(self._key_len):
            start = f"1.{x}"
            end = f"1.{x + 1}"
            if x >= max_len or correct is None:
                color = "black"
            elif correct[x]:
                color = "green"
            else:
                color = "red"

            self._display.tag_add(color, start, end)

    def reset(self):
        """Reset all colors to black.
        """
        self.set_colors(None, 0)



def main():
    root = tk.Tk()
    AlphabetDisplay(root, key="test_string").pack(side="top", fill="both", expand=True)
    root.mainloop()


if __name__ == "__main__":
    main()
