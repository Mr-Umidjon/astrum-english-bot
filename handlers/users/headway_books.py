from aiogram import types

from loader import dp

from keyboards.default.menu_keyboard import unit_keyboard, books_menu_keyboard


@dp.message_handler(text='📕 Student Beginner')
async def beginner_units(message: types.Message):
    await message.answer(text='📕 Student Beginner', reply_markup=unit_keyboard)


@dp.message_handler(text='📘 Student Elementary')
async def elementary_units(message: types.Message):
    await message.answer(text='📘 Student Elementary', reply_markup=unit_keyboard)


@dp.message_handler(text='📙 Student Pre-Intermediate')
async def pre_intermediate_units(message: types.Message):
    await message.answer(text='📙 Student Pre-Intermediate', reply_markup=unit_keyboard)


@dp.message_handler(text='📗 Student Intermediate')
async def intermediate_units(message: types.Message):
    await message.answer(text='📗 Student Intermediate', reply_markup=unit_keyboard)


@dp.message_handler(text='📓 Student Upper-Intermediate')
async def upper_intermediate_units(message: types.Message):
    await message.answer(text='📓 Student Upper-Intermediate', reply_markup=unit_keyboard)


@dp.message_handler(text='📔 Student Advanced')
async def advanced_units(message: types.Message):
    await message.answer(text='📔 Student Advanced', reply_markup=unit_keyboard)


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


@dp.message_handler(text='🔙 Go back')
async def back(message: types.Message):
    await message.answer(text="📚 Books", reply_markup=books_menu_keyboard)
