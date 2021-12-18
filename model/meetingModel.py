from model.personModel import Person


class Meeting:
    def __init__(self, start_date, end_date, attendees_list: [Person]):
        self.start_date = start_date
        self.end_date = end_date
        self.attendees_list: [Person] = attendees_list
