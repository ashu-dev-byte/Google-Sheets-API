from create_gsheet_service import CreateService
from utils import print_formatted_exception, print_formatted_output

GOOGLE_SHEET_ID, sheet = CreateService.create_service()


class CreateOperations:
    """Create Operations"""

    @staticmethod
    def add_sheets_to_existing_spreadsheet():
        BODY = {
            "requests": [
                {
                    "addSheet": {
                        "properties": {
                            "title": "First Sheet",
                            "sheetType": "GRID",
                            "gridProperties": {"rowCount": 50, "columnCount": 20},
                        }
                    }
                },
                {"addSheet": {"properties": {"title": "Second Sheet"}}},
            ],
        }

        try:
            request = sheet.batchUpdate(
                spreadsheetId=GOOGLE_SHEET_ID,
                body=BODY,
            )
            result = request.execute()
            print_formatted_output(result)

        except Exception as exception:
            print_formatted_exception(str(exception))


if __name__ == "__main__":
    pass
    # CreateOperations.add_sheets_to_existing_spreadsheet()
