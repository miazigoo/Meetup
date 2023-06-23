from telegram import InlineKeyboardButton

from bot_meetup.models import Event

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

get_keyboard_all_event = []
for event in Event.objects.all()[:10]:
    get_keyboard_all_event.append(
        [
            InlineKeyboardButton(f"{event.title}", callback_data=f'allevent_{event.pk}'),
        ]
    )
get_keyboard_all_event.append(
    [
        InlineKeyboardButton("Назад", callback_data="to_start"),
    ]
)

get_keyboard_add_speaker = [
    [
        InlineKeyboardButton("Стать спикером", callback_data='add_speaker'),
    ],
    [
        InlineKeyboardButton("Назад", callback_data="to_start"),
    ]
]
