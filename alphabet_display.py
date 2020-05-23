import tkinter as tk

class AlphabetDisplay(tk.Frame):
    def __init__(self, parent, *args, font="Menlo", **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self._display = tk.Text(self, width=51, height=1, font=font, bg="brown")
        self._display.pack(fill="both", expand=True)
        self._display.insert("end", "a b c d e f g h i j k l m n o p q r s t u v w x y z")
        self._display.configure(state="disabled")
        self._make_tags()
        
    def reset(self):
        self.set_colors(None, 0)
        
    def set_colors(self, correct, max_len):
        #removes all tags
        for col in ["red", "green", "black"]:
            self._display.tag_remove(col, "1.0", "1.51")
        
        #reapplies tags
        for x in range(26):
            start = f"1.{x * 2}"
            end = f"1.{(x * 2) + 1}"
            if x >= max_len or correct is None:
                color = "black"
            elif correct[x]:
                color = "green"
            else: 
                color = "red"
            self._display.tag_add(color, start, end)    
    
    def _make_tags(self):
        self._display.tag_configure("red", foreground="red")
        self._display.tag_configure("black", foreground="black")
        self._display.tag_configure("green", foreground="green")

def main():
    root = tk.Tk()
    AlphabetDisplay(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

if __name__ == "__main__":
    main()        