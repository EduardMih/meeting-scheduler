from graphics.app import App
from model.dbConnection import DbConnection
from model.personModel import Person
from model.meetingModel import Meeting
from service.personService import PersonService
from service.meetingService import MeetingService
import datetime
#app = App()
#app.run()

#person = Person("Lorena", "Popescu")
#person.insert_person()
#person_service = PersonService()
#print(person_service.get_person(person))

#person_service.insert_person(person)

current = datetime.datetime.now()
add = datetime.timedelta(hours=2)
future = current + add
#print(current, future)

meeting = Meeting(current, future, [Person("Lorena", "Popescu"), Person("Zahar", "Andrei")])
meeting_service = MeetingService()
meeting_service.insert_meeting(meeting)
