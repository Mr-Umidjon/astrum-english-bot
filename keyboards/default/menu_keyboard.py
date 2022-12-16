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
