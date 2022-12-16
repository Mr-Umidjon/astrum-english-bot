from aiogram import types

from loader import dp

from keyboards.default.menu_keyboard import unit_keyboard, headway_menu_keyboard


@dp.message_handler(text='📕 Work Beginner')
async def beginner_units(message: types.Message):
    await message.answer(text='📕 Work Beginner', reply_markup=unit_keyboard)


@dp.message_handler(text='📘 Work Elementary')
async def elementary_units(message: types.Message):
    await message.answer(text='📘 Work Elementary', reply_markup=unit_keyboard)


@dp.message_handler(text='📙 Work Pre-Intermediate')
async def pre_intermediate_units(message: types.Message):
    await message.answer(text='📙 Work Pre-Intermediate', reply_markup=unit_keyboard)


@dp.message_handler(text='📗 Work Intermediate')
async def intermediate_units(message: types.Message):
    await message.answer(text='📗 Work Intermediate', reply_markup=unit_keyboard)


@dp.message_handler(text='📓 Work Upper-Intermediate')
async def upper_intermediate_units(message: types.Message):
    await message.answer(text='📓 Work Upper-Intermediate', reply_markup=unit_keyboard)


@dp.message_handler(text='📔 Work Advanced')
async def advanced_units(message: types.Message):
    await message.answer(text='📔 Work Advanced', reply_markup=unit_keyboard)


@dp.message_handler(text='◀️ Go back')
async def back(message: types.Message):
    await message.answer(text='📕 Headway', reply_markup=headway_menu_keyboard)
