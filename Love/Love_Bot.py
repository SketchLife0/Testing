import telebot

bot = telebot.TeleBot("5941936023:AAHUBnzn2tj0bznYfMR5QJCZENA1sjZ7_rM")

@bot.message_handler(commands=['start'])
def Love(message):
    while True:
        bot.send_message(message.chat.id, f'*цём*')

bot.infinity_polling()