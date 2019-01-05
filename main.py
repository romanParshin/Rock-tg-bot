import telebot
import constants


bot = telebot.TeleBot(constants.token)


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('Информация', 'Контакты', 'Прайс')
    bot.send_message(message.from_user.id, message.from_user.first_name+str (',Че хотел ?'), reply_markup=user_markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Информация':
        user_markup = telebot.types.ReplyKeyboardMarkup(True)
        user_markup.row('Назад')
        bot.send_message(message.from_user.id, 'Won', reply_markup=user_markup)
    elif message.text == 'Контакты':
        user_markup = telebot.types.ReplyKeyboardMarkup(True)
        user_markup.row('Назад')
        bot.send_message(message.from_user.id, 'woon', reply_markup=user_markup)
    elif message.text == 'Прайс':
        user_markup = telebot.types.ReplyKeyboardMarkup(True)
        user_markup.row('Назад')
        bot.send_message(message.from_user.id, 'Wooon', reply_markup=user_markup)
    elif message.text == 'Назад':
        user_markup = telebot.types.ReplyKeyboardMarkup(True)
        user_markup.row('Информация', 'Контакты', 'Прайс')
        bot.send_message(message.from_user.id, 'Welcomr', reply_markup=user_markup)
    else:
        bot.send_message(message.from_user.id, 'sorry')


# @bot.message_handler(content_types=['text'])
# def handle_text(message):
#   if message.text == 'Информация':
#     bot.send_message(message.from_user.id,'Won' )
#  elif message.text == 'Контакты':
#  bot.send_message(message.from_user.id,'Win' )
# elif message.text == 'Прайс':
#   bot.send_message(message.from_user.id,'Winner')
# elif message.text == 'Назад':
#  bot.send_message(message.from_user.id, 'Welcome')


bot.polling(none_stop=True)
