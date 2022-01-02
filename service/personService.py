from dao.personDAO import PersonDAO
from model.personModel import Person
from exception.exceptions import *


class PersonService:
    """
    Class to validate controller requests and call appropriate DAO methods to perform desired action.
    """
    def __init__(self):
        """
        PersonService class constructor to initialize object.
        """
        self.person_DAO = PersonDAO()

    def insert_person(self, firstname, lastname):
        """
        Method to add a new person. Checks if firstname and lastname contains only alphabets.

        :param firstname: Person's firstname.
        :param lastname: Person's lastname.
        :return: None
        """
        if (not firstname.isalpha()) or (not lastname.isalpha()):
            raise InvalidNameFormat

        try:
            self.person_DAO.insert_person(firstname, lastname)
        except Exception:
            raise

    def get_person(self, person: Person) -> Person:
        """
        Method to select a person by firstname and lastname.
        :param person: Person to be searched.
        :return: Person with full details.
        """
        try:
            result = self.person_DAO.select_person_by_firstname_and_lastname(person.firstname, person.lastname)
        except Exception:
            raise

        else:

            return Person(result['lastname'], result['firstname'], result['id']) if result is not None else None
