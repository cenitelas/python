import telebot

# bot name FivernBot

bot = telebot.TeleBot('1083644677:AAH1QsHlKR_s17kip0n-UpDtMWdI3WDuVWY')

result = {}

@bot.message_handler(content_types=["text"])
def get_messages(message):
    global result
    if message.text == "/start":
        bot.send_message(message.chat.id, "Добро пожаловать!")
    else:
        try:
            if not result.get(message.chat.id):
                result[message.chat.id] = float(message.text)
                bot.send_message(message.chat.id, message.text)
            else:
                result[message.chat.id] = result[message.chat.id]+float(message.text)
                bot.send_message(message.chat.id, result[message.chat.id])
        except Exception:
            bot.send_message(message.chat.id, "Введите число")


if __name__ == '__main__':
     bot.polling(none_stop=True)