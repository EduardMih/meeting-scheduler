from dao.meetingDAO import MeetingDAO
from dao.meetingPersonDAO import MeetingPersonDAO
from dao.personDAO import PersonDAO
from model.meetingModel import Meeting
from model.personModel import Person
from exception.exceptions import *
from datetime import datetime
import pytz


class MeetingService:
    def __init__(self):
        self.meeting_DAO = MeetingDAO()
        self.meeting_person_DAO = MeetingPersonDAO()
        self.person_DAO = PersonDAO()
        self.date_format = "%d-%m-%Y %H:%M"

    def insert_meeting(self, title, start_date, end_date, attendees: [(str, str)]):

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

        except PersonDoesNotExistException:
            raise
        except Exception as e:
            print("Exceptie necunoscuta la insert meeting in service")

    def filter_meetings(self, start_date, end_date) -> [Meeting]:
        start = self.convert_date(start_date)

        if not start:
            raise InvalidStartDatetime

        end = self.convert_date(end_date)

        if not end:
            raise InvalidEndDatetime

        try:
            meetings_list = []
            meeting_rows = self.meeting_DAO.filter_meetings_by_date(start, end)

            for meeting_row in meeting_rows:
                meeting = Meeting(meeting_row['title'], meeting_row['start_date'],
                                  meeting_row['end_date'], None, meeting_row['id'])

                attendees_id_list = [x['person_id'] for x in self.meeting_person_DAO.select_all_meeting_attendees(meeting_row['id'])]
                for attendee_id in attendees_id_list:
                    attendee_row = self.person_DAO.select_person_by_id(attendee_id)
                    meeting.attendees_list.append(Person(attendee_row['lastname'],
                                                         attendee_row['firstname'],
                                                         attendee_row['id']))

                meetings_list.append(meeting)

            return meetings_list

        except Exception as e:
            print(e)

    def convert_date(self, date):
        try:
            date_time_obj = datetime.strptime(date, self.date_format)
            timezone = pytz.timezone("Europe/Bucharest")
            timezone.localize(date_time_obj)
        except ValueError:

            return False

        else:

            return date_time_obj


