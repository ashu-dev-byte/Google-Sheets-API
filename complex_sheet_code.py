from create_gsheet_service import CreateService
from utils import get_values_list, print_formatted_exception, print_formatted_output

GOOGLE_SHEET_ID, sheet = CreateService.create_service()


class ComplexSheetCode:
    """Complex Sheet Code Operations"""

    @staticmethod
    def complex_sheet_code(sheet_range):
        """String followed by '#' is a unique number to keep track of unique objects/entities."""
        try:
            sheet_rule_id = sheet_range.split("!")[0].split("#")[-1]
            sheet_name = sheet_range.split("!")[0]

            # getting all sheets data in spreadsheet
            sheet_list = sheet.get(spreadsheetId=GOOGLE_SHEET_ID).execute()["sheets"]
            print_formatted_output("", "Fetched all sheets data!")

            # trying to get the sheet with same sheet_rule_id
            request_sheet_rule_id = list(
                map(
                    lambda x: {
                        "sheet_id": x["properties"]["sheetId"],
                        "title": x["properties"]["title"],
                    },
                    filter(
                        lambda y: y["properties"]["title"].split("#")[-1]
                        == sheet_rule_id,
                        sheet_list,
                    ),
                )
            )
            print_formatted_output(request_sheet_rule_id, "Request Sheet Rule Id")

            # creating new sheet tab if sheet with same sheet_rule_id is not present
            if not request_sheet_rule_id:
                batch_update_request_make_new_sheet = {
                    "requests": [{"addSheet": {"properties": {"title": sheet_name}}}],
                }
                response_make_new_tab = sheet.batchUpdate(
                    spreadsheetId=GOOGLE_SHEET_ID,
                    body=batch_update_request_make_new_sheet,
                ).execute()
                print_formatted_output(
                    response_make_new_tab, "Sheet not found, Created New Sheet"
                )

            else:
                # renaming sheet if it doesn't match with input sheet_name
                if request_sheet_rule_id[0]["title"] != sheet_name:
                    batch_update_request_rename_sheet = {
                        "requests": [
                            {
                                "updateSheetProperties": {
                                    "properties": {
                                        "sheetId": request_sheet_rule_id[0]["sheet_id"],
                                        "title": sheet_name,
                                    },
                                    "fields": "title",
                                }
                            },
                        ],
                    }
                    response_rename_sheet = sheet.batchUpdate(
                        spreadsheetId=GOOGLE_SHEET_ID,
                        body=batch_update_request_rename_sheet,
                    ).execute()
                    print_formatted_output(
                        response_rename_sheet,
                        "Sheet Name doesn't match, Sheet Renamed",
                    )

                # clearing sheet data
                response_clear_sheet = (
                    sheet.values()
                    .clear(
                        spreadsheetId=GOOGLE_SHEET_ID,
                        range=sheet_name,
                    )
                    .execute()
                )
                print_formatted_output(response_clear_sheet, "Sheet Data Cleared")

            # writing data to sheet
            batch_update_request_put_values = {
                "value_input_option": "RAW",
                "data": [{"range": sheet_range, "values": get_values_list()}],
            }
            response_put_values = (
                sheet.values()
                .batchUpdate(
                    spreadsheetId=GOOGLE_SHEET_ID, body=batch_update_request_put_values
                )
                .execute()
            )
            print_formatted_output(response_put_values, "Data written to Sheet")
            print_formatted_output(
                response_put_values["responses"][0]["updatedRange"].replace("'", ""),
                "Updated Range",
            )

        except Exception as exception:
            print_formatted_exception(str(exception))


if __name__ == "__main__":
    pass
    # ComplexSheetCode.complex_sheet_code("A New Sheet#14!A1:E30")
