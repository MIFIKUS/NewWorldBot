from MainClasses.GoogleSheets.google_sheets import GoogleSheets
from MainClasses.Image.image import Image
from GoogleInfo.google_tables import get_info
image = Image()

cell_num = 2
end_sell = 0
cell_num_uniq = 2


class WriteInSheets:

    def __init__(self, main_name, name, number_of_entries, number_of_sheet, need_for_uniqueness=False):

        self.main_name = main_name
        self.name = name
        self.number_of_entries = number_of_entries
        self.types_of_viewing = [6, 8, 7, 13]
        self.need_for_uniqueness = need_for_uniqueness

        self.google_sheets_second_for_uniq = GoogleSheets(
            "https://docs.google.com/spreadsheets/d/1nFUIPW6nUTc5CfMroHsCCKzlOG4-9rEZGVmSHc9zMog/edit#gid=1830930516",
            "E:\\projects\\NewWorldBot\\services_files\\credentials.json",
            1)

        self.google_sheets = GoogleSheets(
            "https://docs.google.com/spreadsheets/d/1nFUIPW6nUTc5CfMroHsCCKzlOG4-9rEZGVmSHc9zMog/edit#gid=0",
            "E:\\projects\\NewWorldBot\\services_files\\credentials.json",
            number_of_sheet)

    def image_preparation(self):

        for i in range(1, self.number_of_entries + 1):

            image.delete_all_colors_except_one(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\price{i}.png",
                                               [51, 41, 24], [191, 181, 165])
            image.delete_all_colors_except_one(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\avail{i}.png",
                                               [51, 41, 24], [191, 181, 165])

            image.upscale_image(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\price{i}.png", 2)
            image.upscale_image(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\avail{i}.png", 2)
        self.get_numbers_from_pictures()

    def get_numbers_from_pictures(self):
        global end_sell

        price_list = []
        avail_list = []
        main_name_list = []
        name_list = []
        info_diction = {}
        for i in range(1, self.number_of_entries + 1):
            price = image.image_to_string(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\price{i}.png",
                                          True)
            avail = image.image_to_string(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\avail{i}.png",
                                          True)

            if len(price) == 0:
                for installation in self.types_of_viewing:
                    price = image.image_to_string_custom_confing(
                            f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\price{i}.png",
                            f'--psm {installation} -c tessedit_char_whitelist=0123456789/,.')
                    if len(price) > 0:
                        break

            if len(avail) == 0:
                for installation in self.types_of_viewing:
                    avail = image.image_to_string_custom_confing(
                        f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\avail{i}.png",
                        f'--psm {installation} -c tessedit_char_whitelist=0123456789/,.')
                    if len(avail) > 0:
                        break

            price_list.append([price])
            avail_list.append([avail])
            main_name_list.append([self.main_name])
            name_list.append([self.name])
            end_sell += 1

            if self.need_for_uniqueness is True:

                if info_diction.get(price) is None:
                    try:
                        info_diction[price] = int(avail)
                    except:
                        info_diction[price] = 0
                else:
                    amount = info_diction.get(price)
                    info_diction[price] = int(avail) + int(amount)

                if i == self.number_of_entries:
                    self.write_uniq_in_google(info_diction)

        self.write_in_google(main_name_list, name_list, price_list, avail_list)

    def write_uniq_in_google(self, info_diction):
        global cell_num_uniq

        price_stack = list(info_diction.keys())
        avail_stack = list(info_diction.values())

        main_name_stack_list = []
        name_stack_list = []
        price_stack_list = []
        avail_stack_list = []

        for amount in price_stack:
            main_name_stack_list.append([self.main_name])
            name_stack_list.append([self.name])
            price_stack_list.append([amount])
        for avail_amount in avail_stack:
            avail_stack_list.append([avail_amount])

        self.google_sheets_second_for_uniq.write_google({f"A{cell_num_uniq}:A{cell_num_uniq + len(price_stack)}"
                                                    : main_name_stack_list})
        self.google_sheets_second_for_uniq.write_google({f"B{cell_num_uniq}:B{cell_num_uniq + len(price_stack)}"
                                                    : name_stack_list})
        self.google_sheets_second_for_uniq.write_google({f"C{cell_num_uniq}:C{cell_num_uniq + len(price_stack)}"
                                                    : price_stack_list})
        self.google_sheets_second_for_uniq.write_google({f"D{cell_num_uniq}:D{cell_num_uniq + len(price_stack)}"
                                                    : avail_stack_list})
        cell_num_uniq = cell_num_uniq + len(price_stack)

    def write_in_google(self, main_name_list, name_list, price_list, avail_list):
        global cell_num
        global end_sell

        self.google_sheets.write_google({f"A{cell_num}:A{end_sell + 1}": main_name_list})
        self.google_sheets.write_google({f"B{cell_num}:B{end_sell + 1}": name_list})
        self.google_sheets.write_google({f"C{cell_num}:C{end_sell + 1}": price_list})
        self.google_sheets.write_google({f"D{cell_num}:D{end_sell + 1}": avail_list})
        cell_num = end_sell + 1

    @staticmethod
    def calculating_the_best_price():
        counter = 0
        count_of_goods = 0
        list_of_names = get_info.get_value_list(2)[1:]
        list_of_price = get_info.get_value_list(3)[1:]
        list_of_count = get_info.get_value_list(4)[1:]

        for elements_of_column in list_of_names:
            if counter > 1 and list_of_names[counter - 1] != list_of_names[counter]:
                for elements_of_category in range(counter):
                    if (float(list_of_price[count_of_goods]) *
                            float(list_of_count[count_of_goods]) >= 2000):

                        print(list_of_names[count_of_goods],
                              list_of_price[count_of_goods],
                              list_of_count[count_of_goods])
                        count_of_goods += counter
                        break
                    count_of_goods += 1
            counter += 1


#write_in_sheets = WriteInSheets(1, 1, 1, 1)
#write_in_sheets.calculating_the_best_price()

WriteInSheets.calculating_the_best_price()
