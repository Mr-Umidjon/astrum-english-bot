from aiogram.types import ReplyKeyboardRemove, Message
from aiogram.dispatcher.filters.builtin import Command, Text

from keyboards.default.menu_keyboard import menu
from keyboards.default.headway_student_book_keyboard import menu_headway_student_book, menu_headway_student_book_levels
from keyboards.default.headway_workbook_keyboard import menu_headway_workbook, menu_headway_work_book_levels
from keyboards.default.navigate_student_book_keyboard import menu_navigate_student_book
from keyboards.default.navigate_workbook_keyboard import menu_navigate_workbook

from loader import dp


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


# Headway student book
@dp.message_handler(text='📕 Headway Student\'s book Beginner')
async def show_headway_student_beginner_units(message: Message):
    await message.answer('Units', reply_markup=menu_headway_student_book_levels['menu_hsbb_units'])


@dp.message_handler(text='📘 Headway Student\'s book Elementary')
async def show_headway_student_elementary_units(message: Message):
    await message.answer('Units', reply_markup=menu_headway_student_book_levels['menu_hsbe_units'])


@dp.message_handler(text="📙 Headway Student's book Pre-Intermediate")
async def show_headway_student_pre_units(message: Message):
    await message.answer('Units', reply_markup=menu_headway_student_book_levels['menu_hsbp_units'])


@dp.message_handler(text='📗 Headway Student\'s book Intermediate')
async def show_headway_student_inter_units(message: Message):
    await message.answer('Units', reply_markup=menu_headway_student_book_levels['menu_hsbi_units'])


@dp.message_handler(text="📓 Headway Student's book Upper-Intermediate")
async def show_headway_student_upper_units(message: Message):
    await message.answer('Units', reply_markup=menu_headway_student_book_levels['menu_hsbu_units'])


@dp.message_handler(text='📔 Headway Student\'s book Advanced')
async def show_headway_student_advanced_units(message: Message):
    await message.answer('Units', reply_markup=menu_headway_student_book_levels['menu_hsba_units'])


# Headway work book
@dp.message_handler(text="📕 Headway Workbook Beginner")
async def show_headway_work_beginner_units(message: Message):
    await message.answer('Units', reply_markup=menu_headway_student_book_levels['menu_hwbb_units'])


@dp.message_handler(text='📘 Headway Workbook Elementary')
async def show_headway_work_elementary_units(message: Message):
    await message.answer('Units', reply_markup=menu_headway_student_book_levels['menu_hwbe_units'])


@dp.message_handler(text="📙 Headway Workbook Pre-Intermediate")
async def show_headway_work_pre_units(message: Message):
    await message.answer('Units', reply_markup=menu_headway_student_book_levels['menu_hwbp_units'])


@dp.message_handler(text='📗 Headway Workbook Intermediate')
async def show_headway_work_inter_units(message: Message):
    await message.answer('Units', reply_markup=menu_headway_student_book_levels['menu_hwbi_units'])


@dp.message_handler(text="📓 Headway Workbook Upper-Intermediate")
async def show_headway_work_upper_units(message: Message):
    await message.answer('Units', reply_markup=menu_headway_student_book_levels['menu_hwbu_units'])


@dp.message_handler(text='📔 Headway Workbook Advanced')
async def show_headway_work_advanced_units(message: Message):
    await message.answer('Units', reply_markup=menu_headway_student_book_levels['menu_hwba_units'])
