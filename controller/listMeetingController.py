from service.meetingService import MeetingService
from exception.exceptions import *


class ListMeetingController:
    def __init__(self, view):
        self.meeting_service = MeetingService()
        self.view = view
        self.date_format = '%d-%m-%Y %H:%M'

    def get_meetings(self, start_date, start_hour, end_date, end_hour):
        start = start_date + " " + start_hour
        end = end_date + " " + end_hour
        try:
            meeting_list = self.meeting_service.filter_meetings(start, end)

            meeting_data = []

            for meeting in meeting_list:
                person_list = []
                for person in meeting.attendees_list:
                    person_str = person.lastname + " " + person.firstname
                    person_list.append(person_str)

                meeting_data.append((meeting.title, meeting.start_date.strftime(self.date_format),
                                     meeting.end_date.strftime(self.date_format),
                                     ", ".join(person_list)))

            self.view.show_message_label(True)
            self.view.populate_meetings(meeting_data)
            self.view.refresh()

        except InvalidStartDatetime as e:
            self.view.show_message_label(False, "Start date/hour nu este formatat corect!")

        except InvalidEndDatetime as e:
            self.view.show_message_label(False, "End date/hours nu este formatat corect!")

        except InvalidTimeInterval as e:
            self.view.show_message_label(False, "Intervalul de timp nu este corect!")

        except Exception as e:
            print(e)

