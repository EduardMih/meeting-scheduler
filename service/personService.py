from dao.personDAO import PersonDAO
from model.personModel import Person
from exception.exceptions import *


class PersonService:
    def __init__(self):
        self.person_DAO = PersonDAO()

    def insert_person(self, person: Person):
        try:
            self.person_DAO.insert_person(person.firstname, person.lastname)
        except PersonExists as e:
            print("Persoana exista")

        except Exception:

            print("Exceptie necunoscuta la insert person")

    def get_person(self, person: Person) -> Person:
        try:
            result = self.person_DAO.select_person_by_firstname_and_lastname(person.firstname, person.lastname)
        except Exception:
            print("Exceptie necunoscuta la get person")

        else:

            return Person(result[1], result[2], result[0]) if result is not None else None
