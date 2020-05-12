import telebot



bot=telebot.TeleBot('993119728:AAFJBC3QM3uVUnazKyvU-Y6NOhmTdV2ay4Y')





@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, 'Как тебя зовут?')
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')

def get_name(message): #получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    # while age == 0: #проверяем что возраст изменился
    try:
        age = int(message.text) #проверяем, что возраст введен корректно
        keyboard = telebot.types.InlineKeyboardMarkup()  # наша клавиатура
        key_yes = telebot.types.InlineKeyboardButton(text='Да', callback_data='yes')  # кнопка «Да»
        keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
        key_no = telebot.types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_no)
        question = 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    except Exception:
        bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
        bot.register_next_step_handler(message, get_age)


def  valut(message):
    keyboard = telebot.types.InlineKeyboardMarkup()


    button1 = telebot.types.InlineKeyboardButton(text="USD ЦБ РФ", url='https://yandex.ru/news/quotes/1.html')
    keyboard.add(button1)
    button2 = telebot.types.InlineKeyboardButton(text="EUR ЦБ РФ", url='https://yandex.ru/news/quotes/23.html')
    keyboard.add(button2)
    button3 = telebot.types.InlineKeyboardButton(text="GBP ЦБ РФ", url='https://yandex.ru/news/quotes/24.html')
    keyboard.add(button3)
    button4 = telebot.types.InlineKeyboardButton(text="JPY ЦБ РФ", url='https://yandex.ru/news/quotes/25.html')
    keyboard.add(button4)
    button5 = telebot.types.InlineKeyboardButton(text="Роснефть акция", url='https://yandex.ru/news/quotes/282.html')
    keyboard.add(button5)
    button6 = telebot.types.InlineKeyboardButton(text="Яндекс акция", url='https://yandex.ru/news/quotes/43.html')
    keyboard.add(button6)


    bot.send_message(message.from_user.id, text=message.text+',выбери валюту плиз', reply_markup=keyboard)
    bot.register_next_step_handler(message, turma)


def  turma(message):
    keyboard = telebot.types.InlineKeyboardMarkup()


    button1 = telebot.types.InlineKeyboardButton(text="Сидел", callback_data='Side')
    keyboard.add(button1)
    button2 = telebot.types.InlineKeyboardButton(text="Не сидел", callback_data='Notside')
    keyboard.add(button2)

    bot.register_next_step_handler(message, mast)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
 #код сохранения данных, или их обработки
        bot.send_message(call.message.chat.id, 'Запомню : )')
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Не понял')
    elif call.data == "fish":
        i = 0
        while i < 10:
            bot.send_message(call.message.chat.id, "Самоизоляция, сидите дома")
            i+=1

        bot.send_message(call.message.chat.id, "Самоизоляция, сидите дома")
         #переспрашиваем
    elif call.data == "koz":


        bot.send_message(call.message.chat.id, "Родной, сиди дома,пока масть не потерял")



    elif call.data == "shibut":

        bot.send_message(call.message.chat.id, "Родной, сиди ровно,похулиганишь, пока еще на свободе")

    elif call.data == "fraer":

        bot.send_message(call.message.chat.id, "На параше останешься, если нарушишь режим, понял")

    elif call.data == "poker":

        bot.send_message(call.message.chat.id, "Сиди дома играй, ферзь ")




bot.polling()




