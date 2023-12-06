import gspread

class GoogleSheets:
    """Класс для работы с гугл таблицами"""

    def __init__(self, SPREADSHEET_URL, credentials):
        self.SPREADSHEET_URL = SPREADSHEET_URL
        self.credentials = credentials

        self.gs = gspread.service_account(self.credentials)
        self.sh = self.gs.open_by_url(self.SPREADSHEET_URL)
        self.worksheet = self.sh.sheet1

    def write_google(self, **kwargs):
        """Фуцнкия для записи в гугл таблицу данных\n
        Сюда нужно указать словарь который необходимо записать в таблицу. В таком виде\n
        {Клетка(или диапазон клеток) : значение этой клетки}"""
        for key, value in kwargs.items():
            self.worksheet.update(key, value)

    def get_value_from_cell(self, cell):
        """Функция чтобы получить значение из определенной клетки(или дипазона клеток)"""
        value = self.worksheet.get(cell)
        return value
    