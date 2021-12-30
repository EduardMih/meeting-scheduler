from service.importExportService import ImportExportService
from exception.exceptions import *


class ImportExportController:
    def __init__(self, view):
        self.import_export_service = ImportExportService()
        self.view = view

    def import_cal(self, file_path):
        try:
            self.import_export_service.import_meetings(file_path)
        except (InvalidStartDatetime, InvalidEndDatetime, InvalidTimeInterval):
            self.view.show_message(False, "Import", "Start/End date formatata gresit")
        except PersonDoesNotExistException:
            self.view.show_message(False, "Import", "Nume de perosana necunoscuta in fisier")

        except Exception:
            self.view.show_message(False, "Import", "Eroare necunoscuta la import")

        else:
            self.view.show_message(True, "Import", "Import Realizat cu succes")
        #print("import", file_path)

    def export_cal(self, file_path):
        try:
            self.import_export_service.export_meetings(file_path.name)
        except Exception:
            self.view.show_message(False, "Export", "Eroare necunoscuta la export")

        else:
            self.view.show_message(True, "Export", "Export realizat cu succes")
        #print("export", file_path.name)
