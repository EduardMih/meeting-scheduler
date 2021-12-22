from service.importExportService import ImportExportService


class ImportExportController:
    def __init__(self, view):
        self.import_export_service = ImportExportService()
        self.view = view

    def import_cal(self, file_path):
        self.import_export_service.import_meetings(file_path)
        self.view.show_message(True, "Import", "Import Realizat cu succes")
        #print("import", file_path)

    def export_cal(self, file_path):
        self.import_export_service.export_meetings(file_path.name)
        self.view.show_message(True, "Export", "Export realizat cu suces")
        #print("export", file_path.name)
