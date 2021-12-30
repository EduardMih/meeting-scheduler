from model.personModel import Person


class Meeting:
    """
    Class to model meeting entity.
    """
    def __init__(self, title=None, start_date=None, end_date=None, attendees_list: [Person] = None, meeting_id=None):
        """
        Meeting class constructor to initialize object.

        :param title: Meeting title.
        :param start_date: Meeting start date.
        :param end_date: Meeting end date.
        :param attendees_list: Meeting attendees list
        :param meeting_id: Meeting id.
        """
        self.id = meeting_id
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.attendees_list: [Person] = attendees_list if attendees_list is not None else []
