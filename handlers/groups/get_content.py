from aiogram import types
import re

from aiogram.types import InlineKeyboardMarkup

from data.config import group_likes
from data.text import text
from filters import IsGroup
from loader import dp
from aiogram.utils.deep_linking import get_start_link
from utils.check_like import get_owner, check_like
from utils.db_api.mongo import post_db

instagram_regex = r'Dx([1-9]|[1-4]\d|50) (?:(?:https?|ftp):\/\/)?(?:www\.)?(?:instagram\.com|instagr\.am)\/([A-Za-z0-9-_]+)\/'


@dp.message_handler(IsGroup())
async def get_link(message: types.Message):
    if re.search(instagram_regex, message.text):
        ### Wait text
        await message.reply(text['checking_list'].format(message.from_user.get_mention(message.from_user.full_name)))

        ### Get instagram link, shortcode and owner
        instagram_link = message.text.split(' ')[-1]
        shortcode = instagram_link.split('/')[4]
        owner_id = "@{}".format(await get_owner(shortcode))

        if not await check_like(shortcode):
            await message.delete()
            await message.answer(
                text['warning_text'].format(message.from_user.get_mention(message.from_user.full_name)))
            return

        temp = post_db.insert_one({'link': instagram_link})
        print(temp.inserted_id)
        ### Create Button with link
        deeplink = await get_start_link(group_likes[message.chat.id])
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [(types.InlineKeyboardButton(text['instagram_button'], url=instagram_link)),
             (types.InlineKeyboardButton(text['instagram_link_list'], url=deeplink))],
        ], row_width=2)

        ### Message delete
        await message.delete()

        ### Send message
        await message.answer(text['instagram_text'].format(message.from_user.get_mention(message.from_user.full_name),
                                                           message.text.split(" ")[0],
                                                           owner_id,
                                                           instagram_link), reply_markup=keyboard)
        return

    await message.delete()
    await message.answer(text['warning_text'].format(message.from_user.get_mention(message.from_user.full_name)))
