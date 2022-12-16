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
            KeyboardButton(text='📕 Headway'),
        ]
        ,
        [
            KeyboardButton("🏠 Go back to menu")
        ]
    ],
    resize_keyboard=True
)

headway_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📕Student Beginner"),
            KeyboardButton(text='📘Student Elementary'),
        ],
        [
            KeyboardButton(text="📙Student Pre-Intermediate"),
            KeyboardButton(text='📗Student Intermediate'),
        ],
        [
            KeyboardButton(text="📓 Student Upper-Intermediate"),
            KeyboardButton(text='📔 Student Advanced'),
        ],
        [
            KeyboardButton(text="📕 Work Beginner"),
            KeyboardButton(text='📘 Work Elementary'),
        ],
        [
            KeyboardButton(text="📙 Work Pre-Intermediate"),
            KeyboardButton(text='📗 Work Intermediate'),
        ],
        [
            KeyboardButton(text="📓 Work Upper-Intermediate"),
            KeyboardButton(text='📔 Work Advanced'),
        ],
        [
            KeyboardButton(text='🔙 Go back')
        ],
        [
            KeyboardButton("🏠 Go back to menu")
        ],
    ],
    resize_keyboard=True
)
