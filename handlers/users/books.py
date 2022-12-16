from aiogram import types

from keyboards.default.menu_keyboard import books_menu_keyboard, main_menu_keyboard, unit_keyboard

from loader import dp


@dp.message_handler(text='📚 Books')
async def show_books(message: types.Message):
    await message.answer(text="📚 Books", reply_markup=books_menu_keyboard)


@dp.message_handler(text="🏠 Go back to menu")
async def back_menu(message: types.Message):
    await message.answer(text='🏠 Menu', reply_markup=main_menu_keyboard)



