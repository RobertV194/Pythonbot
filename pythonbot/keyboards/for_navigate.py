from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/about')
        ],
        [
            KeyboardButton(text='/games')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='All commands'
)


game = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text='Add game')
            ],
            [
                KeyboardButton(text='Delete all')
            ],
            [
                KeyboardButton(text='View all')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Choose action'
)






