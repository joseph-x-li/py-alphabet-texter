from tkinter import *
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
graph = Canvas(root, width=200, height=100, background="blue")
graph.create_text(50, 10, text="Hello World", font="Menlo")
graph.grid(row=1)


# ---------- ROW 2 ---------- to be a canvas
title = Label(root, text="abcdefghijklmnopqrstuvwxyz", font="Menlo", fg="gray")
title.grid(row=2, column = 0)


# ---------- ROW 3 ---------- 
def on_keystroke(*args):
    global running, prev_time, best_time
    running = True
    x = au.tell(input_var.get())
    print(x)
    correct, letter_states, time_array = x
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

previous_time_label = Label(root, text=f"Previous Time: {'--:--' if best_time is None else 'fill'}", font="Menlo")
previous_time_label.grid(row=4, column = 1)

best_time_label = Label(root, text=f"Best Time: {'--:--' if best_time is None else 'fill'}", font="Menlo")
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
