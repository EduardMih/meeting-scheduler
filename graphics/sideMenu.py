import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfile


class SideMenu:
    def __init__(self, window: tk.Tk, frame: [tk.Frame], current_frame: tk.Frame):
        self.window = window
        self.frame = frame
        self.current_frame = current_frame
        self.menu = tk.Frame(window, bg="orange", width=200)
        self.title_label = tk.Label(self.menu, text="Menu", bg="orange", fg="white", font="Helvetica 15 bold")
        self.menu_options = ["Adauga persoana", "Adauga eveniment", "Afiseaza evenimente", "Import", "Export"]

        self.controller = None

    def create_menu_options(self):
        frame = tk.Frame(self.menu, bg="orange")
        for i in range(len(self.menu_options)):
            if i <= 2:
                tk.Button(frame, text=self.menu_options[i], bg="blue", fg="white",
                          command=lambda i=i: self.show_page(i)).pack(pady=20)

            if i == 3:

                tk.Button(frame, text=self.menu_options[i], bg="blue", fg="white",
                          command=self.import_file_dialog).pack(pady=20)

            if i == 4:
                tk.Button(frame, text=self.menu_options[i], bg="blue", fg="white",
                          command=self.export_file_dialog).pack(pady=20)

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

    def import_file_dialog(self):
        filename = askopenfilename(filetypes=[("iCalendar files", "*.ics")])

        self.controller.import_cal(filename)

    def export_file_dialog(self):
        filename = asksaveasfile(filetypes=[("iCalendar files", "*.ics")], defaultextension="*.ics", initialfile="export.ics")

        self.controller.export_cal(filename)

    def set_controller(self, controller):
        self.controller = controller

    def show_message(self, success, title, message):
        if success:
            messagebox.showinfo(title, message)

        else:

            messagebox.showerror(title, message)
