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

        except InvalidStartDatetime as e:
            self.view.show_message_label(False, "Start date/hour nu este formatat corect!")

        except InvalidEndDatetime as e:
            self.view.show_message_label(False, "End date/hours nu este formatat corect!")

        except Exception as e:
            print(e)


