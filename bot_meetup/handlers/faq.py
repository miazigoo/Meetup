from telegram import Update, InlineKeyboardMarkup

from bot_meetup.keyboards.keyboards import get_keyboard_back

FAQ = """
Уважаемые пользователи❗️
ВПЕРВЫЕ‼️
Представляем вашему вниманию нашего бота❗️
Хотите спросить что он умеет⁉️
БОТ УМЕЕТ КАКАТЬ‼️
"""


def faq_u(update: Update, _):
    query = update.callback_query
    query.answer()
    reply_markup = InlineKeyboardMarkup(get_keyboard_back)
    if query.data == 'FAQ':
        query.edit_message_text(
            text=FAQ, reply_markup=reply_markup
        )
    else:
        query.edit_message_text(
            text=query.data, reply_markup=reply_markup
        )
    return 'GREETINGS'
