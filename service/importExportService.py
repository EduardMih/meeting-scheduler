from service.meetingService import MeetingService
from icalendar import Calendar, Event
from datetime import datetime


class ImportExportService:
    """
    Class to validate controller requests, call appropriate meeting service method and
    to write/read data form file.
    """
    def __init__(self):
        """
        ImportExportService class controller to initialize the object.
        """
        self.meeting_service = MeetingService()

    def export_meetings(self, file_path):
        """
        Method that uses meeting service to get all meetings and then exports them in .ics format.

        :param file_path: Path to file where to write calendar in .ics format.
        :return: None
        """
        cal = Calendar()
        try:
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
        except Exception:
            raise

        else:

            with open(file_path, 'wb') as f:
                f.write(cal.to_ical())

    def import_meetings(self, file_path):
        """
        Method that read .ics file, convert data to internal model and insert meetings in database.
        Data validation is performed and exceptions are rise in case of problems.

        :param file_path: Path to the files where to take data from.
        :return: None
        """
        with open(file_path, "rb") as f:
            cal = Calendar.from_ical(f.read())

            try:
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

                        self.meeting_service.insert_meeting(title, start_date.strftime("%d-%m-%Y %H:%M"),
                                                            end_date.strftime("%d-%m-%Y %H:%M"), attendees_list)

            except Exception:
                raise

    def extract_person_from_string(self, string: str):
        """
        Auxiliary method to extract person info from string.

        :param string: String containing lastname and firstname of person.
        :return: (firstname, lastname) tuple
        """
        lastname, firstname = string.split(" ", 1)

        return (firstname, lastname)

