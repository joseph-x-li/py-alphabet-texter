from tkinter import *
from tkmacosx import Button

root = Tk()

title = Label(root, text="Welcome to Alphabet Texter Python Edition :)")
title.pack()

aboutFrame = Frame(root, bg="pink")
aboutFrame.pack(side=BOTTOM)

button1 = Button(aboutFrame, text="my linkedin1", fg="red")
button2 = Button(aboutFrame, text="my linkedin2", fg="blue")
button3 = Button(aboutFrame, text="my linkedin3", fg="green")
button4 = Button(aboutFrame, text="my linkedin4", fg="yellow") 

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=RIGHT)

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