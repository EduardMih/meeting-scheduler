from service.importExportService import ImportExportService

serv = ImportExportService()
#serv.export_meetings("")

meetings = serv.import_meetings("C:\\Users\\hamza\\Desktop\\export.ics")
print(len(meetings))
