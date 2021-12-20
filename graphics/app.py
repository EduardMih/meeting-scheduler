import tkinter as tk
from graphics.listEventsPage import ListEventsPage
from graphics.sideMenu import SideMenu
from graphics.addPersonPage import AddPerssonPage
from graphics.addMeetingPage import AddMeetingPage
from controller.personController import PersonController
from controller.meetingController import MeetingController
from controller.listMeetingController import ListMeetingController


class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Meeting scheduler")
        self.window.minsize(width=1000, height=800)
        self.window.configure(bg="grey")

    def run(self):
        self.window.update()

        add_person = AddPerssonPage(self.window)
        person_controller = PersonController(add_person)
        add_person.set_controller(person_controller)

        add_meeting = AddMeetingPage(self.window)
        meeting_controller = MeetingController(add_meeting)
        add_meeting.set_controller(meeting_controller)

        list_meetings = ListEventsPage(self.window)
        list_meetings_controller = ListMeetingController(list_meetings)
        list_meetings.set_controller(list_meetings_controller)

        frames = [add_person.create_page(),
                  add_meeting.create_page(),
                  list_meetings.create_page()]

        menu = SideMenu(self.window, frames, frames[0]).create_menu()
        menu.pack(side="left", fill=tk.Y, padx=(0, 10))
        frames[0].pack(fill="both", expand=True)

        self.window.mainloop()


app = App()
app.run()
