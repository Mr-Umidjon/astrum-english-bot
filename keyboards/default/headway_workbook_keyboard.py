from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu_headway_workbook = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📕 Headway Workbook Beginner"),
            KeyboardButton(text='📘 Headway Workbook Elementary'),
        ],
        [
            KeyboardButton(text="📙 Headway Workbook Pre-Intermediate"),
            KeyboardButton(text='📗 Headway Workbook Intermediate'),
        ],
        [
            KeyboardButton(text="📓 Headway Workbook Upper-Intermediate"),
            KeyboardButton(text='📔 Headway Workbook Advanced'),
        ],
        [
            KeyboardButton(text='Go Back')
        ]
    ],
    resize_keyboard=True
)
