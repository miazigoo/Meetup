import re

from telegram import Update, InlineKeyboardMarkup, ParseMode

from bot_meetup.keyboards.keyboards import get_keyboard_back, get_keyboard_all_event, get_keyboard_add_speaker
from bot_meetup.models import Event

EVENT_TEXT = """
Программа на 20.06: 
*Отлоси клоси мафлоси*
----------------------------------------------------------------------------
Будем говорить чепуху целый час.
Ждем всех! Может услышим что-то забавное. 
ДАЕШЬ ЧЕПУХРЕНЬ!!!
"""


def view_event(update: Update, _):
    query = update.callback_query
    query.answer()
    reply_markup = InlineKeyboardMarkup(get_keyboard_back)
    if query.data == 'view_event':
        query.edit_message_text(
            text=EVENT_TEXT, reply_markup=reply_markup,
            parse_mode=ParseMode.MARKDOWN
        )
    # elif query.data == 'view_upcoming_events':
    #     # ---------------------------------------
    #     # ближайшие мероприятия
    #     # ---------------------------------------
    #     reply_markup = InlineKeyboardMarkup(get_keyboard_all_event)
    #     query.edit_message_text(
    #         text='# ---------------------------------------\n'
    #              '# ближайшие мероприятия\n'
    #              '# ---------------------------------------',
    #         reply_markup=reply_markup,
    #         parse_mode=ParseMode.MARKDOWN
    #     )
    else:
        query.edit_message_text(
            text=query.data, reply_markup=reply_markup
        )
    return 'SHOW_INFO'


def view_events(update: Update, _):
    query = update.callback_query
    query.answer()
    reply_markup = InlineKeyboardMarkup(get_keyboard_all_event)
    if query.data == 'view_upcoming_events':
        # ---------------------------------------
        # ближайшие мероприятия
        # ---------------------------------------
        reply_markup = InlineKeyboardMarkup(get_keyboard_all_event)
        query.edit_message_text(
            text='# ---------------------------------------\n'
                 '# ближайшие мероприятия\n'
                 '# ---------------------------------------',
            reply_markup=reply_markup,
            parse_mode=ParseMode.MARKDOWN
        )
    else:
        query.edit_message_text(
            text=query.data, reply_markup=reply_markup
        )
    return 'VIEW_EVENT'


def event(update: Update, _):
    query = update.callback_query
    query.answer()
    reply_markup = InlineKeyboardMarkup(get_keyboard_add_speaker)
    if re.match("^allevent_", query.data):
        pk = int(query.data.split('_')[1])
        print(pk)
        event = Event.objects.get_or_none(pk=pk)
        if event:
            text = f'{event.title}\n{event.text}\n{event.speaker}\n{event.topic}'
        else:
            text = 'Сейчас нет доступных мероприятий'
        query.edit_message_text(
            text=text,
            reply_markup=reply_markup,
            parse_mode=ParseMode.MARKDOWN
        )
    else:
        query.edit_message_text(
            text=query.data, reply_markup=reply_markup
        )
    return 'VIEW_EVENT'
