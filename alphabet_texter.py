from tkinter import *
import alphabet_utils
import alphabet_display as ald
# import alphabet_graph

class AlphabetTexter:
    def __init__(self, parent_frame):
        self.root = Frame(parent_frame, bg="red", highlightthickness=1, highlightbackground="black")
        self.root.grid(row=0, column=0)
        
        self.MASTER_FONT = "Menlo"
        self.au = alphabet_utils.AlphabetUtils()
        self.make_internals(self.root)
    
    def make_internals(self, parent_frame):
        self.title = Label(parent_frame, 
                           text="Welcome to Alphabet Texter, Python Edition", 
                           font=(self.MASTER_FONT, 16), 
                           relief="ridge")
        self.title.grid(row=0, column=0, sticky="news", ipady=5, ipadx=5)
        
        # self.graph = alphabet_graph.AlphabetGraph(parent_frame, (4, 3), 100)
        # self.graph.grid(row=2, column=0, sticky="news")
        
        self.alphabet_display = ald.AlphabetDisplay(parent_frame)
        self.alphabet_display.grid(row=2, column=0, sticky="news", ipadx=5, ipady=5)
        # self.alphabet_display = Text(parent_frame, width=51, height=1, font=self.MASTER_FONT, bg="green")
        # self.alphabet_display.grid(row=2, column=0, sticky="news", ipadx=5, ipady=5)
        # self.alphabet_display.insert("end", "a b c d e f g h i j k l m n o p q r s t u v w x y z")
        # self.alphabet_display.configure(state="disabled")
        # self.alphabet_display.tag_configure("red", foreground="red")
        # self.alphabet_display.tag_configure("black", foreground="black")
        # self.alphabet_display.tag_configure("green", foreground="green")

        self.input_var = StringVar()
        self.input_var.trace("w", self.on_keystroke)
        
        self.text_entry = Entry(parent_frame, textvariable = self.input_var, font=self.MASTER_FONT, width=26)
        self.text_entry.grid(row=3)
        self.text_entry.focus()

        self.util_frame = Frame(parent_frame)
        self.util_frame.grid(row=4, sticky="ew")

        self.previous_time_label = Label(self.util_frame, text=f"Recent Time: -", font=self.MASTER_FONT, bg="purple")
        self.previous_time_label.grid(row=0, column=0, sticky="w")

        self.best_time_label = Label(self.util_frame, text=f"Best Time: -", font=self.MASTER_FONT, bg="orange")
        self.best_time_label.grid(row=0, column=1, sticky="w")

        self.reset_button = Button(self.util_frame, text="Reset", font=self.MASTER_FONT, command=self.on_reset, bg="yellow")
        self.reset_button.grid(row=0, column=2, sticky="e")
        self.util_frame.grid_columnconfigure(2, weight=1)

        self.about_me = Label(parent_frame, text="Joseph X Li, 2020", font=self.MASTER_FONT)
        self.about_me.grid(row=5)
    
    def on_keystroke(self, *args):
        inp = self.input_var.get()
        correct, letter_states, time_array = self.au.tell(inp)
        self.alphabet_display.set_colors(letter_states, len(inp))
        # self.make_color(letter_states)
        time_array = [(round(t, 5) if t >= 0.0 else 0.0) for t in time_array]
        # self.make_plot(time_array)
        if correct:
            self.text_entry.config(state="disabled")
            recent_time, best_time = self.au.get_scores()
            self.previous_time_label.config(text=f"Recent Time: {recent_time}")
            self.best_time_label.config(text=f"Best Time: {best_time}")
        return
    
    def on_reset(self):
        self.au.reset()
        self.text_entry.config(state="normal")
        self.text_entry.delete(0, "end")
        self.alphabet_display.reset()
        # self.make_color(None, reset=True)
        # self.make_plot(None, erase=True)
    
    # def make_color(self, colors, reset=False):
    #     for col in ["red", "green", "black"]:
    #         self.alphabet_display.tag_remove(col, "1.0", "1.51")
            
    #     for x in range(26):
    #         start = x*2
    #         end = start + 1
    #         start = f"1.{start}"
    #         end = f"1.{end}"
    #         if reset or x >= len(self.input_var.get()):
    #             color = "black"
    #         elif colors[x]:
    #             color = "green"
    #         else: 
    #             color = "red"
    #         self.alphabet_display.tag_add(color, start, end)    
    #     return
    
    # def init_plot(self, parent_frame):
    #     self.figure = plt.Figure(figsize=(3, 4), dpi=100)
    #     self.canvas = FigureCanvasTkAgg(self.figure, master=parent_frame)
    #     self.canvas.get_tk_widget().grid(row=1, column=0, sticky="news")
    #     self.ax = self.figure.add_subplot(111)
    #     self.make_plot(None, init=True)
    
    # def animate(self, i):
    #     for rect, height in zip(self.bar_plt_var, self.times):
    #         rect.set_height(height)
    #     return self.bar_plt_var,
    
    # def make_plot(self, times, init=False, erase=False):
    #     x = [chr(i) for i in range(98, 123)]
    #     if erase:
    #         self.ax.clear()
    #         init=True
        
    #     if init:
    #         times = [0.0 for _ in range(25)]
    #         self.bar_plt_var = self.ax.bar(x, times, color="blue")
    #         self.ax.set_xlabel("Time To Press")
    #         self.ax.set_ylabel("Seconds")
    #         self.ax.set_ylim(bottom=0, top=0.5)
    #         self.canvas.draw()
    #         return
        
    #     for rect, height in zip(self.bar_plt_var, times):
    #         rect.set_height(height)
        
    #     self.canvas.draw()


def main():
    root = Tk()
    at = AlphabetTexter(root)
    root.mainloop()

if __name__ == "__main__":
    main()



# root.title("py-alphabet-texter")
