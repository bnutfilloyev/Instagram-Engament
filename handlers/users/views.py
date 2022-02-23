from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton
import requests

import data
from data.config import URL, API_TOKEN
from data.text import views_button
from loader import dp


@dp.message_handler(commands=['views'])
async def views(msg: types.Message, state: FSMContext):
    keyboard = []

    for i in range(0, len(views_button), 2):
        keyboard.append([InlineKeyboardButton(text=views_button[i]['title'], callback_data=views_button[i]['callback']),
                         InlineKeyboardButton(text=views_button[i + 1]['title'], callback_data=views_button[i + 1]['callback'])])

    await msg.answer('Выберите проект', reply_markup=types.InlineKeyboardMarkup(inline_keyboard=keyboard))


@dp.callback_query_handler(lambda c: c.data in [i['callback'] for i in views_button])
async def views_callback(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['count'] = int(call.data.split(':')[1])*1000
        await call.message.answer(f"Выбрано {data['count']} проектов")
        await call.message.answer('Please send me VIDEO link')
        await state.set_state('views')


@dp.message_handler(content_types=['text'], state='views')
async def views_text(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        res = requests.post(URL.format(API_TOKEN, msg.text, data['count']))
        if res.status_code == 200:
            await msg.answer('ALL IS DONE!')
            await state.finish()
        else:
            await msg.answer('ERROR!')
            await state.finish()



