import telebot

TOKEN = '827583705:AAEb2ApHsxNKfuFWtR2Yu_YbR2PMBjmqO3M'
bot = telebot.TeleBot(TOKEN)
value = 0


@bot.message_handler(commands=['start'])
def start_command(message):
    print(message.message_id)
    bot.delete_message(message.chat.id, message.message_id)

    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Exchange XLM', callback_data='get-XLM')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Support', callback_data='get-Call-back')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Check status by number', callback_data='get-check-by-number')
    )

    bot.send_message(
        message.chat.id,
        'Welcome to XLM STELLAR EXCHANGE BOT!',
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
    if data.startswith('getUSD'):
        bot.answer_callback_query(query.id)
        gettingUSD(query.message)
    if data.startswith('getEUR'):
        bot.answer_callback_query(query.id)
        gettingEUR(query.message)
    if data.startswith('getPPUSD'):
        bot.answer_callback_query(query.id)
        gettingPPUSD(query.message)
    if data.startswith('getppeuro'):
        bot.answer_callback_query(query.id)
        gettingPPEUR(query.message)
    if data.startswith('getBackToXLM'):
        bot.answer_callback_query(query.id)
        getMyXLM(query.message)
    if data.startswith('yesButton'):
        bot.answer_callback_query(query.id)
        yesButton(query.message)
    if data.startswith('yespp'):
        bot.answer_callback_query(query.id)
        yesButtonPP(query.message)
    if data.startswith('yesppeuro'):
        bot.answer_callback_query(query.id)
        yesButtonPP(query.message)
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
        telebot.types.InlineKeyboardButton('Back', callback_data='getBack')
    )
    bot.send_message(message.chat.id, "Contact\n" + '@StellarExchangeSup', reply_markup=keyboard)


def checkByNumber(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Enter: \n" + 'Exchange request number:\n')
    bot.register_next_step_handler(message, cheking)


def cheking(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Back', callback_data='getBack')
    )
    bot.delete_message(message.chat.id, message.message_id - 1)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, 'Request №' + message.text + ' is being processed.', reply_markup=keyboard)


# Initialization
def getMyXLM(message):
    print(message.message_id)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_chat_action(message.chat.id, 'typing')
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('XLM on USD credit card', callback_data='getUSD'),
        telebot.types.InlineKeyboardButton('XLM on EUR credit card', callback_data='getEUR')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('XLM on PayPal', callback_data='getPPUSD'),
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Back', callback_data='getBack')
    )

    bot.send_message(
        message.chat.id,
        'Choose an exchange method\n' +
        '1 XLM -> 0.11 USD\n' +
        '1 XLM -> 0.1 EUR\n',
        reply_markup=keyboard
    )


def gettingUSD(message):
    print(message.message_id)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_chat_action(message.chat.id, 'typing')
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Back', callback_data='getBackToXLM')
    )

    bot.send_message(
        message.chat.id,
        'Enter the amount of XLM\n' +
        'Rate: 0.11$',
        reply_markup=keyboard
    )
    bot.register_next_step_handler(message, valueXLMUSD)


def gettingEUR(message):
    print(message.message_id)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_chat_action(message.chat.id, 'typing')
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Back', callback_data='getBackToXLM')
    )

    bot.send_message(
        message.chat.id,
        'Enter the amount of XLM\n' +
        'Rate: 0.1€',
        reply_markup=keyboard
    )
    bot.register_next_step_handler(message, valueXLMEUR)


def gettingPPUSD(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_chat_action(message.chat.id, 'typing')
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Back', callback_data='getBackToXLM')
    )

    bot.send_message(
        message.chat.id,
        'Enter the amount of XLM\n' +
        'Rate: USD = 0.11$ , EUR = 0.1€',
        reply_markup=keyboard
    )
    bot.register_next_step_handler(message, valueXLMPPUSD)


def gettingPPEUR(message):
    print('zbs')
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_chat_action(message.chat.id, 'typing')
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Back', callback_data='getBackToXLM')
    )

    bot.send_message(
        message.chat.id,
        'Enter the amount of XLM\n' +
        'Rate: 0.1€',
        reply_markup=keyboard
    )
    bot.register_next_step_handler(message, valueXLMPPEUR)


@bot.message_handler(content_types=['text'])
def valueXLMUSD(message):
    global price
    bot.delete_message(message.chat.id, message.message_id - 1)
    price = message.text
    global value
    if value == 0:
        try:

            if float(message.text) >= 549:
                keyboard = telebot.types.InlineKeyboardMarkup()
                keyboard.row(
                    telebot.types.InlineKeyboardButton('Yes', callback_data='yesButton')
                )
                keyboard.row(
                    telebot.types.InlineKeyboardButton('Back', callback_data='getBackToXLM')
                )
                bot.send_message(
                    message.from_user.id,
                    "You want to exchange " + str(message.text) + "XLM to " + str(float(message.text) * 0.11) + " USD",
                    reply_markup=keyboard
                )
            else:
                bot.send_message(message.from_user.id, 'min 549')
        except Exception:
            bot.send_message(message.from_user.id, 'Use numbers')

def valueXLMEUR(message):
    global price
    bot.delete_message(message.chat.id, message.message_id - 1)
    price = message.text
    global value
    if value == 0:
        try:

            if float(message.text) >= 549:
                keyboard = telebot.types.InlineKeyboardMarkup()
                keyboard.row(
                    telebot.types.InlineKeyboardButton('Yes', callback_data='yesButton')
                )
                keyboard.row(
                    telebot.types.InlineKeyboardButton('Back', callback_data='getBackToXLM')
                )
                bot.send_message(
                    message.from_user.id,
                    "You want to exchange " + str(message.text) + "XLM to " + str(float(message.text) * 0.1) + " EUR",
                    reply_markup=keyboard
                )
            else:
                bot.send_message(message.from_user.id, 'min 549')
        except Exception:
            bot.send_message(message.from_user.id, 'Use numbers')


def valueXLMPPUSD(message):
    global price
    bot.delete_message(message.chat.id, message.message_id - 1)
    price = message.text
    global value
    if value == 0:
        try:
            if int(message.text) >= 549:
                keyboard = telebot.types.InlineKeyboardMarkup()
                price = message.text
                keyboard.row(
                    telebot.types.InlineKeyboardButton('Yes', callback_data='yespp')
                )
                keyboard.row(
                    telebot.types.InlineKeyboardButton('Back', callback_data='getBackToXLM')
                )
                bot.send_message(
                    message.from_user.id,
                    "You want to exchange " + str(message.text) + "XLM to " + str(float(message.text) * 0.11) + " USD or " + str(float(message.text) * 0.1) + ' EUR',
                    reply_markup=keyboard
                )
            else:
                bot.send_message(message.from_user.id, 'min 549')
        except Exception:
            bot.send_message(message.from_user.id, 'Use numbers')


def yesButton(message):
    print(message.message_id)
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Back', callback_data='getBackToXLM')
    )
    bot.send_message(
        message.chat.id,
        'Enter card number\n' +
        'Like here: XXXX XXXX XXXX XXXX',
        reply_markup=keyboard
    )

    bot.register_next_step_handler(message, valueCardNumber)

def yesButtonPP(message):
    print(message.message_id)
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Back', callback_data='getBackToXLM')
    )
    bot.send_message(
        message.chat.id,
        'Enter your PayPal mail:',
        reply_markup=keyboard
    )

    bot.register_next_step_handler(message, userDataPP)


def valueCardNumber(message):
    print(message.message_id)
    bot.delete_message(message.chat.id, message.message_id)
    bot.delete_message(message.chat.id, message.message_id - 1)
    global card_number
    card_number = message.text
    if len(message.text) == 19:
        bot.send_message(message.from_user.id, "Enter the details of the card holder. Example: Ivanov Ivan.")
        bot.register_next_step_handler(message, userData)
    else:
        yesButton(message)




def userData(message):
    print(message.message_id)
    bot.delete_message(message.chat.id, message.message_id - 1)
    global user_data
    user_data = message.text
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Confirm', callback_data='confirm')
    )
    bot.send_message(
        message.chat.id,
        'Check the data entry is correct:\n' +
        'Card number: ' + card_number + '\n' +
        'Holder name: ' + message.text + '\n' +
        'Give:' + str(price) + '\n',
        reply_markup=keyboard
    )
    print('Card number: ' + card_number + '\n')
    print('Holder name: ' + message.text + '\n')
    print('Give:' + str(price) + '\n')

def userDataPP(message):
    pp_link = message.text
    print(message.message_id)
    bot.delete_message(message.chat.id, message.message_id - 1)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Confirm', callback_data='confirm')
    )
    bot.send_message(
        message.chat.id,
        'Check the data entry is correct:\n' +
        'PayPal: ' + pp_link + '\n' +
        'Give: ' + str(price) + '\n',
        reply_markup=keyboard
    )
    print('PayPal: ' + pp_link + '\n')
    print('Give:' + str(price) + '\n')


def confirm(message):
    print(message.message_id)
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Performed', callback_data='gotowo')
    )
    bot.send_message(
        message.chat.id,
        'Transfer the exact amount: ' + str(price) + ' XLM to wallet:\n' +
        'GB4JY7XWDUZAVFEZ4PURL42VTYOWGLUQ2R3RBNNLRD3BR7W276ZTJGEN\n' +
        'Your exchange request number:' + str(message.message_id),
        reply_markup=keyboard
    )




def finish(message):
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Back', callback_data='getBack')
    )
    bot.send_message(
        message.chat.id,
        'After confirmation by the operator of your transfer, the funds will be credited within 15-20 minutes.', reply_markup=keyboard
    )





bot.polling(none_stop=True)
