from aiogram.types import ReplyKeyboardRemove, Message
from aiogram.dispatcher.filters.builtin import Command, Text

from keyboards.default.menu_keyboard import menu
from keyboards.default.headway_student_book_keyboard import menu_headway_student_book
from keyboards.default.headway_workbook_keyboard import menu_headway_workbook
from keyboards.default.navigate_student_book_keyboard import menu_navigate_student_book
from keyboards.default.navigate_workbook_keyboard import menu_navigate_workbook

from loader import dp


@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
    await message.answer('Menu', reply_markup=menu)


@dp.message_handler(text='📕 Headway Student\'s book Audios')
async def show_menu_headway_student(message: Message):
    await message.answer('📕 Headway Student\'s book Audios', reply_markup=menu_headway_student_book)


@dp.message_handler(text='📘 Headway Workbook Audios')
async def show_menu_headway_work(message: Message):
    await message.answer('📘 Headway Workbook Audios', reply_markup=menu_headway_workbook)


@dp.message_handler(text='📙 Navigate Student\'s book Audio')
async def show_menu_navigate_student(message: Message):
    await message.answer('📙 Navigate Student\'s book Audio', reply_markup=menu_navigate_student_book)


@dp.message_handler(text='📗 Navigate Workbook Audios')
async def show_menu_navigate_work(message: Message):
    await message.answer('📗 Navigate Workbook Audios', reply_markup=menu_navigate_workbook)


@dp.message_handler(text='Go Back')
async def go_back(message: Message):
    await message.answer("Menu", reply_markup=menu)
