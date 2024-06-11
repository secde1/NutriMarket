from aiogram.types.web_app_info import WebAppInfo
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
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


def lan_btn(language):
    russian = KeyboardButton(text='Русский 🇷🇺')
    uzbek = KeyboardButton(text='Узбекский 🇺🇿')
    back = KeyboardButton(text=get_translation('back', language))

    button = ReplyKeyboardMarkup(
        keyboard=[[russian, uzbek, back]],
        one_time_keyboard=True,
        resize_keyboard=True
    )
    return button


def phone_btn(language):
    send_nummer = KeyboardButton(text=get_translation('send_phone', language), request_contact=True)

    button = ReplyKeyboardMarkup(
        keyboard=[[send_nummer]],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return button


def location_btn(language):
    send_location = KeyboardButton(text=get_translation('send_location', language), request_location=True)
    button = ReplyKeyboardMarkup(
        keyboard=[[send_location]],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return button


def buy_btn(language):
    order_text = get_translation('buy', language)
    order_button = InlineKeyboardButton(
        text=order_text,
        web_app=WebAppInfo(url='https://nutri-market.vercel.app/')
    )
    keyboard = [[order_button]]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup


def confirmation_btn(language):
    yes = KeyboardButton(text=get_translation('yes', language))
    no = KeyboardButton(text=get_translation('no', language))
    button = ReplyKeyboardMarkup(
        keyboard=[[yes, no]],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return button
