import tkinter as tk


class ListEventsPage:

    def __init__(self, window: tk.Tk):
        self.window = window

        self.canvas = tk.Canvas(self.window, bg="grey", highlightthickness=0)
        self.top_frame = tk.Frame(self.window, bg="grey")
        self.main_frame = tk.Frame(self.window, bg="grey")

        self.scrollbar_y = tk.Scrollbar(self.window, command=self.canvas.yview)
        self.scrollbar_x = tk.Scrollbar(self.window, orient="horizontal", command=self.canvas.xview)

        self.start_label = tk.Label(self.top_frame, text="Start date:")
        self.end_label = tk.Label(self.top_frame, text="End date:")
        self.start_entry = tk.Entry(self.top_frame)
        self.end_entry = tk.Entry(self.top_frame)
        self.start_hour_label = tk.Label(self.top_frame, text="Start hour: ")
        self.end_hour_label = tk.Label(self.top_frame, text="End hour: ")
        self.start_hour_entry = tk.Entry(self.top_frame)
        self.end_hour_entry = tk.Entry(self.top_frame)

        self.filter_button = tk.Button(self.top_frame, text="Filter", command=self.filter_command)

    def pack_elements(self):
        self.top_frame.pack(side="top")
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.pack(fill="both", expand=True, side="left")

    def populate_events(self):
        for i in range(20):
            temp = "Title {}\nStart Date: 2021-11-29 10:12\nEnd Date: 2021-11-29 11:00\nParticipants: Andrei, Robert"
            temp = temp + "Andrei, " * i
            tk.Label(self.main_frame, text=temp.format(i), justify="left", bg="white", anchor="w").pack(pady=20,
                                                                                                        anchor=tk.W,
                                                                                                        fill=tk.X)

    def create_canvas(self):
        self.canvas.create_window(0, 0, anchor='nw', window=self.main_frame)
        self.canvas.update_idletasks()

        self.canvas.configure(scrollregion=self.canvas.bbox('all'), yscrollcommand=self.scrollbar_y.set,
                         xscrollcommand=self.scrollbar_x.set)

    def grid_entries(self):
        self.start_label.grid(row=0, column=0, padx=2, pady=(10, 0))
        self.start_entry.grid(row=0, column=1, padx=2, pady=(10, 0))

        self.start_hour_label.grid(row=0, column=2, padx=2, pady=(10, 0))
        self.start_hour_entry.grid(row=0, column=3, padx=2, pady=(10, 0))

        self.end_label.grid(row=1, column=0, padx=2, pady=(10, 0))
        self.end_entry.grid(row=1, column=1, padx=2, pady=(10, 0))

        self.end_hour_label.grid(row=1, column=2, padx=2, pady=(10, 0))
        self.end_hour_entry.grid(row=1, column=3, padx=2, pady=(10, 0))

        self.filter_button.grid(row=0, column=4, rowspan=2, sticky=tk.N+tk.S, padx=5, pady=(10, 0))

    def create_page(self):
        self.populate_events()
        self.create_canvas()
        self.grid_entries()
        self.pack_elements()

    def filter_command(self):
        start_date = self.start_entry.get()
        start_hour = self.start_hour_entry.get()
        end_date = self.end_entry.get()
        end_hour = self.end_hour_entry.get()


        print("Start: ", start_date, start_hour)
        print("End: ", end_date, end_hour)


