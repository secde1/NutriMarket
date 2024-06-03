from aiogram.types.web_app_info import WebAppInfo
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from translations import get_translation


def many(language):
    products = KeyboardButton(text=get_translation('products', language),
                              web_app=WebAppInfo(url='https://nutri-market.vercel.app/'))
    cart = KeyboardButton(text=get_translation('my_orders', language))
    settings = KeyboardButton(text=get_translation('language_settings', language))

    button = ReplyKeyboardMarkup(
        keyboard=[[products, cart, settings]],
        one_time_keyboard=True,
        resize_keyboard=True
    )
    return button


def lan_btn():
    russian = KeyboardButton(text='Русский 🇷🇺')
    uzbek = KeyboardButton(text='Узбекский 🇺🇿')
    back = KeyboardButton(text=get_translation('back', 'ru'))

    button = ReplyKeyboardMarkup(
        keyboard=[[russian, uzbek, back]],
        one_time_keyboard=True,
        resize_keyboard=True
    )
    return button


def phone_btn():
    send_nummer = KeyboardButton(text=get_translation('send_phone', 'ru'), request_contact=True)

    button = ReplyKeyboardMarkup(
        keyboard=[[send_nummer]],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return button


def location_btn():
    send_location = KeyboardButton(text=get_translation('send_location', 'ru'), request_location=True)
    button = ReplyKeyboardMarkup(
        keyboard=[[send_location]],
        resize_keyboard=True,
        one_time_keyboard=True

    )
    return button
