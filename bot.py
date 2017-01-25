import logging

import chino

from config import base_url
from config import token
import os

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import InlineQueryHandler
from telegram import InlineQueryResultPhoto


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)
updater = Updater(token=token)
dispatcher = updater.dispatcher

path = os.path.dirname(os.path.realpath(__file__))


def start(bot, update):
    bot.sendPhoto(chat_id=update.message.chat_id, photo=open(path + '/chino.jpg', 'rb'))


def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)


def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)


def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    images = chino.say(query)
    for image in images:
        name, w, h = image
        results.append(
            InlineQueryResultPhoto(
                id=query.upper(),
                title='智乃 说',
                photo_url=base_url + name,
                thumb_url=base_url + name,
                photo_width=w,
                photo_height=h,
                description=query
            )
        )
    bot.answerInlineQuery(update.inline_query.id, results)


def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")


updater.start_polling()

inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)


