from telegram import InlineKeyboardButton

get_keyboard_back = [
    [
        InlineKeyboardButton("Назад", callback_data="to_start"),
    ]
]

get_keyboard_start = [
    [
        InlineKeyboardButton("Посмотреть программу мероприятия", callback_data='view_event'),
    ],
    [
        InlineKeyboardButton("Посмотреть ближайшие мероприятия", callback_data='view_upcoming_events'),
    ],
    [
        InlineKeyboardButton("Задать вопрос спикеру", callback_data="ask_question"),
        InlineKeyboardButton("Что умеет бот", callback_data="FAQ"),
    ]
]
