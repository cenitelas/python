import telebot

# bot name FivernBot

bot = telebot.TeleBot('1083644677:AAFrkiMCpVAkrbE2UFxhslduYJcHPxcIKBU')

riddles = [("Зимой и летом одним цветом?", "ель"),
           ("Без окон без дверей полногорница людей", "огурец"),
           ("Сто одежек и все без застежек", "капуста"),
           ("Кто его раздевает тот слезы проливает", "лук"),
           ("Два конца, два кольца,посредине гвоздик", "ножницы"),
           ("Висит груша нельзя скушать", "лампочка"),
           ("Не лает, не кусает, в дом не пускает", "замок"),
           ("Ах, не трогайте меня, обожгу и без огня!", "крапива"),
           ("Апельсина брат меньшой, потому как небольшой", "мандарин"),
           ("В огороде хоть росла, знает ноты соль и фа", "фасоль")]

quest, answer = riddles.pop()

answers = []

@bot.message_handler(content_types=["text"])
def get_messages(message):
    global quest, answer
    if message.text == "/start":
        bot.send_message(message.chat.id, "Добро пожаловать!")
        bot.send_message(message.chat.id, quest)
    else:
        if len(answer) < 10:
            if answer == message.text:
                answers.append(f"Вы верно ответили - {message.text}")
            else:
                answers.append(f"Правильный ответ - {answer}")
        if len(riddles) > 0:
            quest, answer = riddles.pop()
            bot.send_message(message.chat.id, quest)
        else:
            for x in range(10):
                bot.send_message(message.chat.id, f"{x+1} - {answers[x]}")


if __name__ == '__main__':
     bot.polling(none_stop=True)