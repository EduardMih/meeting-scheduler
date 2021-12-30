from graphics.page import *


class ListEventsPage(Page):
    """
    Class for displaying all events page (view).
    """
    def __init__(self, window: tk.Tk):
        """
        ListEventsPage constructor to initialize all object's members.
        :param window: Parent window.
        """
        super(ListEventsPage, self).__init__(window)

        self.title_label = tk.Label(self.container, text="Vizualizare evenimente", bg="grey", fg="white",
                                    font=title_font)

        self.wrapper = tk.Frame(self.container)
        self.canvas = tk.Canvas(self.wrapper, bg="grey", highlightthickness=0)
        self.top_frame = tk.Frame(self.container, bg="grey")
        self.main_frame = tk.Frame(self.wrapper, bg="grey")

        self.scrollbar_y = tk.Scrollbar(self.wrapper, command=self.canvas.yview)
        self.scrollbar_x = tk.Scrollbar(self.wrapper, orient="horizontal", command=self.canvas.xview)

        self.start_label = tk.Label(self.top_frame, text="Start date:", bg="grey", fg="white")
        self.end_label = tk.Label(self.top_frame, text="End date:", bg="grey", fg="white")
        self.start_entry = tk.Entry(self.top_frame)
        self.end_entry = tk.Entry(self.top_frame)
        self.start_hour_label = tk.Label(self.top_frame, text="Start hour: ", bg="grey", fg="white")
        self.end_hour_label = tk.Label(self.top_frame, text="End hour: ", bg="grey", fg="white")
        self.start_hour_entry = tk.Entry(self.top_frame)
        self.end_hour_entry = tk.Entry(self.top_frame)

        self.filter_button = tk.Button(self.top_frame, text="Filter", command=self.filter_command)

        self.message_label = tk.Label(self.top_frame, text="", bg="grey")

        self.controller = None

    def pack_elements(self):
        """
        Pack all elements inside page.
        :return: None
        """
        self.title_label.pack(fill="both", pady=20)
        self.top_frame.pack(side="top")
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.pack(fill="both", expand=True, side="left")
        self.wrapper.pack(fill="both", expand=True)

    def populate_meetings(self, data: [str]):
        """
        Creates a list of labels containing meetings data.
        :param data: List of strings containing meeting data to be displayed.
        :return: None
        """
        for labels in self.main_frame.winfo_children():
            labels.destroy()

        for meeting in data:
            temp = "Title {}\nStart Date: {}\nEnd Date: {}\nParticipants: {}"
            tk.Label(self.main_frame, text=temp.format(meeting[0], meeting[1], meeting[2], meeting[3]), justify="left",
                     bg="white", anchor="w").pack(pady=20, anchor="w", fill=tk.X, expand=True)

    def create_canvas(self):
        """
        Creates canvas for scrollable area.
        :return: None
        """
        self.canvas.create_window(0, 0, anchor='nw', window=self.main_frame)
        self.canvas.update_idletasks()

        self.canvas.configure(scrollregion=self.canvas.bbox('all'), yscrollcommand=self.scrollbar_y.set,
                         xscrollcommand=self.scrollbar_x.set)

    def grid_entries(self):
        """
        Places input fields and their labels using a grid packing method.
        :return: None
        """
        self.start_label.grid(row=0, column=0, padx=2, pady=(10, 0))
        self.start_entry.grid(row=0, column=1, padx=2, pady=(10, 0))

        self.start_hour_label.grid(row=0, column=2, padx=2, pady=(10, 0))
        self.start_hour_entry.grid(row=0, column=3, padx=2, pady=(10, 0))

        self.end_label.grid(row=1, column=0, padx=2, pady=(10, 0))
        self.end_entry.grid(row=1, column=1, padx=2, pady=(10, 0))

        self.end_hour_label.grid(row=1, column=2, padx=2, pady=(10, 0))
        self.end_hour_entry.grid(row=1, column=3, padx=2, pady=(10, 0))

        self.message_label.grid(row=2, column=0, columnspan=5, padx=2, pady=(10, 0), ipady=5, sticky="we")

        self.filter_button.grid(row=0, column=4, rowspan=2, sticky=tk.N+tk.S, padx=5, pady=(10, 0))

    def create_page(self):
        """
        Places all elements on page.
        :return: A container frame that contains all page elements.
        """
        #self.populate_meetings()
        self.create_canvas()
        self.grid_entries()
        self.pack_elements()

        return self.container

    def filter_command(self):
        """
        Takes user input and call controller to select meetings accordingly.
        :return: None
        """
        start_date = self.start_entry.get()
        start_hour = self.start_hour_entry.get()
        end_date = self.end_entry.get()
        end_hour = self.end_hour_entry.get()

        self.controller.get_meetings(start_date, start_hour, end_date, end_hour)

    def set_controller(self, controller):
        """
        Sets controller of the current view.
        :param controller: Controller class that will manage this view.
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
        bg = "grey"
        text = ""
        fg = "white"
        if not success:
            bg = "red"
            fg = "white"
            text = err_message
        self.message_label.configure(bg=bg, fg=fg, text=text)

    def refresh(self):
        """
        Refreshes the canvas after meeting data was added.
        :return: None
        """
        self.create_canvas()




