from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu_navigate_student_book = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📕 Navigate Student's book Beginner"),
            KeyboardButton(text='📘 Navigate Student\'s book Elementary'),
        ],
        [
            KeyboardButton(text="📙 Navigate Student's book Pre-Intermediate"),
            KeyboardButton(text='📗 Navigate Student\'s book Intermediate'),
        ],
        [
            KeyboardButton(text="📓 Navigate Student's book Upper-Intermediate"),
            KeyboardButton(text='📔 Navigate Student\'s book Advanced'),
        ],
        [
            KeyboardButton(text='Go Back')
        ]
    ],
    resize_keyboard=True
)
