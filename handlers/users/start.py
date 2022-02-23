from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Command

from data.text import text
from filters import IsPrivate, IsGroup
from loader import dp
from utils.db_api.mongo import user_db, post_db
import time


@dp.message_handler(CommandStart(), IsPrivate())
async def bot_start(message: types.Message):
    args = message.get_args()

    if args:
        textback = text['list_text']
        count = 1
        link = []
        for i in post_db.find():
            textback += f'{count}) ' + i['link'] + '\n'
            link.append(i['link'])
            count += 1

        user_db.update_one({'id': message.from_user.id}, {'$set': {'links': link}}, upsert=True)
        await message.answer(textback)
        return

    user_db.update_one({'id': message.from_user.id}, {
        '$set': {'id': message.from_user.id,
                 'name': message.from_user.full_name,
                 'username': message.from_user.username,
                 'time': int(time.time())}}, upsert=True)

    await message.answer(text['start_text'], disable_web_page_preview=True)
