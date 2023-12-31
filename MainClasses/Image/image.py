from PIL import Image as pil
import PIL.ImageGrab
import numpy as np
import cv2
import pytesseract

class Image:
    """Класс для работы с изображениями"""
    def matching(self, main_image_name, template_image_name, need_for_taking_screenshot=False, threshold=0.8,
                 func=None, area_of_screenshot=None):
        """Функция для сравнения 2ух изображений\n
        main_image_name - название основного изображения\n
        template_image_name - названия шаблона для сравнения\n
        need_for_taking_screenshot - нужно ли делать скриншот\n
        threshold - минимальный уровень совпадения 2ух изображений\n
        func - нужно ли возвращать координаты\n
        area_of_screenshot - область в которой нужно сделать скриншот. (указывать как тапл). Если оставить None, то будет сделан скриншот всего экрана
        """
        if need_for_taking_screenshot:
            if area_of_screenshot:
                PIL.ImageGrab.grab(bbox=area_of_screenshot).save(main_image_name)
            else:
                PIL.ImageGrab.grab().save(main_image_name)

        img_rgb = cv2.imread(main_image_name)
        template = cv2.imread(template_image_name)

        res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)

        if func is None:
            for pt in zip(*loc[::-1]):
                print("Найдено совпадение")
                return True
            return False

        for pt in zip(*loc[::-1]):
            return pt
        return False

    def take_screenshot(self, image_name, area_of_screenshot=None):
        """Функция для создания скриншота\n
        image_name - название изображения скриншота\n
        area_of_screenshot - область скриншота(указывать как тапл)
        """
        if area_of_screenshot:
            PIL.ImageGrab.grab(bbox=area_of_screenshot).save(image_name)
        else:
            PIL.ImageGrab.grab().save(image_name)

    def image_to_string(self, image_name, is_digits):
        """Функция для перевода картники в строку\n
        image_name - название изображения с которого нужно получить текст\n
        is_digits - True если с картинки нужно получить только числа, False если нужно получить еще и текст
        """
        if is_digits is True:
            text = pytesseract.image_to_string(image_name, config='--psm 11 -c tessedit_char_whitelist=0123456789/')
            return text
        text = pytesseract.image_to_string(image_name, lang='rus', config='--psm 3')
        return text

    def image_to_string_custom_confing(self, image_name, config):
        """Фуцнкия для получения текста с картинки с использованием своего запроса к Tesseract"""
        text = pytesseract.image_to_string(image_name, config=config)
        return text

    def get_main_color(self, file):
        """Функция для получения цвета который чаще всего представлен на картинке\n
        file - название изображения на котором нужно найти цвет
        """
        img = pil.open(file)
        colors = img.getcolors(256)  # put a higher value if there are many colors in your image
        max_occurence, most_present = 0, 0
        try:
            for c in colors:
                if c[0] > max_occurence:
                    (max_occurence, most_present) = c
            return most_present
        except TypeError:
            raise Exception("Too many colors in the image")