from service.meetingService import MeetingService
from exception.exceptions import *


class MeetingController:
    def __init__(self, view):
        self.meeting_service = MeetingService()
        self.view = view
        self.date_format = '%d-%m-%Y %H:%M'

    def add_meeting(self, title, start_date, start_hour, end_date, end_hour, attendees: str):
        start = start_date + " " + start_hour
        end = end_date + " " + end_hour

        temp = attendees.split('\n')
        while "" in temp:
            temp.remove("")

        try:
            attendee_list = []

            for attendee in temp:
                lastname, firstname = attendee.split(' ', 1)
                attendee_list.append((firstname, lastname))

            self.meeting_service.insert_meeting(title, start, end, attendee_list)

            self.view.show_message_label(True)
            self.view.clear_form()

        except InvalidStartDatetime as e:
            self.view.show_message_label(False, "Start date/hour nu este formatat corect!")

        except InvalidEndDatetime as e:
            self.view.show_message_label(False, "End date/hours nu este formatat corect!")

        except InvalidTimeInterval as e:
            self.view.show_message_label(False, "Intervalul de timp nu este corect")

        except PersonDoesNotExistException as e:
            self.view.show_message_label(False, "Persona {} {} nu exista".format(e.person.lastname, e.person.firstname))

        except Exception as e:
            self.view.show_message_label(False, "Exceptie necunoscuta la adaugare meeting")


