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
            KeyboardButton(text="📕 Student Beginner"),
            KeyboardButton(text='📘 Student Elementary'),
        ],
        [
            KeyboardButton(text="📙 Student Pre-Intermediate"),
            KeyboardButton(text='📗 Student Intermediate'),
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
            KeyboardButton(text="🏠 Go back to menu")
        ],
    ],
    resize_keyboard=True
)

unit_keyboard = ReplyKeyboardMarkup(row_width=1)

for i in range(1, 13):
    unit_keyboard.insert(KeyboardButton(text=f"Unit {i}"))
unit_keyboard.insert(KeyboardButton(text='🔙 Go back'))
unit_keyboard.insert(KeyboardButton(text="🏠 Go back to menu"))
