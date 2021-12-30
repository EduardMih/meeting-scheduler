from service.meetingService import MeetingService
from exception.exceptions import *


class MeetingController:
    """
    Class responsible for linking add meeting page with meeting service.
    """
    def __init__(self, view):
        """
        MeetingController class constructor to initialize object.

        :param view: View responsible for displaying add meeting form.
        """
        self.meeting_service = MeetingService()
        self.view = view
        self.date_format = '%d-%m-%Y %H:%M'

    def add_meeting(self, title, start_date, start_hour, end_date, end_hour, attendees: str):
        """
        Method called by view that calls meeting service appropriate function to insert a new meeting.
        After completing the operation calls view method to display corresponding message.

        :param title: Meeting title.
        :param start_date: Start date string dd-mm-yyyy.
        :param start_hour: Start hour string hh:mm.
        :param end_date: End date string dd-mm-yyyy.
        :param end_hour: End hour string hh:mm.
        :param attendees: List of strings containing attendees lastname and first name.
        :return:
        """
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

        except InvalidStartDatetime:
            self.view.show_message_label(False, "Start date/hour nu este formatat corect!")

        except InvalidEndDatetime:
            self.view.show_message_label(False, "End date/hours nu este formatat corect!")

        except InvalidTimeInterval:
            self.view.show_message_label(False, "Intervalul de timp nu este corect")

        except PersonDoesNotExistException as e:
            self.view.show_message_label(False, "Persona {} {} nu exista".format(e.person.lastname, e.person.firstname))

        except Exception:
            self.view.show_message_label(False, "Exceptie necunoscuta la adaugare meeting")
