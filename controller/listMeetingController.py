from service.meetingService import MeetingService
from exception.exceptions import *


class ListMeetingController:
    """
    Class responsible for linking list meetings page with meetings service.
    """
    def __init__(self, view):
        """
        ListMeetingController class constructor to initialize object.

        :param view: View responsible for displaying meetings list.
        """
        self.meeting_service = MeetingService()
        self.view = view
        self.date_format = '%d-%m-%Y %H:%M'

    def get_meetings(self, start_date, start_hour, end_date, end_hour):
        """
        Method to be called from view that calls meeting service appropriate function to select all meetings
        inside time range.
        After completing the operation calls view method to display meetings or to show error message.

        :param start_date: Start date string dd-mm-yyyy
        :param start_hour: Start hour string hh:mm
        :param end_date: End date string dd-mm-yyyy
        :param end_hour: End hour string hh:mm
        :return: None
        """
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

        except InvalidStartDatetime:
            self.view.show_message_label(False, "Start date/hour nu este formatat corect!")

        except InvalidEndDatetime:
            self.view.show_message_label(False, "End date/hours nu este formatat corect!")

        except InvalidTimeInterval:
            self.view.show_message_label(False, "Intervalul de timp nu este corect!")

        except Exception:
            self.view.show_message_label(False, "Exceptie necunoscuta la preluare meeting")
