from googleapiclient.errors import HttpError

from create_gsheet_service import CreateService
from utils import (
    print_formatted_error,
    print_formatted_exception,
    print_formatted_output,
)

GOOGLE_SHEET_ID, sheet = CreateService.create_service()


class ReadOperation:
    """Read Operations"""

    @staticmethod
    def read_from_sheet_single_range():
        SHEET_RANGE = "Student Data!A1:E12"

        try:
            request = sheet.values().get(
                spreadsheetId=GOOGLE_SHEET_ID, range=SHEET_RANGE
            )
            result = request.execute()
            print_formatted_output(result)

        except HttpError as err:
            print_formatted_error(err.status_code)
            print_formatted_error(err.error_details)

    @staticmethod
    def read_from_sheet_multiple_range():
        SHEET_RANGES = ["Student Data", "Sheet2!B3:E4", "Sheet2!A1:F5"]

        try:
            request = sheet.values().batchGet(
                spreadsheetId=GOOGLE_SHEET_ID, ranges=SHEET_RANGES
            )
            result = request.execute()
            print_formatted_output(result)

        except Exception as exception:
            print_formatted_exception(str(exception))


if __name__ == "__main__":
    pass
    # ReadOperation.read_from_sheet_single_range()
    # ReadOperation.read_from_sheet_multiple_range()
