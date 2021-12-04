import tkinter as tk


class SideMenu:
    def __init__(self, window: tk.Tk):
        self.window = window
        self.menu = tk.Frame(window, bg="orange", width=200)
        self.title_label = tk.Label(self.menu, text="Menu", bg="orange", fg="white")
        self.menu_options = ["Adauga persoana", "Adauga eveniment", "Afiseaza evenimente", "Import", "Export"]

    def create_menu_options(self):
        frame = tk.Frame(self.menu, bg="orange")
        for option in self.menu_options:
            tk.Button(frame, text=option, bg="blue", fg="white").pack(pady=20)

        frame.pack(expand=True, padx=10)

    def create_menu(self):
        self.title_label.pack(fill=tk.X, pady=20)
        self.create_menu_options()
        self.menu.pack(side="left", fill=tk.Y, padx=(0, 10))
