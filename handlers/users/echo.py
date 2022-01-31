from aiogram import types
from aiogram.dispatcher import FSMContext

from data.text import text
from filters import IsPrivate
from loader import dp


@dp.message_handler(IsPrivate())
async def bot_echo(message: types.Message):
    await message.answer(text['start_text'])
