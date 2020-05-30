import tkinter as tk

class AlphabetDisplay(tk.Frame):
    def __init__(self, parent, key, *args, font=("Menlo", 12), **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.key = key
        self.key_len = len(key)
        self._display = tk.Text(self, width=self.key_len, height=1, font=font)
        self._display.grid(row=0, column=0, sticky="") # empty sticky means default to center
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self._display.insert("end", self.key)
        self._display.configure(state="disabled")
        self._make_tags()
        
    def reset(self):
        self.set_colors(None, 0)
        
    def set_colors(self, correct, max_len):
        # removes all tags
        for color in ["red", "green", "black"]:
            self._display.tag_remove(color, "1.0", f"1.{self.key_len}")
        
        # reapplies tags
        for x in range(self.key_len):
            if x >= max_len or correct is None:
                color = "black"
            elif correct[x]:
                color = "green"
            else: 
                color = "red"
                
            start = f"1.{x * 2}"
            end = f"1.{(x * 2) + 1}"
            self._display.tag_add(color, start, end)    
    
    def _make_tags(self):
        self._display.tag_configure("red", foreground="red")
        self._display.tag_configure("black", foreground="black")
        self._display.tag_configure("green", foreground="green")

def main():
    root = tk.Tk()
    AlphabetDisplay(root, key="asdf").pack(side="top", fill="both", expand=True)
    root.mainloop()

if __name__ == "__main__":
    main()        