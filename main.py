import tkinter as tk
from listEventsPage import ListEventsPage
from sideMenu import SideMenu
from addPersonPage import AddPerssonPage
from addMeetingPage import AddMeetingPage

class App:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Meeting scheduler")
        self.window.minsize(width=800, height=800)
        self.window.configure(bg="grey")

    def set_window_prop(self):
        self.window.title("Meeting scheduler")
        self.window.minsize(width=500, height=800)

    def run(self):
        self.window.update()
        menu = SideMenu(self.window)
        menu.create_menu()

        #events = ListEventsPage(self.window)
        #events.create_page()

        #person_page = AddPerssonPage(self.window)
        #person_page.create_page()

        add = AddMeetingPage(self.window)
        add.create_page()

        self.window.mainloop()


app = App()
app.run()
