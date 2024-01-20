import pyautogui


class Keyboard:
    """Класс для работы с клавиатурой"""

    def __init__(self):
        self.TYPE_INTERVAL = 0.1

    def press_button(self, button):
        """Фуцнкия для нажатия клавиши\n
        button - клавиша
        """
        pyautogui.press(button)

    def esc(self):
        """Функция для нажатия клавиши esc"""
        pyautogui.press('esc')

    def type(self, text):
        """Функция для того чтобы напечатать текст"""
        pyautogui.write(text)
