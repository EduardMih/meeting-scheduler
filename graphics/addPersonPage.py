from graphics.page import *


class AddPerssonPage(Page):
    """
    AddPersonPage class for a page(view) to add new person.
    """
    def __init__(self, window: tk.Tk):
        """
        AddPersonPage class cosntructor to initialize object.
        :param window: Parent window
        """
        super(AddPerssonPage, self).__init__(window)

        self.frame = tk.Frame(self.container, bg="grey")
        self.title_label = tk.Label(self.container, text="Adauga persoana", bg="grey", fg="white", font=title_font)
        self.lastname_label = tk.Label(self.frame, text="Nume", bg="grey", fg="white")
        self.lastname_entry = tk.Entry(self.frame)
        self.firstname_label = tk.Label(self.frame, text="Prenume", bg="grey", fg="white")
        self.firstname_entry = tk.Entry(self.frame)
        self.submit_button = tk.Button(self.frame, text="Adauga persoana", command=self.get_data)

        self.message_label = tk.Label(self.frame, text="", bg="grey")

        self.controller = None

    def create_page(self):
        """
        Packs all the elements inside parent frame.
        :return: A container frame containing all elements
        """
        self.lastname_label.grid(row=0, column=0, padx=20, pady=(0, 5), stick=tk.W)
        self.lastname_entry.grid(row=0, column=1, pady=(0, 5))
        self.firstname_label.grid(row=1, column=0, padx=20, pady=(0, 5), sticky=tk.W)
        self.firstname_entry.grid(row=1, column=1, pady=(0, 5))
        self.submit_button.grid(row=0, column=3, rowspan=2, sticky=tk.N+tk.S, padx=20, pady=(0, 5))
        self.message_label.grid(row=2, column=0, columnspan=4, padx=20, pady=(15, 15), ipady=5, sticky=tk.W+tk.E)

        self.title_label.pack(fill="both", pady=20)
        self.frame.pack(expand=True)

        return self.container

    def get_data(self):
        """
        Gets data about person to insert and call appropriate controller method.
        :return: None
        """
        lastname = self.lastname_entry.get()
        firstname = self.firstname_entry.get()

        self.controller.add_person(firstname, lastname)

    def set_controller(self, controller):
        """
        Sets current view controller.
        :param controller: Controller class to control current view.
        :return: None
        """
        self.controller = controller

    def show_message_label(self, success, err_message=None):
        """
        Displays status message.
        :param success: Operation was successful or not.
        :param err_message: In case of error, error message.
        :return: None
        """
        bg = "green"
        fg = "white"
        text = "Persoana adaugata cu suces"

        if not success:
            bg = "red"
            fg = "white"
            text = err_message

        self.message_label.configure(bg=bg, fg=fg, text=text)

    def clear_form(self):
        """
        Clears the form after submit.
        :return: None
        """
        self.lastname_entry.delete(0, "end")
        self.firstname_entry.delete(0, "end")



