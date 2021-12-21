from service.meetingService import MeetingService
from model.meetingModel import Meeting
from model.personModel import Person
from icalendar import Calendar, Event
from datetime import datetime


class ImportExportService:
    def __init__(self):
        self.meeting_service = MeetingService()

    def export_meetings(self, file_path):
        cal = Calendar()
        meetings_list = self.meeting_service.get_all_meetings()

        for meeting in meetings_list:
            cal_event = Event()
            cal_event.add('summary', meeting.title)
            cal_event.add('dtstart', meeting.start_date)
            cal_event.add('dtend', meeting.end_date)
            cal_event.add('dtstamp', datetime.now())

            for attendee in meeting.attendees_list:
                cal_event.add('attendee', attendee.lastname + " " + attendee.firstname)

            cal.add_component(cal_event)

        with open("C:\\Users\\hamza\\Desktop\\export.ics", 'wb') as f:
            f.write(cal.to_ical())

    def import_meetings(self, file_path):
        meetings_list = []
        with open(file_path, "rb") as f:
            cal = Calendar.from_ical(f.read())

            for component in cal.walk():
                if component.name == "VEVENT":
                    title = component.get('summary')
                    start_date = component.get('dtstart').dt
                    end_date = component.get('dtend').dt
                    attendees = component.get('attendee')
                    attendees_list = []

                    if isinstance(attendees, str):
                        attendees_list.append(self.extract_person_from_string(attendees))

                    if isinstance(attendees, list):
                        for attendee in attendees:
                            attendees_list.append(self.extract_person_from_string(attendee))

                    meetings_list.append(Meeting(title, start_date, end_date, attendees_list))

        for meeting in meetings_list:
            self.meeting_service.insert_meeting(meeting.title, meeting.start_date.strftime("%d-%m-%Y %H:%M"),
                                                meeting.end_date.strftime("%d-%m-%Y %H:%M"), meeting.attendees_list)

        return meetings_list

    def extract_person_from_string(self, string: str):
        lastname, firstname = string.split(" ", 1)

        #return Person(lastname, firstname)
        return (firstname, lastname)

