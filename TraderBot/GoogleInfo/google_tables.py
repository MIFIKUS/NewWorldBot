from MainClasses.GoogleSheets.google_sheets import GoogleSheets


class GetInfo(GoogleSheets):
    """"""
    def __init__(self, SPREADSHEET_URL="https://docs.google.com/spreadsheets/d/1nFUIPW6nUTc5CfMroHsCCKzlOG4-9rEZGVmSHc9zMog/edit#gid=0",
                       credentials="D:\Python_progect\\NewWorldBot\\services_files\\credentials.json",
                       num_of_sheet=0):
        super().__init__(SPREADSHEET_URL, credentials, num_of_sheet)

    def get_info(self):
        get = self.get_value_from_cell("A2:A4")
        print(get)


class WriteInfo(GoogleSheets):
    pass


get_info = GetInfo()
get_info.get_info()

