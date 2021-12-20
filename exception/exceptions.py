class DbConnectionException(Exception):
    pass


class PersonExists(Exception):
    pass


class PersonDoesNotExistException(Exception):
    pass


class InvalidStartDatetime(Exception):
    pass


class InvalidEndDatetime(Exception):
    pass
