import time

from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from aiogram.utils.deep_linking import decode_payload

from data.text import text
from filters import IsGroup
from loader import dp
from utils.db_api.mongo import user_db


@dp.message_handler(CommandStart(), IsGroup())
async def bot_start(message: types.Message):
    user_db.update_one({'id': message.from_user.id}, {
        '$set': {'id': message.from_user.id,
                 'name': message.from_user.full_name,
                 'username': message.from_user.username,
                 'time': int(time.time())}}, upsert=True)

    await message.delete()
    await message.bot.send_message(message.from_user.id, text['start_text'], disable_web_page_preview=True)
