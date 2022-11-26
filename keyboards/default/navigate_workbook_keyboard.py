from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu_navigate_workbook = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📕 Navigate Workbook Beginner"),
            KeyboardButton(text='📘 Navigate Workbook Elementary'),
        ],
        [
            KeyboardButton(text="📙 Navigate Workbook Pre-Intermediate"),
            KeyboardButton(text='📗 Navigate Workbook Intermediate'),
        ],
        [
            KeyboardButton(text="📓 Navigate Workbook Upper-Intermediate"),
            KeyboardButton(text='📔 Navigate Workbook Advanced'),
        ],
        [
            KeyboardButton(text='Go Back')
        ]
    ],
    resize_keyboard=True
)
