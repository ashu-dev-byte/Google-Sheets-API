from google.oauth2 import service_account
from googleapiclient.discovery import build

from utils import print_formatted_exception, print_formatted_output

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_ACCOUNT_FILE = "keys.json"

credentials = None
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

# The ID and range of the google sheet.
SHEET_ID = "1pPOmPWNtHEFmAK7mFYGZXJ8A5VVxNwu9-sO2o39El1Y"
SHEET_RANGE = "Student Data!A1:F12"


def read_from_sheet():
    try:
        service = build("sheets", "v4", credentials=credentials)
        sheet = service.spreadsheets()
        request = sheet.values().get(spreadsheetId=SHEET_ID, range=SHEET_RANGE)
        result = request.execute()
        # values = result.get("values", [])
        print_formatted_output(result)

    except Exception as exception:
        print_formatted_exception(str(exception))


if __name__ == "__main__":
    read_from_sheet()
