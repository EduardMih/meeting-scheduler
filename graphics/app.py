import tkinter as tk
from graphics.listEventsPage import ListEventsPage
from graphics.sideMenu import SideMenu
from .addPersonPage import AddPerssonPage
from .addMeetingPage import AddMeetingPage


class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Meeting scheduler")
        self.window.minsize(width=1000, height=800)
        self.window.configure(bg="grey")

    def run(self):
        self.window.update()

        frames = [AddPerssonPage(self.window).create_page(),
                  AddMeetingPage(self.window).create_page(),
                  ListEventsPage(self.window).create_page()]

        menu = SideMenu(self.window, frames, frames[0]).create_menu()
        menu.pack(side="left", fill=tk.Y, padx=(0, 10))
        frames[0].pack(fill="both", expand=True)

        self.window.mainloop()


#app = App()
#app.run()
