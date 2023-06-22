import logging

from django.core.management import BaseCommand
from environs import Env
from telegram.ext import Updater, CommandHandler

from bot_meetup.handlers.command import start_conversation
from bot_meetup.handlers.conv_handler import conv_handler

# Ведение журнала логов
from Meetup import settings

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **kwargs):
        logger.info('Bot is running')
        env = Env()
        env.read_env()
        tg_bot_token = settings.tg_token
        updater = Updater(token=tg_bot_token, use_context=True)
        dispatcher = updater.dispatcher

        dispatcher.add_handler(conv_handler)
        start_handler = CommandHandler('start', start_conversation)
        dispatcher.add_handler(start_handler)

        start_handler = CommandHandler('cancel', start_conversation)
        dispatcher.add_handler(start_handler)

        updater.start_polling()
        updater.idle()
