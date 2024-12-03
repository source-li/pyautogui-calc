import os
import pyautogui
import time


def open_calculator():
    '''
    Открываем калькулятор, если работаем на OS Windows
    '''
    if os.name == 'nt':  # Windows
        os.system("start calc")
    else:
        print("Программа работает только на OS Windows")
    time.sleep(2)


def click_button(image):
    '''
    Функция для выполнения кликов по кнопкам
    '''
    button_location = pyautogui.locateOnScreen(image, confidence=0.9)
    if button_location:
        pyautogui.click(pyautogui.center(button_location))
    else:
        print(f"Кнопка '{image}' не найдена на экране.")
    

def main():
    '''
    Основная логика программы
    '''
    expression = input("Введите выражение: ")
    open_calculator()
    
    for char in expression:
        if char == "*":
            char = "X"
        elif char == "/":
            char = "D"
        click_button(f"data/{char}.png")

    click_button(f"data/=.png")

if __name__ == "__main__":
    main()
