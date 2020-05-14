from tkinter import *

master = Tk()

title = Label(master, text="Welcome to Alphabet Texter, Python Edition", font = "Menlo")
title.grid(row=0)

graph = Canvas(master, width=200, height=100, background = "blue")
graph.create_text(50, 10, text = "Hello World")
graph.grid(row=1)


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