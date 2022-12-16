from aiogram import types

from keyboards.default.menu_keyboard import books_menu_keyboard, main_menu_keyboard, headway_menu_keyboard

from loader import dp


@dp.message_handler(text='📚 Books')
async def show_books(message: types.Message):
    await message.answer(text="📚 Books", reply_markup=books_menu_keyboard)


@dp.message_handler(text='📕 Headway')
async def show_headway_books(message: types.Message):
    await message.answer("📕 Headway", reply_markup=headway_menu_keyboard)


@dp.message_handler(text="🏠 Go back to menu")
async def back_menu(message: types.Message):
    await message.answer(text='🏠 Menu', reply_markup=main_menu_keyboard)


#

@dp.message_handler(text='🔙 Go back')
async def back(message: types.Message):
    await message.answer(text="📚 Books", reply_markup=books_menu_keyboard)
