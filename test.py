from tkinter import *
import alphabet_utils

master = Tk()
au = alphabet_utils.AlphabetUtils()

title = Label(master, text="Welcome to Alphabet Texter, Python Edition", font="Menlo")
title.grid(row=0)

graph = Canvas(master, width=200, height=100, background="blue")
graph.create_text(50, 10, text = "Hello World")
graph.grid(row=1)

title = Label(master, text="abcdefghijklmnopqrstuvwxyz", font="Menlo", fg="green")
title.grid(row=2)

def on_keystroke(*args):
    print(au.tell(input_var.get()))
    print(input_var.get())
    return

input_var = StringVar()
input_var.trace("w", on_keystroke)

textEntry = Entry(master, textvariable = input_var, font="Menlo", width=26)
textEntry.grid(row=3)

button1 = Button(master, text="button1")
button1.grid(row=4)

about_me = Label(master, text="Joseph X Li, 2020", font="Menlo")
about_me.grid(row=5)

master.mainloop()

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
