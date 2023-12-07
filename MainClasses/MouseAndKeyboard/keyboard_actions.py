import pyautogui

TYPE_INTERVAL = 0.1

def press_button(button):
    """Фуцнкия для нажатия клавиши\n
    button - клавиша
    """
    pyautogui.press(button)

def esc():
    """Функция для нажатия клавиши esc"""
    pyautogui.press('esc')

def type(text):
    """Функция для того чтобы напечатать текст"""
    pyautogui.write(text, self.TYPE_INTERVAL)
