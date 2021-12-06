from dao.personDAO import PersonDAO
from model.personModel import Person


class PersonService:
    def __init__(self):
        self.person_DAO = PersonDAO()

    def insert_person(self, person: Person):
        self.person_DAO.insert_person(person.firstname, person.lastname)

    def get_person(self, person: Person) -> Person:
        result = self.person_DAO.select_person_by_firstname_and_lastname(person.firstname, person.lastname)

        return Person(result[1], result[2])
