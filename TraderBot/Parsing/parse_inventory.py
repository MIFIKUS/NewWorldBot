from TraderBot.NavigationInTheGame.navigation_in_the_sell_my_items import navigation_in_the_sell_my_items
from MainClasses.Image.image import Image


class ParseInventory(Image):
    @staticmethod
    def go_to_inventory():
        navigation_in_the_sell_my_items.go_to_my_items()

    def taking_screenshot(self):
        print('2222')
        position = 1
        for i in range(9):
            self.take_screenshot(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\name{position}.png",
                                 (247, 338 + 77 * i, 370, 362 + 77 * i))
            self.take_screenshot(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\avail{position}.png",
                                 (555, 338 + 77 * i, 645, 360 + 77 * i))
            position += 1
        print(3333)

    def converting_images_to_strings(self):
        self.go_to_inventory()
        self.taking_screenshot()

        position = 1
        product_list = []

        for i in range(9):
            self.upscale_image(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\name{position}.png", 1.5)
            self.upscale_image(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\avail{position}.png", 1.5)

            self.delete_all_colors_except_one(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\name{position}.png",
                                              [60, 60, 60], [191, 181, 175])
            self.delete_all_colors_except_one(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\avail{position}.png",
                                              [65, 65, 65], [196, 186, 171])

            name = self.image_to_string(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\name{position}.png",
                                        False)
            avail = self.image_to_string(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\avail{position}.png",
                                         True)
            print(name)
            print(avail)

            if '\n' in name:
                name = name.replace('\n', '')

            if avail == 'oF' or avail == 'oT':
                avail = 97

            if '\n' in avail:
                avail = ''.join(x for x in avail if x.isdigit())

            print(avail)

            product_list.append([name, int(avail)])

            position += 1

        return product_list


parse_inventory = ParseInventory()


