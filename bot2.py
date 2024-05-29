import os
import sys
import asyncio
import logging

from dotenv import load_dotenv
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram import Dispatcher, types, Bot, F
from aiogram.client.default import DefaultBotProperties
from buttons.buttons import many, lan_btn

load_dotenv()

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Configure logging
logging.basicConfig(level=logging.INFO, stream=sys.stdout)


@dp.message(CommandStart())
async def welcome(message: types.Message) -> None:
    await message.answer('Выберите одно из следующих!\n\n\n',
                         reply_markup=many())


@dp.message(F.content_type == types.ContentType.TEXT)
async def text(message: types.Message) -> None:
    if message.text.lower() == 'настройки':
        await message.answer('выберем язык обслуживания!', reply_markup=lan_btn())
    elif message.text.lower() == 'назад':
        await message.answer('Вы вернулись в главное меню', reply_markup=many())


@dp.message(F.content_type == types.ContentType.TEXT)
async def text(message: types.Message) -> None:
    if message.text.lower() == 'чат':
        await message.answer()


async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
