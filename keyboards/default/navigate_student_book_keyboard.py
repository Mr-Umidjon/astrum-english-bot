from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu_headway_student_book = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📕 Headway Student's book Beginner"),
            KeyboardButton(text='📘 Headway Student\'s book Elementary'),
        ],
        [
            KeyboardButton(text="📙 Headway Student's book Pre-Intermediate"),
            KeyboardButton(text='📗 Headway Student\'s book Intermediate'),
        ],
        [
            KeyboardButton(text="📓 Headway Student's book Upper-Intermediate"),
            KeyboardButton(text='📔 Headway Student\'s book Advanced'),
        ],
        [
            KeyboardButton(text='Go Back')
        ]
    ],
    resize_keyboard=True
)
