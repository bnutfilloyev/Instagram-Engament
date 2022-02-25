from aiogram import types

from data.text import text
from loader import dp


@dp.message_handler(commands=['rules'])
async def rules(message: types.Message):
    await message.answer(text=text['rules'])