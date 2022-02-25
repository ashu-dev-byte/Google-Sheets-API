from create_gsheet_service import CreateService
from utils import print_formatted_exception, print_formatted_output

GOOGLE_SHEET_ID, sheet = CreateService.create_service()


class DeleteOperation:
    """Delete Operations"""

    @staticmethod
    def delete_sheets_from_existing_spreadsheet():
        """Google Spreadsheet has a criteria of having at least one sheet, so not all sheets can be deleted"""

        BODY = {
            "requests": [
                {"deleteSheet": {"sheetId": "1799397331"}},  # Here sheetId is gid
                {"deleteSheet": {"sheetId": "970056677"}},
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
    # DeleteOperation.delete_sheets_from_existing_spreadsheet()
