from create_gsheet_service import CreateService
from utils import print_formatted_exception, print_formatted_output

GOOGLE_SHEET_ID, sheet = CreateService.create_service()


class ClearOperations:
    """Clear Operations"""

    @staticmethod
    def clear_sheet_single_range():
        SHEET_RANGE = "Sheet3"

        try:
            request = sheet.values().clear(
                spreadsheetId=GOOGLE_SHEET_ID,
                range=SHEET_RANGE,
            )
            result = request.execute()
            print_formatted_output(result)

        except Exception as exception:
            print_formatted_exception(str(exception))

    @staticmethod
    def clear_sheet_multiple_range():
        BODY = {"ranges": ["Sheet2!A1:C4", "Sheet3"]}

        try:
            request = sheet.values().batchClear(
                spreadsheetId=GOOGLE_SHEET_ID,
                body=BODY,
            )
            result = request.execute()
            print_formatted_output(result)

        except Exception as exception:
            print_formatted_exception(str(exception))


if __name__ == "__main__":
    pass
    # clear_sheet_single_range()
    # clear_sheet_multiple_range()
