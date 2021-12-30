from dao.personDAO import PersonDAO
from model.personModel import Person
from exception.exceptions import *


class PersonService:
    def __init__(self):
        self.person_DAO = PersonDAO()

    def insert_person(self, firstname, lastname):
        try:
            self.person_DAO.insert_person(firstname, lastname)
        except Exception:
            raise

    def get_person(self, person: Person) -> Person:
        try:
            result = self.person_DAO.select_person_by_firstname_and_lastname(person.firstname, person.lastname)
        except Exception:
            raise

        else:

            return Person(result['lastname'], result['firstname'], result['id']) if result is not None else None
