from telegram import Update, InlineKeyboardMarkup, ParseMode

from bot_meetup.keyboards.keyboards import get_keyboard_back

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
    elif query.data == 'view_upcoming_events':
        # ---------------------------------------
        # ближайшие мероприятия
        # ---------------------------------------
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
    return 'SHOW_INFO'


def view_events(update: Update, _):
    query = update.callback_query
    query.answer()
    reply_markup = InlineKeyboardMarkup(get_keyboard_back)
    if query.data == 'view_upcoming_events':
        # ---------------------------------------
        # ближайшие мероприятия
        # ---------------------------------------
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
    return 'SHOW_INFO'
