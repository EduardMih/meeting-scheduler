from graphics.page import *


class AddMeetingPage(Page):
    def __init__(self, window: tk.Tk):
        super(AddMeetingPage, self).__init__(window)

        self.title_label = tk.Label(self.container, text="Adauga meeting", bg="grey", fg="white", font=title_font)

        self.wrapper = tk.Frame(self.container, bg="grey")

        self.meeting_title_label = tk.Label(self.wrapper, text="Title:", bg="grey", fg="white")
        self.meeting_title_entry = tk.Entry(self.wrapper)
        self.start_label = tk.Label(self.wrapper, text="Start date:", bg="grey", fg="white")
        self.end_label = tk.Label(self.wrapper, text="End date:", bg="grey", fg="white")
        self.start_entry = tk.Entry(self.wrapper)
        self.end_entry = tk.Entry(self.wrapper)
        self.start_hour_label = tk.Label(self.wrapper, text="Start hour: ", bg="grey", fg="white")
        self.end_hour_label = tk.Label(self.wrapper, text="End hour: ", bg="grey", fg="white")
        self.start_hour_entry = tk.Entry(self.wrapper)
        self.end_hour_entry = tk.Entry(self.wrapper)

        self.list_of_participants_label = tk.Label(self.wrapper,
                                                   text="Lista de participanti (cate unul pe o linie, <nume> <prenume>):",
                                                   bg="grey",
                                                   fg="white"
                                                   )
        self.list_of_participants = tk.Text(self.wrapper, height=10)

        self.submit_button = tk.Button(self.wrapper, text="Adauga intalnire", command=self.get_data)

        self.message_label = tk.Label(self.wrapper, text="", bg="grey")

        self.controller = None

    def create_page(self):
        self.meeting_title_label.grid(row=0, column=0, padx=2, pady=(10, 0))
        self.meeting_title_entry.grid(row=0, column=1, columnspan=3, padx=2, pady=(10, 0), sticky="we")

        self.start_label.grid(row=1, column=0, padx=2, pady=(10, 0))
        self.start_entry.grid(row=1, column=1, padx=2, pady=(10, 0))

        self.start_hour_label.grid(row=1, column=2, padx=2, pady=(10, 0))
        self.start_hour_entry.grid(row=1, column=3, padx=2, pady=(10, 0))

        self.end_label.grid(row=2, column=0, padx=2, pady=(10, 0))
        self.end_entry.grid(row=2, column=1, padx=2, pady=(10, 0))

        self.end_hour_label.grid(row=2, column=2, padx=2, pady=(10, 0))
        self.end_hour_entry.grid(row=2, column=3, padx=2, pady=(10, 0))

        self.list_of_participants_label.grid(row=3, column=0, columnspan=4, padx=2, pady=(10, 0), sticky="w")
        self.list_of_participants.grid(row=4, column=0, columnspan=4, padx=2, pady=(5, 0))

        self.submit_button.grid(row=5, column=0, columnspan=4, padx=2, pady=(20, 0), sticky="we")

        self.message_label.grid(row=6, column=0, columnspan=4, padx=2, pady=(10, 0), sticky="we", ipady=5)

        self.title_label.pack(fill="both", pady=20)
        self.wrapper.pack(expand=True)

        return self.container

    def get_data(self):
        start_date = self.start_entry.get()
        start_hour = self.start_hour_entry.get()
        end_date = self.end_entry.get()
        end_hour = self.end_hour_entry.get()
        meeting_title = self.meeting_title_entry.get()


        participants_list = self.list_of_participants.get("1.0", "end")
        self.clear_form()

        self.controller.add_meeting(meeting_title, start_date, start_hour, end_date, end_hour, participants_list)

    def clear_form(self):
        self.start_entry.delete(0, "end")
        self.start_hour_entry.delete(0, "end")
        self.end_entry.delete(0, "end")
        self.end_hour_entry.delete(0, "end")
        self.list_of_participants.delete("1.0", "end")

    def set_controller(self, controller):
        self.controller = controller

    def show_message_label(self, success, err_message=None):
        bg = "green"
        fg = "white"
        text = "Meeting adaugat cu succes"

        if not success:
            bg = "red"
            fg = "white"
            text = err_message

        self.message_label.configure(bg=bg, fg=fg, text=text)
