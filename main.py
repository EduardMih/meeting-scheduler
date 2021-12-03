import tkinter as tk
from listEventsPage import ListEventsPage


class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Meeting scheduler")
        self.window.minsize(width=500, height=800)

    def set_window_prop(self):
        self.window.title("Meeting scheduler")
        self.window.minsize(width=500, height=800)

    def run(self):
        events = ListEventsPage(self.window)
        events.create_page()
        self.window.mainloop()


app = App()
app.run()
