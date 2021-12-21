class DbConnectionException(Exception):
    pass


class PersonExists(Exception):
    pass


class PersonDoesNotExistException(Exception):
    def __init__(self, person):
        self.person = person


class InvalidStartDatetime(Exception):
    pass


class InvalidEndDatetime(Exception):
    pass


class InvalidTimeInterval(Exception):
    pass
