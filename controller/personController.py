from service.personService import PersonService
from exception.exceptions import *


class PersonController:
    def __init__(self, view):
        self.person_service = PersonService()
        self.view = view

    def add_person(self, firstname, lastname):
        try:
            self.person_service.insert_person(firstname, lastname)

            self.view.show_message_label(True)
        except PersonExists:
            self.view.show_message_label(False, "Persoana exista deja!")
        except Exception as e:
            self.view.show_message_label(False, "Eroare necunoscuta la adaugare persoana!")


