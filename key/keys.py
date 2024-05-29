from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = KeyboardButton('send image')
    button_2 = KeyboardButton('image 2')
    button_3 = KeyboardButton('image 3')
    button_4 = KeyboardButton('image 4')
    button_5 = KeyboardButton('move to the next keyboard')
    keyboard.add(button_1, button_2, button_3, button_4, button_5)
    return keyboard

def get_keyboard_2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True)
    button_6 = KeyboardButton('send another image')
    button_7 = KeyboardButton('go back to first keyboard')
    keyboard_2.add(button_6, button_7)
    return keyboard_2
