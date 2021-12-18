class Person:
    def __init__(self, lastname, firstname, person_id=None):
        self.id = person_id
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self) -> str:

        return self.lastname + " " + self.firstname










