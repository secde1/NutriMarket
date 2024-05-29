import os
import sys
import asyncio
import logging

from dotenv import load_dotenv
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram import Dispatcher, types, Bot
from aiogram.client.default import DefaultBotProperties

load_dotenv()

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def welcome(message: types.Message):
    # button = types.KeyboardButton(text='Открыть веб страницу',
    #                               web_app=WebAppInfo(url='https://buddyburger.vercel.app/'))
    # markup = types.ReplyKeyboardMarkup(keyboard=[[button]], resize_keyboard=True)
    await message.answer(f"Привет {message.from_user.first_name}! Давай зарегистрируемся. Как тебя зовут?", )
    # reply_markup=markup)


# @dp.message(state=Form.name)
# async def name(message: types.Message, state: FSMContext):
#     async with state.set_state(Form.name)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
