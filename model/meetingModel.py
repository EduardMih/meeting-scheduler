from model.personModel import Person


class Meeting:
    def __init__(self, start_date, start_hour, end_date, end_hour, attendees_list: [Person]):
        self.start_date = start_date
        self.start_hour = start_hour
        self.end_date = end_date
        self.end_hour = end_hour
        self.attendees_list = attendees_list
