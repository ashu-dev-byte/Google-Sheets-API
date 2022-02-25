from create_gsheet_service import CreateService
from utils import get_values_list, print_formatted_exception, print_formatted_output

GOOGLE_SHEET_ID, sheet = CreateService.create_service()


class AppendOperation:
    """On encountering a overlapping row, tries to get the nearest empty row."""

    @staticmethod
    def append_to_sheet_single_range():
        SHEET_RANGE = "Sheet3!L7"
        VALUE_INPUT_OPTION = "RAW"
        VALUES = get_values_list()
        BODY = {"values": VALUES}

        try:
            request = sheet.values().append(
                spreadsheetId=GOOGLE_SHEET_ID,
                range=SHEET_RANGE,
                valueInputOption=VALUE_INPUT_OPTION,
                body=BODY,
            )
            result = request.execute()
            print_formatted_output(result)

        except Exception as exception:
            print_formatted_exception(str(exception))


if __name__ == "__main__":
    pass
    # AppendOperation.append_to_sheet_single_range()
