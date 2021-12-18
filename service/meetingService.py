from dao.meetingDAO import MeetingDAO
from dao.meetingPersonDAO import MeetingPersonDAO
from dao.personDAO import PersonDAO
from model.meetingModel import Meeting
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

                self.meeting_person_DAO.insert_meeting_person(new_meeting_id, row[0])

        except PersonDoesNotExistException:
            raise
        except Exception as e:
            print("Exceptie necunoscuta la insert meeting")
