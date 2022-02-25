from google.oauth2 import service_account
from googleapiclient.discovery import build


class CreateService:
    @staticmethod
    def create_service():
        GOOGLE_SHEET_ID = "1pPOmPWNtHEFmAK7mFYGZXJ8A5VVxNwu9-sO2o39El1Y"
        SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
        SERVICE_ACCOUNT_FILE = "keys.json"

        credentials = None
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES
        )

        service = build("sheets", "v4", credentials=credentials)
        sheet = service.spreadsheets()

        return GOOGLE_SHEET_ID, sheet
