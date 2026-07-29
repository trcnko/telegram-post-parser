from google.oauth2.service_account import Credentials
import gspread
from config import settings


class SheetsClient:
    def __init__(self):
        try:
            scopes = [
                'https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive'
            ]
            creds = Credentials.from_service_account_file(
                settings.CREDENTIALS_FILE,
                scopes=scopes
            )

            client = gspread.authorize(creds)

            self.sheet = client.open_by_key(settings.GOOGLE_SHEET_ID).worksheet(settings.SHEET_NAME)
            print('Успешное подключение')

        except Exception as e:
            print(f'Ошибка подключения {e}')
            raise

    def append_to_b1(self, formatted_text: str):
        try:
            current_value = self.sheet.acell('B1').value

            if current_value:
                new_value = f"{current_value}\n{formatted_text}"
            else:
                new_value = formatted_text

            self.sheet.update_acell('B1', new_value)
            print(f"Пост добавлен в B1")
        except Exception as e:
            print(f"Ошибка записи {e}")

