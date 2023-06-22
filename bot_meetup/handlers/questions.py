from telegram import Update, InlineKeyboardMarkup, ParseMode

from bot_meetup.keyboards.keyboards import get_keyboard_back

SPEAKER_NOW = """
Сейчас выступает SPEAKER_NOW.
Задайте интересующий вас вопрос:
"""


def ask_question(update: Update, _):
    """ Пользователь задает вопрос """
    query = update.callback_query
    query.answer()
    reply_markup = InlineKeyboardMarkup(get_keyboard_back)
    if query.data == 'ask_question':
        query.edit_message_text(
            text=SPEAKER_NOW, reply_markup=reply_markup
        )
    else:
        query.edit_message_text(
            text=query.data, reply_markup=reply_markup
        )
    return 'GET_QUESTION'


def get_question(update, context):
    """Запись вопроса в БД"""
    question = update.message.text
    # context.user_data['question'] = question
    # ------------------------------------------
    # Добавление вопроса в БД к данному спикеру.
    # ------------------------------------------
    reply_markup = InlineKeyboardMarkup(get_keyboard_back)
    update.message.reply_text(
        text="✅ Ув. Слушатель, ваш вопрос отправлен спикеру.\n"
             "Спикер ответит на все вопросы в момент паузы или"
             " ближе к концу лекции.", reply_markup=reply_markup,
        parse_mode=ParseMode.HTML
    )

    return 'GET_QUESTION'
