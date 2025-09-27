from aiogram import Router
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove

router = Router()

def menu():
    kb_list=[
        [KeyboardButton(text="Объявления")],
    ]

    keyboard = ReplyKeyboardMarkup(keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True)
    return keyboard


def under_the_menu():
    kb_list = [
        [KeyboardButton(text="Создать Объявление"),
         KeyboardButton(text="Мои Объявления")],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return keyboard

def my_advertisement():
    kb_list = [
        [KeyboardButton(text="Отправить"),
         KeyboardButton(text="Не отправлять")],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return keyboard



def save_or_clear():
    kb_list = [
        [KeyboardButton(text="Сохранить"),
         KeyboardButton(text="Не сохранять")],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True

    )
    return keyboard