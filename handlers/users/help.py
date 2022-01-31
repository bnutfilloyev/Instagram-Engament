from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from data.text import text
from filters import IsPrivate
from loader import dp


@dp.message_handler(CommandHelp(), IsPrivate())
async def bot_help(message: types.Message):
    await message.answer(text['help_text'])
