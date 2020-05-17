from tkinter import *
from tkinter.font import Font
import alphabet_utils
# import matplotlib
# matplotlib.use('TkAgg')

class AlphabetTexter:
    def __init__(self, parent_frame):
        root = Frame(parent_frame)
        root.grid(row=0, column=0)
        self.best_time = None
        self.prev_time = None
        self.running = False
        self.letter_states = [False for _ in range(26)]
        self.time_array = [-1 for _ in range(25)]
        self.au = alphabet_utils.AlphabetUtils()
        self.make_internals(root)
    
    def make_internals(self, parent_frame):
        self.title = Label(parent_frame, text="Welcome to Alphabet Texter, Python Edition", font="Menlo")
        self.title.grid(row=0)

        self.graph = Canvas(parent_frame, width=380, height=100, background="blue")
        self.graph.create_text(50, 10, text="Hello World", font="Menlo")
        self.graph.grid(row=1)

        self.alphabet_display = Text(width=51, height=1)
        self.alphabet_display.insert("end", "a b c d e f g h i j k l m n o p q r s t u v w x y z")
        self.alphabet_display.configure(state="disabled")
        self.alphabet_display.grid(row=2)

        self.input_var = StringVar()
        self.input_var.trace("w", self.on_keystroke)
        
        self.textEntry = Entry(parent_frame, textvariable = self.input_var, font="Menlo", width=26)
        self.textEntry.grid(row=3)

        self.util_frame = Frame(parent_frame)
        self.util_frame.grid(row=4, sticky="ew")

        self.previous_time_label = Label(self.util_frame, text=f"Previous Time: {'-' if self.prev_time is None else f'{self.prev_time:.3f}'}", font="Menlo")
        self.previous_time_label.grid(row=0, column=0, sticky="w")

        self.best_time_label = Label(self.util_frame, text=f"Best Time: {'-' if self.best_time is None else f'{self.best_time:.3f}'}", font="Menlo")
        self.best_time_label.grid(row=0, column=1, sticky="w")

        self.reset_button = Button(self.util_frame, text="Reset", font="Menlo", command=self.onReset)
        self.reset_button.grid(row=0, column=2, sticky="e")
        self.util_frame.grid_columnconfigure(2, weight=1)

        self.about_me = Label(parent_frame, text="Joseph X Li, 2020", font="Menlo")
        self.about_me.grid(row=5)
    
    def on_keystroke(self, *args):
        self.running = True
        correct, self.letter_states, self.time_array = self.au.tell(self.input_var.get())
        self.time_array = [(t if t >= 0 else 0) for t in self.time_array]
        if correct:
            self.running = False
            self.prev_time = sum(self.time_array)
            print(self.prev_time)
            self.best_time = self.prev_time if self.best_time is None else min(self.prev_time, self.best_time)
            self.previous_time_label.config(text=f"Previous Time: {'-' if self.prev_time is None else f'{self.prev_time:.3f}'}")
            self.best_time_label.config(text=f"Best Time: {'-' if self.best_time is None else f'{self.best_time:.3f}'}")
        return
    
    def onReset(self):
            self.running = False
            self.au.reset()
            self.textEntry.delete(0, "end")
        
        
def main():
    root = Tk()
    at = AlphabetTexter(root)
    root.mainloop()

if __name__ == "__main__":
    main()



# root.title("py-alphabet-texter")
# root.grid_rowconfigure(1, weight=1)
# root.grid_columnconfigure(0, weight=1)