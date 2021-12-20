from model.personModel import Person


class Meeting:
    def __init__(self, title=None, start_date=None, end_date=None, attendees_list: [Person] = None, meeting_id=None):
        self.id = meeting_id
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.attendees_list: [Person] = attendees_list if attendees_list is not None else []
