from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.text import text
from filters import IsPrivate
from loader import dp
from utils.db_api.mongo import user_db
import time


@dp.message_handler(CommandStart(), IsPrivate())
async def bot_start(message: types.Message):
    user_db.update_one({'id': message.from_user.id}, {
        '$set': {'id': message.from_user.id,
                 'name': message.from_user.full_name,
                 'username': message.from_user.username,
                 'time': int(time.time())}}, upsert=True)

    await message.answer(text['start_text'], disable_web_page_preview=True)
