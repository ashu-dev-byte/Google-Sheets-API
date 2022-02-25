from create_gsheet_service import CreateService
from utils import get_values_list, print_formatted_exception, print_formatted_output

GOOGLE_SHEET_ID, sheet = CreateService.create_service()


class WriteOpeartions:
    """Write Operation (Upsert) but doesn't clear the whole sheet. It justs overwrite the overlapping cell data."""

    @staticmethod
    def write_to_sheet_single_range():
        SHEET_RANGE = "Sheet2!A1"
        VALUE_INPUT_OPTION = "RAW"  # other option can be USER_ENTERED
        VALUES = get_values_list()
        BODY = {"values": VALUES}

        try:
            request = sheet.values().update(
                spreadsheetId=GOOGLE_SHEET_ID,
                range=SHEET_RANGE,
                valueInputOption=VALUE_INPUT_OPTION,
                body=BODY,
            )
            result = request.execute()
            print_formatted_output(result)

        except Exception as exception:
            print_formatted_exception(str(exception))

    @staticmethod
    def write_to_sheet_multiple_range():
        VALUE_INPUT_OPTION = "RAW"
        DATA = [
            {"range": "Sheet2!A1", "values": get_values_list()},
            {"range": "Sheet2!A11", "values": get_values_list()},
            {"range": "Sheet3!C3", "values": get_values_list()},
        ]
        BODY = {"valueInputOption": VALUE_INPUT_OPTION, "data": DATA}

        try:
            request = sheet.values().batchUpdate(
                spreadsheetId=GOOGLE_SHEET_ID,
                body=BODY,
            )
            result = request.execute()
            print_formatted_output(result)

        except Exception as exception:
            print_formatted_exception(str(exception))


if __name__ == "__main__":
    pass
    # WriteOpeartions.write_from_sheet_single_range()
    # WriteOpeartions.write_from_sheet_multiple_range()
