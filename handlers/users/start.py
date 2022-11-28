from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Command

from keyboards.default.menu_keyboard import menu

from loader import dp


@dp.message_handler(CommandStart())
@dp.message_handler(Command('menu'))
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
    await message.answer("Menu", reply_markup=menu)
