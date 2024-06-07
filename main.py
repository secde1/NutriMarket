import os
import sys
import asyncio
import logging

from aiogram.types import FSInputFile
from dotenv import load_dotenv
from aiogram import Dispatcher, types, Bot, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.client.default import DefaultBotProperties
from aiogram.methods.send_photo import SendPhoto
from buttons.buttons import many, lan_btn, phone_btn, location_btn, buy_btn
from translations import get_translation

load_dotenv()

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

user_languages = {}
user_states = {}

STATE_WAITING_FOR_PHONE = "waiting_for_phone"
STATE_WAITING_FOR_LOCATION = "waiting_for_location"
STATE_MAIN_MENU = "main_menu"


@dp.message(CommandStart())
async def welcome(message: types.Message) -> None:
    user_id = message.from_user.id
    user_languages[user_id] = 'ru'
    user_states[user_id] = STATE_WAITING_FOR_PHONE
    await message.answer(get_translation('send_phone_prompt', user_languages[user_id]),
                         reply_markup=phone_btn(user_languages[user_id]))


@dp.message(Command(commands=['support']))
async def support(message: types.Message):
    user_id = message.from_user.id
    user_language = user_languages.get(user_id, 'ru')
    await message.answer(get_translation('support', user_language))


@dp.message(Command(commands=['buy']))
async def buy(message: types.Message):
    user_id = message.from_user.id
    user_language = user_languages.get(user_id, 'ru')

    photo_path = FSInputFile("media/photo_2024-06-07_16-00-56.jpg")
    order_markup = buy_btn(user_language)
    await bot.send_photo(
        chat_id=user_id,
        photo=photo_path,
        caption=get_translation('buy', user_language),
        reply_markup=order_markup
    )


@dp.message(lambda message: message.content_type == types.ContentType.CONTACT)
async def process_phone(message: types.Message):
    user_id = message.from_user.id
    contact = message.contact
    phone_number = contact.phone_number
    await message.answer(get_translation('phone_received', user_languages[user_id]).format(phone_number))

    user_states[user_id] = STATE_WAITING_FOR_LOCATION
    await message.answer(get_translation('send_location_prompt', user_languages[user_id]),
                         reply_markup=location_btn(user_languages[user_id]))


@dp.message(lambda message: message.content_type == types.ContentType.LOCATION)
async def process_location(message: types.Message):
    user_id = message.from_user.id
    location = message.location
    await message.answer(get_translation('location_received', user_languages[user_id]).format(
        location.latitude, location.longitude))

    user_states[user_id] = STATE_MAIN_MENU
    await message.answer(get_translation('choose_option', user_languages[user_id]),
                         reply_markup=many(user_languages[user_id]))


@dp.message(F.content_type == types.ContentType.TEXT)
async def text(message: types.Message) -> None:
    user_id = message.from_user.id
    if user_id not in user_languages:
        user_languages[user_id] = 'ru'

    if user_states.get(user_id) != STATE_MAIN_MENU:
        return

    text = message.text.lower()
    if text in ['язык(ru/uz)', 'til(ru/uz)']:
        await message.answer(get_translation('choose_language', user_languages[user_id]),
                             reply_markup=lan_btn(user_languages[user_id]))
    elif text in ['назад', 'ortga']:
        await message.answer(get_translation('back_to_menu', user_languages[user_id]),
                             reply_markup=many(user_languages[user_id]))

    elif text == 'русский 🇷🇺':
        user_languages[user_id] = 'ru'
        await message.answer(get_translation('language_set', 'ru'), reply_markup=many('ru'))
    elif text == 'узбекский 🇺🇿':
        user_languages[user_id] = 'uz'
        await message.answer(get_translation('language_set', 'uz'), reply_markup=many('uz'))


async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
