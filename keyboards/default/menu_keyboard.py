from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📚 Books'),
            KeyboardButton(text='📖 Instruction'),
        ],
    ],
    resize_keyboard=True
)

books_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📕 Headway Student\'s books'),
            KeyboardButton(text='📘 Headway Work books'),
        ]
        ,
        [
            KeyboardButton("🏠 Go back to menu")
        ]
    ],
    resize_keyboard=True
)

levels_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📕 Beginner"),
            KeyboardButton(text='📘 Elementary'),
        ],
        [
            KeyboardButton(text="📙 Pre-Intermediate"),
            KeyboardButton(text='📗 Intermediate'),
        ],
        [
            KeyboardButton(text="📓 Upper-Intermediate"),
            KeyboardButton(text='📔 Advanced'),
        ],
        [
            KeyboardButton(text='Go Back')
        ]
    ],
    resize_keyboard=True
)
