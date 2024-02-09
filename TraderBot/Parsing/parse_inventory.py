from TraderBot.NavigationInTheGame.navigation_in_the_sell_my_items import navigation_in_the_sell_my_items
from MainClasses.Image.image import Image


class ParseInventory(Image):
    def __init__(self):
        self.position = 1
        self.name = f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\name{self.position}.png"
        self.avail_name = f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\avail{self.position}.png"

    @staticmethod
    def go_to_inventory():
        navigation_in_the_sell_my_items.go_to_my_items()

    def taking_screenshot(self):
        self.position = 1
        for i in range(9):
            self.take_screenshot(self.name, (660, 310 + 77 * self.position, 600, 387 + 77 * self.position))
            self.take_screenshot(self.avail_name, (660, 310 + 77 * self.position, 600, 387 + 77 * self.position)) #этих бебриков изменить корды
            self.position += 1

    def converting_images_to_strings(self):
        self.go_to_inventory()
        self.taking_screenshot()

        self.position = 1
        product_list = []
        for i in range(9):
            self.delete_all_colors_except_one(self.name, [51, 41, 24], [191, 181, 165])
            self.delete_all_colors_except_one(self.avail_name, [51, 41, 24], [191, 181, 165])
            self.upscale_image(self.name, 2)
            self.upscale_image(self.avail_name, 2)

            name = self.image_to_string(self.name, False)
            avail = self.image_to_string(self.avail_name, False)
            product_list.append([name, avail])

            self.position += 1

        return product_list


parse_inventory = ParseInventory()



