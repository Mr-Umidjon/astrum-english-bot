from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📕 Headway Student's book Audios"),
            KeyboardButton(text='📘 Headway Workbook Audios'),
        ],
        [
            KeyboardButton(text="📙 Navigate Student's book Audios"),
            KeyboardButton(text='📗 Navigate Workbook Audios'),
        ],
    ],
    resize_keyboard=True
)
