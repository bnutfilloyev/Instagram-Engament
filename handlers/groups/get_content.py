from aiogram import types
import re

from filters import IsGroup
from loader import dp

instagram_regex = r'Dx([1-9]|[1-4]\d|50) (?:(?:https?|ftp):\/\/)?(?:www\.)?(?:instagram\.com|instagr\.am)\/([A-Za-z0-9-_]+)\/'

@dp.message_handler(IsGroup())
async def get_link(message: types.Message):
    if re.search(instagram_regex, message.text):
        instagram_link = message.text.split(' ')[-1]

        await message.answer("Получаю информацию о пользователе...")
    else:
        await message.answer("Не понял вашего запроса")