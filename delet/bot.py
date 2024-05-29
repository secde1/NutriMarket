import os
import sys
import asyncio
import logging

from dotenv import load_dotenv
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram import Dispatcher, types, Bot
from aiogram.client.default import DefaultBotProperties

from buttons.buttons import lan_btn

load_dotenv()

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Configure logging
logging.basicConfig(level=logging.INFO, stream=sys.stdout)


@dp.message(CommandStart())
async def welcome(message: types.Message) -> None:
    # await state.set_state(Form.language)
    await message.answer('Asssalomu alekum! Keling, avvalo xizmat tilini tanlaylik!\n\n\n'
                         'Здравствуйте! Давайте для начала выберем язык обслуживания!',
                         reply_markup=lan_btn())


# @dp.message(StateFilter(Form.language))
# async def process_language(message: types.Message, state: FSMContext):
#     await state.update_data(language=message.text)
#
#     # Retrieve the user data
#     user_data = await state.get_data()
#
#     # Determine the response based on the selected language
#     if user_data.get('language') == 'Русский 🇷🇺':
#         await message.reply("Добро пожаловать в NutriMarket!")
#     else:
#         await message.reply("NutriMarket'ga xush kelibsiz!")
#
#     await message.reply(
#         "Отправьте свой номер телефона, чтобы отправить номер, нажмите на кнопку 'Отправить мой номер' или отправьте номер в формате: +998 ** *** ****",
#         reply_markup=phone_btn())
#
#
# @dp.message(StateFilter(Form.phone), F.content_type == types.ContentType.CONTACT)
# async def process_phone(message: types.Message, state: FSMContext):
#     contact = message.contact
#     phone_number = contact.phone_number
#     data = await state.get_data()
#     language = data.get('language')
#     await message.answer(f"Спасибо за предоставленный номер телефона ({phone_number}). "
#                          f"Выбранный вами язык: {language}.")
#

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
