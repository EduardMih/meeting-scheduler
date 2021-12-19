from graphics.app import App
from model.dbConnection import DbConnection
from model.personModel import Person
from model.meetingModel import Meeting
from service.personService import PersonService
from dao.meetingDAO import MeetingDAO
from service.meetingService import MeetingService
import datetime
#app = App()
#app.run()

person = Person("Lorena", "LAA")
person_service = PersonService()
person_service.insert_person(person)
print(person_service.get_person(person))

#person_service.insert_person(person)

current = datetime.datetime.now()
add = datetime.timedelta(hours=2)
future = current + add
future2 = current - add
#print(current, future)

meeting = Meeting(current, future, [Person("Lorena", "Popescu"), Person("Zamurca", "Andrei")])
meeting_service = MeetingService()
meeting_service.insert_meeting(meeting)
rows = meeting_service.filter_meetings(future2, future)
print(rows)

#mdao = MeetingDAO()
#print(mdao.filter_meetings_by_date(current, future))

