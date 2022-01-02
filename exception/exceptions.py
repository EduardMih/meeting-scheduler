class PersonExists(Exception):
    """
    Exception raised when the person attempted to be inserted already exists.
    """
    pass


class PersonDoesNotExistException(Exception):
    """
    Exception raised when a person that doesn't exist is tried to be used.
    """
    def __init__(self, person):
        self.person = person


class InvalidStartDatetime(Exception):
    """
    Exception raised when Start datetime string is misformatted.
    """
    pass


class InvalidEndDatetime(Exception):
    """
    Exception raised when end datetime string is misformatted.
    """
    pass


class InvalidTimeInterval(Exception):
    """
    Exception raised when time range is not correct.
    """
    pass


class InvalidNameFormat(Exception):
    """
    Exception raised when firstname or lastname contains anything else but alphabets.
    """
    pass
