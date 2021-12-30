class Person:
    """
    Class to model person entity.
    """
    def __init__(self, lastname, firstname, person_id=None):
        """
        Person class constructor to initialize object.

        :param lastname: Person lastname.
        :param firstname: Person firstname.
        :param person_id: Person id.
        """
        self.id = person_id
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self) -> str:

        return self.lastname + " " + self.firstname
