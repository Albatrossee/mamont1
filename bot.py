import telebot

TOKEN = '887738069:AAHY-nswZIq3N_GSAQ939OIPnHLGRkAmx8s'
bot = telebot.TeleBot(TOKEN)
value = 0




@bot.message_handler(commands=['start'])
def start_command(message):
    print(message.message_id)
    bot.delete_message(message.chat.id, message.message_id)

    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Обмен XLM', callback_data='get-XLM')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Обратная связь', callback_data='get-Call-back')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Проверить заявку по номеру', callback_data='get-check-by-number')
    )

    bot.send_message(
        message.chat.id,
        'Вас приветствует XLM STELLAR EXCHANGE BOT!',
        reply_markup=keyboard
    )




# All the queries
@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    if data.startswith('get-XLM'):
        bot.answer_callback_query(query.id)
        getMyXLM(query.message)
    if data.startswith('getBack'):
        bot.answer_callback_query(query.id)
        start_command(query.message)
    if data.startswith('getUAH'):
        bot.answer_callback_query(query.id)
        gettingUAH(query.message)
    if data.startswith('getRUB'):
        bot.answer_callback_query(query.id)
        gettingRUB(query.message)
    if data.startswith('getBackToXLM'):
        bot.answer_callback_query(query.id)
        getMyXLM(query.message)
    if data.startswith('yesButton'):
        bot.answer_callback_query(query.id)
        yesButton(query.message)
    if data.startswith('confirm'):
        bot.answer_callback_query(query.id)
        confirm(query.message)
    if data.startswith('gotowo'):
        bot.answer_callback_query(query.id)
        finish(query.message)
    if data.startswith('get-Call-back'):
        bot.answer_callback_query(query.id)
        callback(query.message)
    if data.startswith('get-check-by-number'):
        bot.answer_callback_query(query.id)
        checkByNumber(query.message)


def callback(message):
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Назад', callback_data='getBack')
    )
    bot.send_message(message.chat.id, "Оператор\n" + '@StellarExchangeSup', reply_markup=keyboard)


def checkByNumber(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Что бы проверить заявку введите: \n" + 'Номер заявки:\n')
    bot.register_next_step_handler(message, cheking)


def cheking(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Назад', callback_data='getBack')
    )
    bot.delete_message(message.chat.id, message.message_id - 1)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, 'Заявка №' + message.text + ' обрабатывается.', reply_markup=keyboard)


# Initialization
def getMyXLM(message):
    print(message.message_id)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_chat_action(message.chat.id, 'typing')
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('XLM на карту UAH', callback_data='getUAH')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('XLM на карту RUB', callback_data='getRUB')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Назад', callback_data='getBack')
    )

    bot.send_message(
        message.chat.id,
        'Выберите способ обмена\n' +
        '1 XLM -> 2.12 UAH\n' +
        '1 XLM -> 4.77 RUB',
        reply_markup=keyboard
    )


def gettingUAH(message):
    print(message.message_id)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_chat_action(message.chat.id, 'typing')
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Назад', callback_data='getBackToXLM')
    )

    bot.send_message(
        message.chat.id,
        'Введите количество XLM\n' +
        'Курс: 2.12\n' +
        "Резерв: 163705",
        reply_markup=keyboard
    )
    bot.register_next_step_handler(message, valueXLMUAH)


def gettingRUB(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_chat_action(message.chat.id, 'typing')
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Назад', callback_data='getBackToXLM')
    )

    bot.send_message(
        message.chat.id,
        'Введите количество XLM\n' +
        'Курс: 4.77\n' +
        "Резерв: 163705",
        reply_markup=keyboard
    )
    bot.register_next_step_handler(message, valueXLMRUB)


@bot.message_handler(content_types=['text'])
def valueXLMUAH(message):
    global price
    bot.delete_message(message.chat.id, message.message_id - 1)
    price = message.text
    global value
    if value == 0:
        try:

            if float(message.text) >= 549:
                keyboard = telebot.types.InlineKeyboardMarkup()
                keyboard.row(
                    telebot.types.InlineKeyboardButton('Да', callback_data='yesButton')
                )
                keyboard.row(
                    telebot.types.InlineKeyboardButton('Назад', callback_data='getBackToXLM')
                )
                bot.send_message(
                    message.from_user.id,
                    "Вы хотите обменять " + str(message.text) + "XLM на " + str(float(message.text) * 2.12) + " UAH",
                    reply_markup=keyboard
                )
            else:
                bot.send_message(message.from_user.id, 'min 549')
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')


def valueXLMRUB(message):
    global price
    bot.delete_message(message.chat.id, message.message_id - 1)
    price = message.text
    global value
    if value == 0:
        try:
            if int(message.text) >= 549:
                keyboard = telebot.types.InlineKeyboardMarkup()
                keyboard.row(
                    telebot.types.InlineKeyboardButton('Да', callback_data='yesButton')
                )
                keyboard.row(
                    telebot.types.InlineKeyboardButton('Назад', callback_data='getBackToXLM')
                )
                bot.send_message(
                    message.from_user.id,
                    "Вы хотите обменять " + str(message.text) + "XLM на " + str(float(message.text) * 4.77) + " RUB",
                    reply_markup=keyboard
                )
            else:
                bot.send_message(message.from_user.id, 'min 549т   '
                                                       ''
                                                       '')
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')


def yesButton(message):
    print(message.message_id)
    #bot.delete_message(message.chat.id, message.message_id - 1)
    #bot.delete_message(message.chat.id, message.message_id - 2)
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Назад', callback_data='getBackToXLM')
    )
    bot.send_message(
        message.chat.id,
        'Введите номер карты\n' +
        'Формат: XXXX XXXX XXXX XXXX',
        reply_markup=keyboard
    )

    bot.register_next_step_handler(message, valueCardNumber)


def valueCardNumber(message):
    print(message.message_id)
    bot.delete_message(message.chat.id, message.message_id)
    bot.delete_message(message.chat.id, message.message_id - 1)
    global card_number
    card_number = message.text
    if len(message.text) > 15:
        bot.send_message(message.from_user.id, "Введите реквизиты держателя карты. Пример: Иванов Иван.")
        bot.register_next_step_handler(message, userData)
    else:
        bot.send_message(message.from_user.id, 'Введите действительный номер карты')
        bot.register_next_step_handler(message, valueCardNumber)
  


def userData(message):
    print(message.message_id)
    bot.delete_message(message.chat.id, message.message_id - 1)
    global user_data
    user_data = message.text
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Подтвердить', callback_data='confirm')
    )
    bot.send_message(
        message.chat.id,
        'Проверьте правильность введения данных:\n' +
        'Номер карты: ' + card_number + '\n' +
        'Имя держателя: ' + message.text + '\n' +
        'Отдаёте:' + str(price) + '\n',
        reply_markup=keyboard
    )
    print('Номер карты: ' + card_number + '\n')
    print('Имя держателя: ' + message.text + '\n')
    print('Отдаёте:' + str(price) + '\n')


def confirm(message):
    print(message.message_id)
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Выполнил', callback_data='gotowo')
    )
    bot.send_message(
        message.chat.id,
        'Переведите точную суму: ' + str(price) + ' XLM на кошелек:\n' +
        'GB4JY7XWDUZAVFEZ4PURL42VTYOWGLUQ2R3RBNNLRD3BR7W276ZTJGEN\n' +
        '№ вашей заявки ' + str(message.message_id),
        reply_markup=keyboard
    )




def finish(message):
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Назад', callback_data='getBack')
    )
    bot.send_message(
        message.chat.id,
        'После подтверждения оператором Вашего перевода средства будут зачислены в течении 15-20 минут.', reply_markup=keyboard
    )





bot.polling(none_stop=True)
