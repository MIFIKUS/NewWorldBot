from MainClasses.Image.image import Image
import time


class Check(Image):
    '''Класс в котоором проверяются различные значения внутри игры'''
    def check_balance(self):
        '''Проверить баланс'''
        time.sleep(1)
        path_to_balance_picture = "E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\balance.png"
        #self.take_screenshot(path_to_balance_picture, (1700, 20, 1820, 50))
        #self.delete_all_colors_except_one(path_to_balance_picture, [190, 180, 165], [255, 255, 255])
        balance = self.image_to_string(path_to_balance_picture, True)
        balance = balance.replace(',', '')

        return balance


check = Check()



