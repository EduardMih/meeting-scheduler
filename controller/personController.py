from service.personService import PersonService
from exception.exceptions import *


class PersonController:
    """
    Class responsible for linking add person page with person service.
    """
    def __init__(self, view):
        """
        PersonController class constructor to initialize the object.

        :param view: View to display add person from.
        """
        self.person_service = PersonService()
        self.view = view

    def add_person(self, firstname, lastname):
        """
        Method to be called from view that calls person service appropriate method to insert a new person.
        After the operation is completed view method is called to display corresponding message.

        :param firstname: Person's firstname.
        :param lastname: Person's lastname.
        :return: None
        """
        try:
            self.person_service.insert_person(firstname, lastname)

            self.view.show_message_label(True)
            self.view.clear_form()
        except PersonExists:
            self.view.show_message_label(False, "Persoana exista deja!")
        except InvalidNameFormat:
            self.view.show_message_label(False, "Firstname/lastname trebuie sa contina doar litere!")
        except Exception:
            self.view.show_message_label(False, "Eroare necunoscuta la adaugare persoana!")
