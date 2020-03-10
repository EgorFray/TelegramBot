import telebot

bot = telebot.TeleBot('1013437132:AAHwtzRJffJWNawWc8fTagbv4DCTuypQHi0')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Шифровать', 'Расшифровывать')
slovo = '';
slovar = [];
slovar1 = [];
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, выбери что будем делать', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Шифровать':
        bot.send_message(message.chat.id, 'Напиши слово которое будем шифровать')
        bot.register_next_step_handler(message, shifrowka)
    elif message.text == 'Расшифровывать':
        bot.send_message(message.chat.id, 'Напиши зашифрованое слово')
        bot.register_next_step_handler(message, rashifrowka)


def shifrowka(message):
    global slovo;
    global slovar;
    slovo = message.text
    for i in slovo:
        slovar.append(chr(ord(i) + 1))
    bot.send_message(message.chat.id, ''.join(slovar))
    slovar.clear()


def rashifrowka(message):
    global slovo;
    global slovar1;
    slovo = message.text
    for i in slovo:
        slovar1.append(chr(ord(i) - 1))
    bot.send_message(message.chat.id, ''.join(slovar1))
    slovar.clear()



bot.polling()