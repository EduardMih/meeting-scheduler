from dao.meetingDAO import MeetingDAO
from dao.meetingPersonDAO import MeetingPersonDAO
from dao.personDAO import PersonDAO
from model.meetingModel import Meeting
from model.personModel import Person
from exception.exceptions import *


class MeetingService:
    def __init__(self):
        self.meeting_DAO = MeetingDAO()
        self.meeting_person_DAO = MeetingPersonDAO()
        self.person_DAO = PersonDAO()

    def insert_meeting(self, meeting: Meeting):
        try:
            new_meeting_id = self.meeting_DAO.insert_meeting(meeting.start_date, meeting.end_date)

            for attendee in meeting.attendees_list:
                row = self.person_DAO.select_person_by_firstname_and_lastname(attendee.firstname,
                                                                              attendee.lastname)

                if row is None:

                    raise PersonDoesNotExistException

                self.meeting_person_DAO.insert_meeting_person(new_meeting_id, row['id'])

        except PersonDoesNotExistException:
            raise
        except Exception as e:
            print("Exceptie necunoscuta la insert meeting")

    def filter_meetings(self, start_date, end_date) -> [Meeting]:
        try:
            meetings_list = []
            meeting_rows = self.meeting_DAO.filter_meetings_by_date(start_date, end_date)

            for meeting_row in meeting_rows:
                meeting = Meeting(meeting_row['start_date'], meeting_row['end_date'], None, meeting_row['id'])

                attendees_id_list = [x[1] for x in self.meeting_person_DAO.select_all_meeting_attendees(meeting_row['id'])]
                for attendee_id in attendees_id_list:
                    attendee_row = self.person_DAO.select_person_by_id(attendee_id)
                    meeting.attendees_list.append(Person(attendee_row['lastname'],
                                                         attendee_row['firstname'],
                                                         attendee_row['id']))

                meetings_list.append(meeting)

                return meetings_list

        except Exception as e:
            print(e)
