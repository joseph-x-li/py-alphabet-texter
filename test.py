from tkinter import *
from tkinter.font import Font
import alphabet_utils
import matplotlib
matplotlib.use('TkAgg')

root = Tk()
root.title("py-alphabet-texter")
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

# red_font = Font(family="Menlo", color="red", size=9)
# gray_font = Font(family="Menlo", color="gray", size=9)
# green_font = Font(family="Menlo", color="green", size=9)
# alphabet_display.tag_configure("RED", red_font)
# alphabet_display.tag_configure("GRAY", gray_font)
# alphabet_display.tag_configure("GREEN", green_font)
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
        best_time = prev_time if best_time is None else min(prev_time, best_time)
    return

input_var = StringVar()
input_var.trace("w", on_keystroke)

textEntry = Entry(root, textvariable = input_var, font="Menlo", width=26)
textEntry.grid(row=3)


# ---------- ROW 4 ----------
def onReset():
    running = False
    au.reset()
    textEntry.delete(0, "end")
    
button1 = Button(root, text="Reset", font="Menlo", command=onReset)
button1.grid(row=4)

previous_time_label = Label(root, text=f"Previous Time: {'-' if best_time is None else 'fill'}", font="Menlo")
previous_time_label.grid(row=4, column = 1)

best_time_label = Label(root, text=f"Best Time: {'-' if best_time is None else 'fill'}", font="Menlo")
best_time_label.grid(row=4, column = 2)


# ---------- ROW 5 ----------
about_me = Label(root, text="Joseph X Li, 2020", font="Menlo")
about_me.grid(row=5)

def _quit():
    root.quit()   
    root.destroy() 

root.mainloop()

print("Program Finished")


# def on_variable_trace(*args):
#     if entryVariable2.get() == "":
#         entryWidget3.configure(state="disable")
#     else:
#         entryWidget3.configure(state="normal")

# entryVariable2 = StringVar()
# entryWidget2= Entry(textFrame, textvariable=entryVariable2)
# entryWidget2["width"] = 30
# entryWidget2.pack(side="top")
# entryVariable2.trace("w", on_variable_trace)
