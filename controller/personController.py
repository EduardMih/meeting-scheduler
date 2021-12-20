from graphics import addPersonPage
from service.personService import PersonService
from model.personModel import Person
from exception.exceptions import *


class PersonController:
    def __init__(self, view):
        self.person_service = PersonService()
        self.view = view

    def add_person(self, firstname, lastname):
        try:
            new_person = Person(lastname, firstname)
            self.person_service.insert_person(new_person)

            self.view.show_message_label(True)
        except PersonExists:
            self.view.show_message_label(False, "Persoana exista deja!")
        except Exception as e:
            self.view.show_message_label(False, "Eroare necunoscuta la adaugare persoana!")


