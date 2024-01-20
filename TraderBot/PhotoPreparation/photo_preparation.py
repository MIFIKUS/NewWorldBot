from MainClasses.GoogleSheets.google_sheets import GoogleSheets
from MainClasses.Image.image import Image
#image = Image()


list_of_values = []
list_of_uniq_values = []


class PhotoPreparation(Image):

    def __init__(self, main_name, name, number_of_entries, need_for_uniqueness=False):

        self.main_name = main_name
        self.name = name
        self.number_of_entries = number_of_entries
        self.need_for_uniqueness = need_for_uniqueness

    def image_preparation(self):

        for i in range(1, self.number_of_entries + 1):

            self.delete_all_colors_except_one(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\price{i}.png",
                                              [51, 41, 24], [191, 181, 165])
            self.delete_all_colors_except_one(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\avail{i}.png",
                                              [51, 41, 24], [191, 181, 165])

            self.upscale_image(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\price{i}.png", 2)
            self.upscale_image(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\avail{i}.png", 2)

        self.get_data_from_pictures_and_writing_to_list()

    def get_data_from_pictures_and_writing_to_list(self):
        global list_of_values
        global list_of_uniq_values

        types_of_viewing = [6, 8, 7, 13]
        info_diction = {}

        for i in range(1, self.number_of_entries + 1):
            price = self.image_to_string(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\price{i}.png",
                                         True)
            avail = self.image_to_string(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\avail{i}.png",
                                         True)

            if len(price) == 0:
                for installation in types_of_viewing:
                    price = self.image_to_string_custom_confing(
                            f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\price{i}.png",
                            f'--psm {installation} -c tessedit_char_whitelist=0123456789/,.')
                    if len(price) > 0:
                        break

            if len(avail) == 0:
                for installation in types_of_viewing:
                    avail = self.image_to_string_custom_confing(
                        f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\avail{i}.png",
                        f'--psm {installation} -c tessedit_char_whitelist=0123456789/,.')
                    if len(avail) > 0:
                        break

            list_of_values.append([self.main_name, self.name, price, avail])

        if self.need_for_uniqueness is True:

            for sublist in list_of_values:
                key = (sublist[0], sublist[1], sublist[2])
                sublist[3] = sublist[3].replace('.', '').replace(' ', '')
                value = int(sublist[3])

                if key in info_diction:
                    info_diction[key] += value
                else:
                    info_diction[key] = value

            list_of_uniq_values = [[*key, value] for key, value in info_diction.items()]

    def get_scrollbar_size(self, filename, area_of_screenshot):
        self.take_screenshot(filename, area_of_screenshot)
        self.delete_all_colors_except_one(filename, [65, 65, 65], [120, 120, 120])
        slider_size = self.get_slider_size(filename)

        return slider_size





