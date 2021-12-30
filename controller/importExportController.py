from service.importExportService import ImportExportService
from exception.exceptions import *


class ImportExportController:
    """
    Class responsible for linking import/export views with import/export service.
    """
    def __init__(self, view):
        """
        ImportExportController constructor to initialize object
        .
        :param view: View responsible for displaying information about import/export operations.
        """
        self.import_export_service = ImportExportService()
        self.view = view

    def import_cal(self, file_path):
        """
        Method to be called from view in order to import calendar data from file. After completing the operation
        sets corresponding message in view.

        :param file_path: Path to file from which to import data.
        :return: None
        """
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

    def export_cal(self, file_path):
        """
        Method to be called from view in order to export calendar data to file. After completing the operation
        sets corresponding message in view.

        :param file_path: Path to file where to export data.
        :return: None
        """
        try:
            self.import_export_service.export_meetings(file_path.name)
        except Exception:
            self.view.show_message(False, "Export", "Eroare necunoscuta la export")

        else:
            self.view.show_message(True, "Export", "Export realizat cu succes")
