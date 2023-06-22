from telegram.ext import ConversationHandler, CommandHandler, \
    CallbackQueryHandler, MessageHandler, Filters

from bot_meetup.handlers.command import start_conversation, cancel
from bot_meetup.handlers.faq import faq_u
from bot_meetup.handlers.questions import ask_question, get_question
from bot_meetup.handlers.user_event import view_event

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start_conversation)],
    states={
        'GREETINGS': [
            CallbackQueryHandler(view_event, pattern='view_event'),
            CallbackQueryHandler(start_conversation, pattern='to_start'),
            CallbackQueryHandler(start_conversation, pattern='view_event'),
            CallbackQueryHandler(view_event, pattern='view_upcoming_events'),
            CallbackQueryHandler(ask_question, pattern='ask_question'),
            CallbackQueryHandler(faq_u, pattern='FAQ'),
        ],
        'SHOW_INFO': [
            CallbackQueryHandler(view_event, pattern='view_event'),
            CallbackQueryHandler(view_event, pattern='view_upcoming_events'),
            CallbackQueryHandler(start_conversation, pattern='to_start'),
        ],
        'GET_QUESTION': [
            CallbackQueryHandler(start_conversation, pattern='to_start'),
            MessageHandler(Filters.text, get_question),
        ],
    },
    fallbacks=[CommandHandler('cancel', cancel)]
)
