from aiogram import types

from loader import dp

from keyboards.default.menu_keyboard import unit_keyboard, headway_menu_keyboard


@dp.message_handler(text='📗 Work Intermediate')
async def intermediate_units(message: types.Message):
    await message.answer(text='📗 Work Intermediate', reply_markup=unit_keyboard)


@dp.message_handler(text='◀️ Go back')
async def back(message: types.Message):
    await message.answer(text='📕 Headway', reply_markup=headway_menu_keyboard)
