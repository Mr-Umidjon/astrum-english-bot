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

levels = ['menu_hwbb_units', 'menu_hwbe_units', 'menu_hwbp_units', 'menu_hwbi_units', 'menu_hwbu_units',
          'menu_hwba_units']

menu_headway_work_book_levels = dict()
for level in levels:
    menu_level = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    for i in range(1, 13, 2):
        menu_level.add(KeyboardButton(text=f'unit {i}'), KeyboardButton(text=f'unit {i + 1}'))
    menu_level.add(KeyboardButton(text='Go Back'))
    menu_headway_work_book_levels[level] = menu_level
