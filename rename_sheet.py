from create_gsheet_service import CreateService
from utils import print_formatted_exception, print_formatted_output

GOOGLE_SHEET_ID, sheet = CreateService.create_service()


class RenameOperations:
    """Rename Operations"""

    @staticmethod
    def rename_sheet(old_sheet_name, new_sheet_name):
        try:
            # getting all sheet names
            request = sheet.get(spreadsheetId=GOOGLE_SHEET_ID)
            result = request.execute()["sheets"]
            sheets = list(map(lambda sheet: sheet["properties"]["title"], result))

            if new_sheet_name in sheets:
                print_formatted_output(
                    "A Sheet with given new_sheet_name already exists."
                )
                return

            if old_sheet_name not in sheets:
                print_formatted_output("Sheet with given old_sheet_name doesn't exist.")
                return

            else:
                old_sheet_name_id = list(
                    map(
                        lambda sheet: sheet["properties"]["sheetId"],
                        filter(
                            lambda sheet: sheet["properties"]["title"]
                            == old_sheet_name,
                            result,
                        ),
                    )
                )[0]
                BODY = {
                    "requests": [
                        {
                            "updateSheetProperties": {
                                "properties": {
                                    "sheetId": old_sheet_name_id,
                                    "title": new_sheet_name,
                                },
                                "fields": "title",
                            }
                        },
                    ],
                }
                request = sheet.batchUpdate(
                    spreadsheetId=GOOGLE_SHEET_ID,
                    body=BODY,
                ).execute()
                print_formatted_output(request, "Sheet Renamed!")

        except Exception as exception:
            print_formatted_exception(str(exception))


if __name__ == "__main__":
    pass
    # RenameOperations.rename_sheet("Sheet1", "CobaltBlue")
