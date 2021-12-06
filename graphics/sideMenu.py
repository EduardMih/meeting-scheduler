import tkinter as tk


class SideMenu:
    def __init__(self, window: tk.Tk, frame: [tk.Frame], current_frame: tk.Frame):
        self.window = window
        self.frame = frame
        self.current_frame = current_frame
        self.menu = tk.Frame(window, bg="orange", width=200)
        self.title_label = tk.Label(self.menu, text="Menu", bg="orange", fg="white", font="Helvetica 15 bold")
        self.menu_options = ["Adauga persoana", "Adauga eveniment", "Afiseaza evenimente", "Import", "Export"]

    def create_menu_options(self):
        frame = tk.Frame(self.menu, bg="orange")
        for i in range(len(self.menu_options)):
            tk.Button(frame, text=self.menu_options[i], bg="blue", fg="white",
                      command=lambda i=i: self.show_page(i)).pack(pady=20)

        frame.pack(expand=True, padx=10)

    def create_menu(self):
        self.title_label.pack(fill=tk.X, pady=20)
        self.create_menu_options()
        #self.menu.pack(side="left", fill=tk.Y, padx=(0, 10))

        return self.menu

    def show_page(self, page_index):
        self.current_frame.pack_forget()
        self.frame[page_index].pack(fill="both", expand=True)
        self.current_frame = self.frame[page_index]

