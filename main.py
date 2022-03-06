import random
import tkinter as tk
from tkinter import ttk, font as tkfont
from tkinter.messagebox import showinfo

file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]
movies = {
    'Waynes World': 1,
    'Freaky Friday': 2,
    'Heavy Weights': 3,
    'A Walk to Remember': 4,
    'Confessions of a Teenage Drama Queen': 5,
    'Fight Club': 6,
    'The Princess Diary': 7,
    'Billy Madison': 8,
    'Dumb and Dumber': 9,
    'Jurassic Park': 10,
    'Clueless': 11,
    'White Chicks': 12,
    'Rat Race': 13,
    'Wedding Singer': 14,
    'Mean Girls': 15,
    'How to deal': 16,
    'Riding in Cars with Boys': 17,
    'Dodgeball': 18,
    'Big Fat Liar': 19,
    'Godzilla': 20,
    'Pitch Perfect': 21,
    'Pitch Perfect 2': 22,
    'Pitch Perfect 3': 23,
    'Jaws': 24,
    'American Pie': 25,
    '10 Things I Hate About You': 26,
    'What A Girl Wants': 27,
    'E.T.': 28,
    'Pulp Fiction': 29,
    'Mighty Joe Young': 30,
    'V for Vandetta': 31,
    'Happy Gilmore': 32,
    'Goonies': 33,
    'Sister Act': 34
}

movie2 = {}
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Comic Sans', size=18, weight="bold", slant="italic")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, RandomPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Random Movie Generator", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        randombutton = tk.Button(self, text="Random!",
                                 command=lambda: controller.show_frame("RandomPage"))
        randombutton.pack()


class RandomPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.message = random.choice(list(movies))

        label = tk.Label(self, text=self.message, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        def reset(message):
            message = ""
            label.config(text="")
            message = random.choice(list(movies))
            label.config(text=message)
            return

        def back():
            controller.show_frame("StartPage")

        againbutton = tk.Button(self, text="Again!", command=lambda: reset(self.message))

        backbutton = tk.Button(self, text="Back",
                               command=lambda: back())
        againbutton.pack()
        backbutton.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
