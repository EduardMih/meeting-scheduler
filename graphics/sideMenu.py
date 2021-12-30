import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfile


class SideMenu:
    """
    SideMenu class responsible for side menu aspect.
    """
    def __init__(self, window: tk.Tk, frame: [tk.Frame], current_frame: tk.Frame):
        """
        SideMenu class constructor to initialize the object.
        :param  window: parent window.
        :param frame: Frames list to be shown when corresponding buttons are pressed.
        :param current_frame: Start frame.
        """
        self.window = window
        self.frame = frame
        self.current_frame = current_frame
        self.menu = tk.Frame(window, bg="orange", width=200)
        self.title_label = tk.Label(self.menu, text="Menu", bg="orange", fg="white", font="Helvetica 15 bold")
        self.menu_options = ["Adauga persoana", "Adauga eveniment", "Afiseaza evenimente", "Import", "Export"]

        self.controller = None

    def create_menu_options(self):
        """
        Create and pack all side menu buttons.
        :return: None
        """
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
        """
        Pack together title and buttons on parent frame.
        :return: None
        """
        self.title_label.pack(fill=tk.X, pady=20)
        self.create_menu_options()
        #self.menu.pack(side="left", fill=tk.Y, padx=(0, 10))

        return self.menu

    def show_page(self, page_index):
        """
        Shows corresponding page when a button is pressed.
        :param page_index: index of the page in the list passed to __init__.
        :return: None
        """
        self.current_frame.pack_forget()
        self.frame[page_index].pack(fill="both", expand=True)
        self.current_frame = self.frame[page_index]

    def import_file_dialog(self):
        """
        Opens a file dialog when import button is pressed.
        :return: None
        """
        filename = askopenfilename(filetypes=[("iCalendar files", "*.ics")])

        if filename:
            self.controller.import_cal(filename)

    def export_file_dialog(self):
        """
        Opens a file dialog when export button is pressed.
        :return: None
        """
        filename = asksaveasfile(filetypes=[("iCalendar files", "*.ics")], defaultextension="*.ics", initialfile="export.ics")

        if filename:
            self.controller.export_cal(filename)

    def set_controller(self, controller):
        """
        Sets the controller of the current view.
        :param controller: Controller class that will manage this view.
        :return: None
        """
        self.controller = controller

    def show_message(self, success, title, message):
        """
        Displays a message box for import/export with the status of the operation.
        :param boolean success: Operation completed successfully or not.
        :param str title: Title of dialog box.
        :param str message: Message of dialog box.
        :return:
        """
        if success:
            messagebox.showinfo(title, message)

        else:

            messagebox.showerror(title, message)
