from aiogram.types.web_app_info import WebAppInfo
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def many():
    products = KeyboardButton(text='Продукты', web_app=WebAppInfo(url='https://buddyburger.vercel.app/'))
    cart = KeyboardButton(text='Мои заказы')
    settings = KeyboardButton(text='настройки')
    idea = KeyboardButton(text='Чат')

    button = ReplyKeyboardMarkup(
        keyboard=[[products, cart,
                   settings, idea]],
        one_time_keyboard=True,
        resize_keyboard=True
    )
    return button


def lan_btn():
    russian = KeyboardButton(text='Русский 🇷🇺')
    uzbek = KeyboardButton(text='Узбекский 🇺🇿')
    back = KeyboardButton(text='Назад')

    button = ReplyKeyboardMarkup(
        keyboard=[[russian, uzbek,
                   back]],
        one_time_keyboard=True,
        resize_keyboard=True
    )
    return button


def phone_btn():
    button = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Отправить мой номер", request_contact=True)]],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return button
