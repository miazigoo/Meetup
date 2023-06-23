from telegram import ParseMode, InlineKeyboardMarkup, Update, ReplyKeyboardRemove
from telegram.ext import ConversationHandler

from bot_meetup.keyboards.keyboards import get_keyboard_start
from bot_meetup.models import Client

START_TEXT = "Вас приветствует Сервис PythonMeetup"


def start_conversation(update: Update, context):
    query = update.callback_query
    if query:
        query.answer()
    reply_markup = InlineKeyboardMarkup(get_keyboard_start)

    if query:
        query.edit_message_text(
            text=f"{START_TEXT}\nВыберете интересующий вопросssssss", reply_markup=reply_markup,
            parse_mode=ParseMode.HTML
        )
    else:
        chat_id = update.message.chat_id
        nickname = update.message.from_user.username
        # --------------------------------
        # Добавление в БД Юзера
        # --------------------------------
        Client.objects.get_or_create(
            telegram_id=chat_id,
            defaults={
                'nik_name': nickname
            }
        )
        update.message.reply_text(
            text=f"{START_TEXT}\nВыберете интересующий вас вопрос", reply_markup=reply_markup,
            parse_mode=ParseMode.HTML
        )

    return 'GREETINGS'


def cancel(update, _):
    # user = update.message.from_user
    # logger.info("Пользователь %s отменил разговор.", user.first_name)
    update.message.reply_text(
        'До новых встреч',
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END
