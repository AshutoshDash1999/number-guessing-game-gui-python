import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
import random as r
from tkinter import messagebox


class Application(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Guess the Number")

        container = tk.Frame(self, width=768, height=1000)
        container.pack(side="top", fill='both', expand=1)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, RulePage, GamePage):

            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Guess the Number", font=("Arial Black", 16))
        label.pack(pady=10, padx=10)

        startButton = ttk.Button(self, text="START", command=lambda: controller.show_frame(RulePage)).pack()

        quitButton = ttk.Button(self, text="QUIT", command=controller.quit).pack()


class RulePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Rules!!!", font=("Arial Black", 16))
        label.pack(pady=0, padx=100)
        rules_label = ttk.Label(self, text="""1. Guess a number between 0 and 6.
        2. If you guessed it correctly, you WIN.
        3. If you guessed it wrongly, I WIN.
        """)
        rules_label.pack()
        startGame_button = ttk.Button(self, text="Start Game", command=lambda: controller.show_frame(GamePage)).pack()


class GamePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Enter a number:", font=("Arial Black", 16)).pack(pady=10, padx=50)
        self.userInput = StringVar()
        entry = tk.Entry(self, width=20, textvariable=self.userInput).pack(pady=10, padx=100)
        check_button = ttk.Button(self, text="CHECK", command=self.game).pack(pady=10, padx=150)

    def game(self):

        random_number = r.choice(range(1, 6))
        userNumber = int(self.userInput.get())
        if random_number == userNumber:
            messagebox.showinfo("RESULT", "YOU WIN. HOORRAYY!!!!")
        else:
            messagebox.showinfo("RESULT", "YOU LOOSE. BRRRUUP!!!!")


Application().mainloop()