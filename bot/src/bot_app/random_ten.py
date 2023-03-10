from aiogram import types
from aiogram.dispatcher import FSMContext

from . app import dp, bot
from . data_fetcher import get_random
from . keyboards import inline_kb
from . states import GameStates


@dp.message_handler(commands='train_ten', state='*')
async def train_ten(message: types.Message, state: FSMContext):
    await GameStates.random_ten.set()
    res = await get_random()
    async with state.proxy() as data:
        data['step'] = 1
        data['answer'] = res.get('gender')
        data['word'] = res.get('word')
    await message.reply(f'{data["step"]} из 10. Слово {data["word"]}', reply_markup=inline_kb)


@dp.callback_query_handler(lambda c: c.data in ['женский', 'мужской', 'средний'], state=GameStates.random_ten)
async def button_click_call_back(callback_query: types.CallbackQuery, state: FSMContext):
    answer = callback_query.data
    async with state.proxy() as data:
        if answer == data.get('answer'):
            res = await get_random()
            data['step'] += 1
            data['answer'] = res.get('gender')
            data['word'] = res.get('word')
            if data['step'] > 10:
                await bot.send_message(callback_query.from_user.id, "Игра окончена!!!")
                await GameStates.start.set()
            else:
                await bot.send_message(callback_query.from_user.id, "Все верно\n" + f'{data["step"]} из 10. Слово {data["word"]}', reply_markup=inline_kb)
        else:
            await bot.send_message(callback_query.from_user.id, "Не отгадал\n", reply_markup=inline_kb)
