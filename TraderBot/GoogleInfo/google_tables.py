from MainClasses.GoogleSheets.google_sheets import GoogleSheets
from TraderBot.shared_variables import path_to_services_files


class GetInfo(GoogleSheets):
    """"""
    def __init__(self, SPREADSHEET_URL="https://docs.google.com/spreadsheets/d/1nFUIPW6nUTc5CfMroHsCCKzlOG4-9rEZGVmSHc9zMog/edit#gid=0",
                 credentials=path_to_services_files + "credentials.json",
                 num_of_sheet=0):
        super().__init__(SPREADSHEET_URL, credentials, num_of_sheet)

    def get_values_from_cell(self, first, second):
        """Получение диапазона значений определенного столбца
        first = Буква столбца и номер - A1
        second = тоже самое только конечный пункт вводим"""

        value_of_the_cells = self.get_value_from_cell(f"{first}:{second}")
        return value_of_the_cells

    def get_value_list(self, сolumn_number):
        """Получение всех значений определенного значения
        column_number = номер столбца"""

        value_list = self.worksheet.col_values(сolumn_number)
        return value_list

    def get_value_from_one_cell(self, value):
        val = self.worksheet.acell(value).value
        return val


class WriteInfo(GoogleSheets):
    def __init__(self, SPREADSHEET_URL="https://docs.google.com/spreadsheets/d/1nFUIPW6nUTc5CfMroHsCCKzlOG4-9rEZGVmSHc9zMog/edit#gid=0",
                 credentials="E:\\projects\\NewWorldBot\\services_files\\credentials.json",
                 num_of_sheet=0):
        super().__init__(SPREADSHEET_URL, credentials, num_of_sheet)

    def write_list_of_values(self, name_of_sheet, dict_of_values):
        self.sh.values_update(f'{name_of_sheet}',
                              params={
                                  'valueInputOption': 'USER_ENTERED'
                              },
                              body={
                                  'values': dict_of_values
                              }
                              )

