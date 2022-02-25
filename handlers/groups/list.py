from aiogram import types

from data.text import text
from filters import IsGroup
from loader import dp
from utils.db_api.mongo import post_db, user_db


@dp.message_handler(IsGroup(), commands=['list'])
async def list_groups(message: types.Message):
    await message.delete()
    textback = text['list_text']
    count = 1
    link = []
    for i in post_db.find():
        textback += f'{count}) ' + i['link'] + '\n'
        link.append(i['link'])
        count += 1

    user_db.update_one({'id': message.from_user.id}, {'$set': {'links': link}}, upsert=True)
    await message.bot.send_message(message.from_user.id, textback)
