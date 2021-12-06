from graphics.app import App
from model.dbConnection import DbConnection
from model.personModel import Person
from service.personService import PersonService
#app = App()
#app.run()

person = Person("Lorena", "Popescu")
#person.insert_person()
person_service = PersonService()
print(person_service.get_person(person))


