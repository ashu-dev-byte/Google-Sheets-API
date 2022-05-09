from create_gsheet_service import CreateService
from utils import print_formatted_exception, print_formatted_output

GOOGLE_SHEET_ID, sheet = CreateService.create_service()


class InfoOperations:
    """Info Operations"""

    @staticmethod
    def get_spreadsheet_info():
        try:
            request = sheet.get(spreadsheetId=GOOGLE_SHEET_ID)
            result = request.execute()
            # Complete Info like ["spreadsheetId", "properties", "sheets", "spreadsheetUrl"]
            print_formatted_output(result)

        except Exception as exception:
            print_formatted_exception(str(exception))

    @staticmethod
    def get_all_sheets_name_in_spreadsheet():
        try:
            request = sheet.get(spreadsheetId=GOOGLE_SHEET_ID)
            result = request.execute()["sheets"]
            sheets = list(map(lambda sheet: sheet["properties"]["title"], result))
            print_formatted_output(sheets, "Sheets")

        except Exception as exception:
            print_formatted_exception(str(exception))

    @staticmethod
    def get_sheet_name_from_gid_in_spreadsheet(sheetId):
        try:
            request = sheet.get(spreadsheetId=GOOGLE_SHEET_ID)
            result = request.execute()["sheets"]
            sheet_obj = list(
                filter(
                    lambda sheet: str(sheet["properties"]["sheetId"]) == sheetId,
                    result,
                ),
            )

            if not sheet_obj:
                print_formatted_exception("No sheet with the given sheetId exists")
                return

            print_formatted_output(sheet_obj[0]["properties"]["title"], "Sheet Name")

        except Exception as exception:
            print_formatted_exception(str(exception))

    @staticmethod
    def get_sheet_gid_from_sheet_name_in_spreadsheet(sheet_name):
        try:
            request = sheet.get(spreadsheetId=GOOGLE_SHEET_ID)
            result = request.execute()["sheets"]
            sheet_obj = list(
                filter(
                    lambda sheet: str(sheet["properties"]["title"]) == sheet_name,
                    result,
                ),
            )

            if not sheet_obj:
                print_formatted_exception("No sheet with the given sheet_name exists")
                return

            print_formatted_output(sheet_obj[0]["properties"]["sheetId"], "Sheet GID")

        except Exception as exception:
            print_formatted_exception(str(exception))


if __name__ == "__main__":
    pass
    # InfoOperations.get_spreadsheet_info()
    # InfoOperations.get_all_sheets_name_in_spreadsheet()
    # InfoOperations.get_sheet_name_from_gid_in_spreadsheet("557067360")
    # InfoOperations.get_sheet_gid_from_sheet_name_in_spreadsheet("First Sheet")
