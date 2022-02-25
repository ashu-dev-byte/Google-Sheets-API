from create_gsheet_service import CreateService
from utils import print_formatted_exception, print_formatted_output

GOOGLE_SHEET_ID, sheet = CreateService.create_service()


class CreateSpreadsheetOperation:
    """Create Spreadsheet Operations"""

    @staticmethod
    def create_spreadsheet_with_sheets():
        """Don't use this approach because although sheets get created, access is not provided"""

        BODY = {
            "properties": {"title": "Spreadsheet 1", "timeZone": "Asia/Calcutta"},
            "sheets": [
                {"properties": {"title": "API Sheet 1"}},
                {"properties": {"title": "API Sheet 2"}},
            ],
        }

        try:
            request = sheet.create(body=BODY)
            result = request.execute()
            print_formatted_output(result)

        except Exception as exception:
            print_formatted_exception(str(exception))


if __name__ == "__main__":
    pass
    # CreateSpreadsheetOperation.create_spreadsheet_with_sheets()
