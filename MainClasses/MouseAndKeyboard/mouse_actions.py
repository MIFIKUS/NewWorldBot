import pyautogui

SPEED = 0.5

def move_and_click(x, y):
    """Функция чтобы навестись на координаты на экране и кликнуть на это точку"""
    move(x, y)
    click()

def move(x, y):
    """Функция чтобы переместить курсор на заданные координаты"""
    pyautogui.moveTo(x, y, SPEED)

def move_instantly(x, y):
    """Функция чтобы мгновенно переместить курсор на нужные координаты"""
    pyautogui.moveTo(x, y, 0)

def click():
    """Функция чтобы сделать клик мышкой"""
    pyautogui.click()

def drag(x, y):
    """Функция для того чтобы переместить мышку на нужные координаты с зажатой левой кнопкой"""
    pyautogui.mouseDown(button='left')
    move(x, y)
    pyautogui.mouseUp(button='left')

def scroll_down(amount):
    """Функция для того прокрутить колесико мышки вниз\n
    amount - колличество прокруток
    """
    amount *= 100
    pyautogui.scroll(-amount)

def scroll_up(amount):
    """Функция для того что прокрутить колесико мышки вверх
    amount - колличество прокруток
    """
    amount *= 100
    pyautogui.scroll(amount)