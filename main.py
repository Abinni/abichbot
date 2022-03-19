import os
import logging
import responses
from telegram.ext import *
from dotenv import load_dotenv

# we use this to get api key from env files
load_dotenv()
API_KEY = os.getenv('API_KEY')

# Set up the logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


# We defined this fuction to use as commands
# all update.message are reply from bots to user
def start(update, context):
    update.message.reply_text(
        'Hello there, I\'m a personal assistant bot of @azi7x 🧑‍💻😼.')


def help(update, context):
    update.message.reply_text('what can I do for you /cmd')


def cmd(update, context):
    update.message.reply_text('Availble Commands:\nFor azoo- /azoo\n ')

def me(update, context):
    update.message.reply_text('Hello 🙂👋\n https://telegra.ph/file/1519970a343a283bf5277.jpg')

def azoo(update, context):
    update.message.reply_text(
        'Update soon 👋.')


def list(update, context):
    update.message.reply_text(
        'All commands you can use\n /help : offcourse for help\n\n /azoo: To get azoo\n\n /projects : all projects soon')

# there two methods to crete functions to get repond from bot this is 2nd one


def socials(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="List of Socails are down below:\n {Github} https://github.com/azin7\n\n {Email} moldmold123i1@gmail.com.ml")


def source_code(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="the source code can be accessed here\n {Github}\n https://github.com/azin7")


def projects(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="List of projects are down below:\n \n coming soon .ml")


def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')

    # Bot response
    response = responses.get_response(text)
    update.message.reply_text(response)


def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')


# Run the programms from here
if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    # Commands handler which callback our commands when user ask for it
    dp.add_handler(CommandHandler('start', start))

    dp.add_handler(CommandHandler('help', help))

    dp.add_handler(CommandHandler('cmd', cmd))

    dp.add_handler(CommandHandler('me', me))

    dp.add_handler(CommandHandler('azoo', azoo))

    dp.add_handler(CommandHandler('list', list))

    dp.add_handler(CommandHandler('socials', socials))

    dp.add_handler(CommandHandler('source_code', source_code))

    dp.add_handler(CommandHandler('projects', projects))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    # Idle state give bot time to go in idle
    updater.idle()
