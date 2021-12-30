from dao.meetingDAO import MeetingDAO
from dao.meetingPersonDAO import MeetingPersonDAO
from dao.personDAO import PersonDAO
from model.meetingModel import Meeting
from model.personModel import Person
from exception.exceptions import *
from datetime import datetime
import pytz


class MeetingService:
    """
    Class to validate controller request and call appropriate DAOs to perform desired action.
    """
    def __init__(self):
        """
        MeetingService class constructor to initialize object.
        """
        self.meeting_DAO = MeetingDAO()
        self.meeting_person_DAO = MeetingPersonDAO()
        self.person_DAO = PersonDAO()
        self.date_format = "%d-%m-%Y %H:%M"

    def insert_meeting(self, title, start_date, end_date, attendees: [(str, str)]):
        """
        Method to validate user input, raise exception in case of problems,
        and call DAO methods to insert a new meeting.

        :param title: Meeting title.
        :param start_date: Meeting start date.
        :param end_date: Meeting end date.
        :param attendees: List of tuples containing firstname and lastname
        :return: None
        """

        start = self.convert_date(start_date)

        if not start:
            raise InvalidStartDatetime

        end = self.convert_date(end_date)

        if not end:
            raise InvalidEndDatetime

        if start > end:
            raise InvalidTimeInterval

        try:
            new_meeting_id = self.meeting_DAO.insert_meeting(title, start, end)

            for attendee in attendees:
                row = self.person_DAO.select_person_by_firstname_and_lastname(attendee[0],
                                                                              attendee[1])

                if row is None:

                    raise PersonDoesNotExistException(Person(attendee[1], attendee[0]))

                self.meeting_person_DAO.insert_meeting_person(new_meeting_id, row['id'])

        except Exception:
            raise

    def filter_meetings(self, start_date, end_date) -> [Meeting]:
        """
        Method to filter meetings according to time range.
        Time range validations are performed and exceptions raised in case of problems.

        :param start_date: Time range start.
        :param end_date: Time range end.
        :return: Selected meetings list.
        """
        start = self.convert_date(start_date)

        if not start:
            raise InvalidStartDatetime

        end = self.convert_date(end_date)

        if not end:
            raise InvalidEndDatetime

        if start > end:
            raise InvalidTimeInterval

        try:
            meeting_rows = self.meeting_DAO.filter_meetings_by_date(start, end)

            meetings_list = self.create_meeting_list(meeting_rows)

            return meetings_list

        except Exception:
            raise

    def get_all_meetings(self):
        """
        Method to select all meetings.

        :return: All meetings' data list.
        """
        try:
            meeting_rows = self.meeting_DAO.select_all_meetings()

            meetings_list = self.create_meeting_list(meeting_rows)

            return meetings_list

        except Exception:
            raise

    def create_meeting_list(self, meeting_rows):
        """
        Auxiliary method to pack meetings.

        :param meeting_rows: List off meetings' data.
        :return: Meetings list
        """
        try:
            meetings_list = []
            for meeting_row in meeting_rows:
                meeting = Meeting(meeting_row['title'], meeting_row['start_date'],
                                 meeting_row['end_date'], None, meeting_row['id'])

                attendees_id_list = [x['person_id'] for x in
                                 self.meeting_person_DAO.select_all_meeting_attendees(meeting_row['id'])]
                for attendee_id in attendees_id_list:
                    attendee_row = self.person_DAO.select_person_by_id(attendee_id)
                    meeting.attendees_list.append(Person(attendee_row['lastname'],
                                                     attendee_row['firstname'],
                                                     attendee_row['id']))

                meetings_list.append(meeting)

            return meetings_list

        except Exception:
            raise


    def convert_date(self, date):
        """
        Auxiliary method to convert string to date, and validate date format.

        :param date: Date string.
        :return: Datetime object corresponding to string.
        """
        try:
            date_time_obj = datetime.strptime(date, self.date_format)
            timezone = pytz.timezone("Europe/Bucharest")
            timezone.localize(date_time_obj)
        except ValueError:

            return False

        else:

            return date_time_obj


