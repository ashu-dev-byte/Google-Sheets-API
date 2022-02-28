from create_gsheet_service import CreateService
from utils import get_values_list, print_formatted_exception, print_formatted_output

GOOGLE_SHEET_ID, sheet = CreateService.create_service()


class ComplexOperations:
    """Complex Operations"""

    @staticmethod
    def delete_all_sheets_except_given_sheets(sheet_names):
        try:
            # getting all sheet info
            request = sheet.get(spreadsheetId=GOOGLE_SHEET_ID)
            result = request.execute()["sheets"]

            # getting all sheet ids except the one whose name was given
            sheet_ids = list(
                map(
                    lambda sheet: sheet["properties"]["sheetId"],
                    filter(
                        lambda sheet: sheet["properties"]["title"] not in sheet_names,
                        result,
                    ),
                )
            )

            if not sheet_ids:
                print_formatted_output("No sheets to be deleted found!")
                return

            # generating delete request body
            BODY = {
                "requests": [
                    {"deleteSheet": {"sheetId": sheet_id}} for sheet_id in sheet_ids
                ]
            }

            # making delete request api call
            delete_request = sheet.batchUpdate(
                spreadsheetId=GOOGLE_SHEET_ID,
                body=BODY,
            )
            delete_result = delete_request.execute()
            print_formatted_output(delete_result, "Sheets Deleted!")

        except Exception as exception:
            print_formatted_exception(str(exception))

    @staticmethod
    def get_or_create_sheet_and_add_data(sheet_name):
        try:
            # getting all sheet names
            request = sheet.get(spreadsheetId=GOOGLE_SHEET_ID)
            result = request.execute()["sheets"]
            sheets = list(map(lambda sheet: sheet["properties"]["title"], result))

            if sheet_name not in sheets:
                BODY = {
                    "requests": [
                        {"addSheet": {"properties": {"title": sheet_name}}},
                    ],
                }
                request = sheet.batchUpdate(
                    spreadsheetId=GOOGLE_SHEET_ID,
                    body=BODY,
                ).execute()
                print_formatted_output(request, "Sheet Created!")
            else:
                request = (
                    sheet.values()
                    .clear(
                        spreadsheetId=GOOGLE_SHEET_ID,
                        range=sheet_name,
                    )
                    .execute()
                )
                print_formatted_output(request, "Sheet already exist, clearing it!")

            # writing data to sheet
            VALUE_INPUT_OPTION = "RAW"
            VALUES = get_values_list()
            BODY = {"values": VALUES}

            write_request = (
                sheet.values()
                .update(
                    spreadsheetId=GOOGLE_SHEET_ID,
                    range=sheet_name,
                    valueInputOption=VALUE_INPUT_OPTION,
                    body=BODY,
                )
                .execute()
            )
            print_formatted_output(write_request, "Data written to sheet.")

        except Exception as exception:
            print_formatted_exception(str(exception))


if __name__ == "__main__":
    pass
    # ComplexOperations.delete_all_sheets_except_given_sheets(
    #     ["Student Data", "Unique Sheet"]
    # )
    # ComplexOperations.get_or_create_sheet_and_add_data("Unique Sheet")
