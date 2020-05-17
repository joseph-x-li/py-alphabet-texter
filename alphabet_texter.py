from tkinter import *
from tkinter.font import Font
import alphabet_utils
import matplotlib
matplotlib.use('TkAgg')

root = Tk()
root.title("py-alphabet-texter")
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# ---------- VARS ----------
au = alphabet_utils.AlphabetUtils()
letter_states = [False for _ in range(26)]
time_array = [-1 for _ in range(25)]
running = False
best_time = None # float
prev_time = None # float

# ---------- ROW 0 ---------- title
title = Label(root, text="Welcome to Alphabet Texter, Python Edition", font="Menlo")
title.grid(row=0)


# ---------- ROW 1 ---------- matplotlib stuffs
graph = Canvas(root, width=380, height=100, background="blue")
graph.create_text(50, 10, text="Hello World", font="Menlo")
graph.grid(row=1)


# ---------- ROW 2 ---------- to be a canvas
alphabet_display = Text(width=51, height=1)
alphabet_display.insert("end", "a b c d e f g h i j k l m n o p q r s t u v w x y z")
alphabet_display.configure(state="disabled")

alphabet_display.grid(row=2)


# ---------- ROW 3 ---------- 
def on_keystroke(*args):
    global running, prev_time, best_time, time_array
    running = True
    correct, letter_states, time_array = au.tell(input_var.get())
    time_array = [(t if t >= 0 else 0) for t in time_array]
    if correct:
        running = False
        prev_time = sum(time_array)
        print(prev_time)
        best_time = prev_time if best_time is None else min(prev_time, best_time)
        previous_time_label.config(text=f"Previous Time: {'-' if prev_time is None else f'{prev_time:.3f}'}")
        best_time_label.config(text=f"Best Time: {'-' if best_time is None else f'{best_time:.3f}'}")
    return

input_var = StringVar()
input_var.trace("w", on_keystroke)

textEntry = Entry(root, textvariable = input_var, font="Menlo", width=26)
textEntry.grid(row=3)


# ---------- ROW 4 ----------
util_frame = Frame(root)
util_frame.grid(row=4, sticky="ew")

def onReset():
    running = False
    au.reset()
    textEntry.delete(0, "end")

print(best_time)

previous_time_label = Label(util_frame, text=f"Previous Time: {'-' if prev_time is None else f'{prev_time:.3f}'}", font="Menlo")
previous_time_label.grid(row=0, column=0, sticky="w")

best_time_label = Label(util_frame, text=f"Best Time: {'-' if best_time is None else f'{best_time:.3f}'}", font="Menlo")
best_time_label.grid(row=0, column=1, sticky="w")

button1 = Button(util_frame, text="Reset", font="Menlo", command=onReset)
button1.grid(row=0, column=2, sticky="e")
util_frame.grid_columnconfigure(2, weight=1)


# ---------- ROW 5 ----------
about_me = Label(root, text="Joseph X Li, 2020", font="Menlo")
about_me.grid(row=5)

def _quit():
    root.quit()   
    root.destroy() 

root.mainloop()

print("Program Finished")