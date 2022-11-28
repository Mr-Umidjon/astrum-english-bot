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

levels = ['menu_hsbb_units', 'menu_hsbe_units', 'menu_hsbp_units', 'menu_hsbi_units', 'menu_hsbu_units',
          'menu_hsba_units']

menu_headway_student_book_levels = dict()
for level in levels:
    menu_level = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    for i in range(1, 13, 2):
        menu_level.add(KeyboardButton(text=f'unit {i}'), KeyboardButton(text=f'unit {i + 1}'))
    menu_level.add(KeyboardButton(text='Go Back'))
    menu_headway_student_book_levels[level] = menu_level
