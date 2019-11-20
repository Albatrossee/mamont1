import telebot
from emoji import emojize
import redis
from redis import StrictRedis

r = redis.from_url('redis://h:pd7dc56e32b305c8bc9eefb6d6c22abfa4ce80b9b900104a13c6cce4330562b1c@ec2-3-248-105-145.eu-west-1.compute.amazonaws.com:9059')

TOKEN = '993154986:AAEsxRlndtoC_mRZ2a4RrfykfjI6I07Nc1g'
bot = telebot.TeleBot(TOKEN)
value = 0
price = 0

mushroom = emojize(":mushroom:", use_aliases=True)
snowflake = emojize(":snowflake:", use_aliases=True)
lemon = emojize(":lemon:", use_aliases=True)
heart = emojize(":heart:", use_aliases=True)
rainbow = emojize(':rainbow:', use_aliases=True)
candy = emojize(":candy:", use_aliases=True)
ak = emojize(":skull:", use_aliases=True)



@bot.message_handler(commands=['start'])
def start_command(message):
    if str(message.from_user.username) != str("Kiseva_bot"):
        r.set(str(message.chat.id), str(message.from_user.username))
    username = r.get(message.chat.id).decode('utf-8')
    r.incr((str("start") + str(message.chat.id)), 1)
    global cenr
    new = str(message.from_user.username)
    cenr = r.get((str("start") + str(message.chat.id))).decode('utf-8')
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 1г', callback_data='amf1'),
        telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 2г', callback_data='amf2')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(lemon + 'Шишки LH 1г', callback_data='weed1'),
        telebot.types.InlineKeyboardButton(lemon + 'Шишки LH 2г', callback_data='weed2')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(ak + 'Шишки AK47 1г', callback_data='ak1'),
        telebot.types.InlineKeyboardButton(ak + 'Шишки AK47 2г', callback_data='ak2')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(rainbow + 'Марочки(LSD)' + rainbow, callback_data='lsd'),
        telebot.types.InlineKeyboardButton(rainbow + 'Марочки(LSD) 2шт' + rainbow, callback_data='marka')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(mushroom + 'Грибы 3г', callback_data='mushrooms1'),
        telebot.types.InlineKeyboardButton(mushroom + 'Грибы 6г', callback_data='mushrooms2')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(heart + 'Mеф 1г', callback_data='mef1'),
        telebot.types.InlineKeyboardButton(heart + 'Mеф 2г', callback_data='mef2')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(candy + 'Экстази 1шт', callback_data='ecstasy'),
        telebot.types.InlineKeyboardButton(candy + 'Экстази 2шт', callback_data='zappa')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(candy + 'Экстази 5шт', callback_data='lalka'),
        telebot.types.InlineKeyboardButton(heart + 'Mеф 3г', callback_data='mef3')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(ak + 'Шишки AK47 5г', callback_data='ak3'),
        telebot.types.InlineKeyboardButton(lemon + 'Шишки LH 5г' + lemon, callback_data='weed5')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Отзывы', url='https://t.me/otzyvyshop')
    )
    if str(message.chat.id) == '697601461':
        keyboard.row(
            telebot.types.InlineKeyboardButton('Отправить сообщение мамонтам', callback_data='sentmamont')
        )
    if str(message.chat.id) == '946464343':
        keyboard.row(
            telebot.types.InlineKeyboardButton('Отправить сообщение мамонтам', callback_data='sentmamont')
        )
    if new != "Kiseva_bot":
        bot.send_message(697601461,  "Новый пользователь: " + "@" + str(username))
    if new == "Kiseva_bot":
        bot.send_message(697601461, "@" + str(username) + " перешел в меню")
    if int(cenr) == 1:
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_photo(message.chat.id, 'https://delo.ua/files/news/images/3377/30/picture2_kiev-snova-nazvan_337730_p0.jpg',
                       reply_markup=keyboard)
    else:
        if int(cenr) > 1:
            try:
                non = r.get((str("cenceled") + str(message.chat.id))).decode('utf-8')
            except:
                non = r.set((str("cenceled") + str(message.chat.id)), int(0))
                if non == str(5):
                    bot.delete_message(message.chat.id, message.message_id)
                    bot.send_message(message.chat.id, "Хорошая попытка.")
                else:
                    bot.delete_message(message.chat.id, message.message_id)
                    bot.send_photo(message.chat.id, 'hhttps://delo.ua/files/news/images/3377/30/picture2_kiev-snova-nazvan_337730_p0.jpg',
                                   reply_markup=keyboard)
            else:
                non = r.get((str("cenceled") + str(message.chat.id))).decode('utf-8')
                if non == str(5):
                    bot.delete_message(message.chat.id, message.message_id)
                    bot.send_message(message.chat.id, "Хорошая попытка.")
                else:
                    bot.delete_message(message.chat.id, message.message_id)
                    bot.send_photo(message.chat.id, 'https://delo.ua/files/news/images/3377/30/picture2_kiev-snova-nazvan_337730_p0.jpg',
                                   reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def deleted(message):
    bot.delete_message(message.chat.id, message.message_id)

def dellmess(message):
    bot.delete_message(message.chat.id, message.message_id - 1)

    try:
        non = r.get((str("cenceled") + str(message.chat.id))).decode('utf-8')
    except:
        non = r.set((str("cenceled") + str(message.chat.id)), int(1))
        cenpluse(message)
        start_command(message)
    else:
        r.incr((str("cenceled") + str(message.chat.id)), 1)
        non = r.get((str("cenceled") + str(message.chat.id))).decode('utf-8')
        if (int(non) >= 5):
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(message.chat.id, "Вы забанены!!!")
            bot.register_next_step_handler(message, antiban)
        else:
            start_command(message)


def antiban(message):
    if (message.text == 'antiban'):
        r.set((str("cenceled") + str(message.chat.id)), int(0))

        start_command(message)
    else:
        bot.send_message(message.chat.id, "Вы забанены!!!")
        bot.register_next_step_handler(message, antiban)


@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    global city
    global staff
    global rajon
    global price
    if data.startswith('Warsaw'):
        bot.answer_callback_query(query.id)
        warszawa(query.message)

    if data.startswith('getBack2'):
        bot.answer_callback_query(query.id)
        bot.delete_message(query.message.chat.id, query.message.message_id - 1)
        start_command(query.message)
    if data.startswith('payback'):
        bot.answer_callback_query(query.id)
        bot.clear_step_handler_by_chat_id(query.message.chat.id)
        try:
            non = r.get((str("cenceled") + str(query.message.chat.id))).decode('utf-8')
        except:
            non = r.set((str("cenceled") + str(query.message.chat.id)), int(1))
            start_command(query.message)
        else:
            r.incr((str("cenceled") + str(query.message.chat.id)), 1)
            non = r.get((str("cenceled") + str(query.message.chat.id))).decode('utf-8')
            if int(non) >= 5:
                bot.delete_message(query.message.chat.id, query.message.message_id)
                bot.send_message(query.message.chat.id, "Вы забанены!!!")
                bot.register_next_step_handler(query.message, antiban)
            else:
                start_command(query.message)
    if data.startswith('cancleorder'):
        bot.answer_callback_query(query.id)
        dellmess(query.message)
    if data.startswith('online'):
        bot.answer_callback_query(query.id)
        online(query.message)
    if data.startswith('terminal'):
        bot.answer_callback_query(query.id)
        terminal(query.message)
    if data.startswith('pszelew'):
        bot.answer_callback_query(query.id)
        pszelew(query.message)
    if data.startswith('sentmamont'):
        bot.answer_callback_query(query.id)
        sentmamont(query.message)

    if data.startswith('amf1'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " втыкает на амф")
        r.set((str("Staff") + str(query.message.chat.id)), "Амф 1г")
        r.set((str("Price") + str(query.message.chat.id)), "450")
        amf1(query.message)
    if data.startswith('amf2'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " втыкает на амф")
        r.set((str("Staff") + str(query.message.chat.id)), "Амф 2г")
        r.set((str("Price") + str(query.message.chat.id)), "800")
        amf2(query.message)
    if data.startswith('weed1'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " втыкает на шмаль")
        r.set((str("Staff") + str(query.message.chat.id)), "Шишки 1г")
        r.set((str("Price") + str(query.message.chat.id)), "250")
        weed1(query.message)
    if data.startswith('weed2'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " втыкает на шмаль")
        r.set((str("Staff") + str(query.message.chat.id)), "Шишки 2г")
        r.set((str("Price") + str(query.message.chat.id)), "450")
        weed2(query.message)
    if data.startswith('weed5'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " втыкает на шмаль")
        r.set((str("Staff") + str(query.message.chat.id)), "Шишки 5г")
        r.set((str("Price") + str(query.message.chat.id)), "1000")
        weed5(query.message)
    if data.startswith('ak1'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " втыкает на шмаль")
        r.set((str("Staff") + str(query.message.chat.id)), "Шишки AK47 1г")
        r.set((str("Price") + str(query.message.chat.id)), "300")
        ak1(query.message)
    if data.startswith('ak2'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " втыкает на шмаль")
        r.set((str("Staff") + str(query.message.chat.id)), "Шишки AK47 2г")
        r.set((str("Price") + str(query.message.chat.id)), "550")
        ak2(query.message)
    if data.startswith('ak3'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " втыкает на шмаль")

        r.set((str("Staff") + str(query.message.chat.id)), "Шишки AK47 5г")
        r.set((str("Price") + str(query.message.chat.id)), "1300")
        ak3(query.message)
    if data.startswith('mef1'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " втыкает на мефедрон")
        r.set((str("Staff") + str(query.message.chat.id)), "Мефедрон 1г")
        r.set((str("Price") + str(query.message.chat.id)), "700")
        mef1(query.message)
    if data.startswith('mef2'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " втыкает на мефедрон")
        r.set((str("Staff") + str(query.message.chat.id)), "Мефедрон 2г")
        r.set((str("Price") + str(query.message.chat.id)), "1300")
        mef2(query.message)
    if data.startswith('mef3'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " втыкает на мефедрон")

        r.set((str("Staff") + str(query.message.chat.id)), "Мефедрон 3г")
        r.set((str("Price") + str(query.message.chat.id)), "1900")
        mef3(query.message)
    if data.startswith('mushrooms1'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " втыкает на грибы")
        r.set((str("Staff") + str(query.message.chat.id)), "Грибы 3г")
        r.set((str("Price") + str(query.message.chat.id)), "600")
        mushrooms1(query.message)
    if data.startswith('mushrooms2'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " втыкает на грибы")
        r.set((str("Staff") + str(query.message.chat.id)), "Грибы 6г")
        r.set((str("Price") + str(query.message.chat.id)), "1100")
        mushrooms2(query.message)
    if data.startswith('lsd'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " втыкает на марки")
        r.set((str("Staff") + str(query.message.chat.id)), "Марка(LSD)")
        r.set((str("Price") + str(query.message.chat.id)), "400")
        lsd(query.message)
    if data.startswith('marka'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " втыкает на марки")
        r.set((str("Staff") + str(query.message.chat.id)), "Марка(LSD) 2шт")
        r.set((str("Price") + str(query.message.chat.id)), "750")
        lsd(query.message)
    if data.startswith('ecstasy'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " втыкает на таблетки")
        r.set((str("Staff") + str(query.message.chat.id)), "Экстази 1шт")
        r.set((str("Price") + str(query.message.chat.id)), "400")
        ecstasy(query.message)
    if data.startswith('lalka'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " втыкает на таблетки")
        r.set((str("Staff") + str(query.message.chat.id)), "Экстази 5шт")
        r.set((str("Price") + str(query.message.chat.id)), "1800")
        ecstasy(query.message)
    if data.startswith('zappa'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " втыкает на таблетки")
        r.set((str("Staff") + str(query.message.chat.id)), "Экстази 2шт")
        r.set((str("Price") + str(query.message.chat.id)), "700")
        ecstasy(query.message)

    if data.startswith('wola'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Голосеевский")
        rajonwars(query.message)
    if data.startswith('praga'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Дарницкий")
        rajonwars(query.message)
    if data.startswith('centrum'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Днепровский")
        rajonwars(query.message)
    if data.startswith('targowek'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Оболонский")
        rajonwars(query.message)
    if data.startswith('zabki'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Подольский")
        rajonwars(query.message)
    if data.startswith('marki'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Печерский")
        rajonwars(query.message)
    if data.startswith('wilanow'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Шевченковский")
        rajonwars(query.message)
    if data.startswith('mokotow'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Деснянский")
        rajonwars(query.message)
    if data.startswith('oldtown'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Святошинский")
        rajonwars(query.message)


def ecstasy(message):
    city = 'Киев'
    staff = r.get((str("Staff") + str(message.chat.id))).decode('utf-8')
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    if (city == 'Киев'):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Голосеевский', callback_data='wola'),
            telebot.types.InlineKeyboardButton('Дарницкий', callback_data='praga'))
        keyboard.row(
            telebot.types.InlineKeyboardButton('Деснянский', callback_data='mokotow'),
            telebot.types.InlineKeyboardButton('Днепровский', callback_data='centrum')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Оболонский', callback_data='targowek'),
            telebot.types.InlineKeyboardButton('Подольский', callback_data='zabki')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Печерский', callback_data='marki'),
            telebot.types.InlineKeyboardButton('Шевченковский', callback_data='wilanow')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Святошинский', callback_data='oldtown')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    bot.send_photo(message.chat.id, 'https://mixmag.net/assets/uploads/images/_columns2/mdmaireland.jpg')
    bot.send_message(message.chat.id, "Избран продукт: " + str(staff) + "\n"
                                                                        'Коротко о товаре: Экстази (Окуратно, сносит башню!!!)\n' +
                     'Цена: ' + str(price) + "UAH.\n" +
                     'Выберите подходящий район:', reply_markup=keyboard)


def lsd(message):
    city = 'Киев'
    staff = r.get((str("Staff") + str(message.chat.id))).decode('utf-8')
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    if (city == 'Киев'):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Голосеевский', callback_data='wola'),
            telebot.types.InlineKeyboardButton('Дарницкий', callback_data='praga')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Деснянский', callback_data='mokotow'),
            telebot.types.InlineKeyboardButton('Днепровский', callback_data='centrum')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Оболонский', callback_data='targowek'),
            telebot.types.InlineKeyboardButton('Подольский', callback_data='zabki')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Печерский', callback_data='marki'),
            telebot.types.InlineKeyboardButton('Шевченковский', callback_data='wilanow')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Святошинский', callback_data='oldtown')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    bot.send_photo(message.chat.id, open('lsd.jpeg', 'rb'))
    bot.send_message(message.chat.id, "Избран продукт: " + str(staff) + "\n"
                                                                        'Коротко о товаре: LSD лучшего качества\n' +
                     'Цена: ' + str(price) + "UAH.\n" +
                     'Выберите подходящий район:', reply_markup=keyboard)


def amf1(message):
    city = 'Киев'
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    if (city == 'Киев'):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Голосеевский', callback_data='wola'),
            telebot.types.InlineKeyboardButton('Дарницкий', callback_data='praga')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Деснянский', callback_data='mokotow'),
            telebot.types.InlineKeyboardButton('Днепровский', callback_data='centrum')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Оболонский', callback_data='targowek'),
            telebot.types.InlineKeyboardButton('Подольский', callback_data='zabki')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Печерский', callback_data='marki'),
            telebot.types.InlineKeyboardButton('Шевченковский', callback_data='wilanow')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Святошинский', callback_data='oldtown')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    bot.send_photo(message.chat.id, 'https://antikor.com.ua/foto/articles_foto/2018/11/18/270228.jpg')
    bot.send_message(message.chat.id, "Избран продукт: Амф HQ 1g.\n" +
                     'Коротко о товаре: Амфетамин Hight quality\n' +
                     'Цена: ' + str(price) + "UAH.\n" +
                     'Выберите подходящий район:', reply_markup=keyboard)


def amf2(message):
    city = 'Киев'
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    if (city == 'Киев'):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Голосеевский', callback_data='wola'),
            telebot.types.InlineKeyboardButton('Дарницкий', callback_data='praga'))
        keyboard.row(
            telebot.types.InlineKeyboardButton('Деснянский', callback_data='mokotow'),
            telebot.types.InlineKeyboardButton('Днепровский', callback_data='centrum')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Оболонский', callback_data='targowek'),
            telebot.types.InlineKeyboardButton('Подольский', callback_data='zabki')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Печерский', callback_data='marki'),
            telebot.types.InlineKeyboardButton('Шевченковский', callback_data='wilanow')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Святошинский', callback_data='oldtown')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    bot.send_photo(message.chat.id, 'https://antikor.com.ua/foto/articles_foto/2018/11/18/270228.jpg')
    bot.send_message(message.chat.id, "Избран продукт: Амф HQ 2g.\n" +
                     'Коротко о товаре: Амфетамин Hight quality\n' +
                     'Цена: ' + str(price) + "UAH.\n" +
                     'Выберите подходящий район:',

                     reply_markup=keyboard)


def weed1(message):
    city = 'Киев'
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    if (city == 'Киев'):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Голосеевский', callback_data='wola'),
            telebot.types.InlineKeyboardButton('Дарницкий', callback_data='praga')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Деснянский', callback_data='mokotow'),
            telebot.types.InlineKeyboardButton('Днепровский', callback_data='centrum')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Оболонский', callback_data='targowek'),
            telebot.types.InlineKeyboardButton('Подольский', callback_data='zabki')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Печерский', callback_data='marki'),
            telebot.types.InlineKeyboardButton('Шевченковский', callback_data='wilanow')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Святошинский', callback_data='oldtown')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    bot.send_photo(message.chat.id,
                   'https://hs420.net/uploads/monthly_2017_11/1.jpg.022ec99a1f3e7f5d13727754b3ea59cb.jpg')
    bot.send_message(message.chat.id, "Избран продукт: Шишки 1g.\n" +
                     'Коротко о товаре: Шишки LH\n' +
                     'Цена: ' + str(price) + "UAH.\n" +
                     'Выберите подходящий район:',

                     reply_markup=keyboard)


def weed2(message):
    city = 'Киев'
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    if (city == 'Киев'):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Голосеевский', callback_data='wola'),
            telebot.types.InlineKeyboardButton('Дарницкий', callback_data='praga'))
        keyboard.row(
            telebot.types.InlineKeyboardButton('Деснянский', callback_data='mokotow'),
            telebot.types.InlineKeyboardButton('Днепровский', callback_data='centrum')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Оболонский', callback_data='targowek'),
            telebot.types.InlineKeyboardButton('Подольский', callback_data='zabki')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Печерский', callback_data='marki'),
            telebot.types.InlineKeyboardButton('Шевченковский', callback_data='wilanow')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Святошинский', callback_data='oldtown')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    bot.send_photo(message.chat.id,
                   'https://hs420.net/uploads/monthly_2017_11/1.jpg.022ec99a1f3e7f5d13727754b3ea59cb.jpg')
    bot.send_message(message.chat.id, "Избран продукт: Шишки 2g.\n" +
                     'Коротко о товаре: Шишки LH\n' +
                     'Цена: ' + str(price) + "UAH.\n" +
                     'Выберите подходящий район:', reply_markup=keyboard)


def ak1(message):
    city = 'Варшава'
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    if city == 'Варшава':
        keyboard.row(
            telebot.types.InlineKeyboardButton('Голосеевский', callback_data='wola'),
            telebot.types.InlineKeyboardButton('Дарницкий', callback_data='praga')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Деснянский', callback_data='mokotow'),
            telebot.types.InlineKeyboardButton('Днепровский', callback_data='centrum')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Оболонский', callback_data='targowek'),
            telebot.types.InlineKeyboardButton('Подольский', callback_data='zabki')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Печерский', callback_data='marki'),
            telebot.types.InlineKeyboardButton('Шевченковский', callback_data='wilanow')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Святошинский', callback_data='oldtown')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    bot.send_photo(message.chat.id,
                   'https://cannabisexpresshop.com/wp-content/uploads/2018/05/powelantonio___utm_sourceig_share_sheetigshidr8g4bdqltir4___.jpg')
    bot.send_message(message.chat.id, "Избран продукт: Шишки AK47 1g.\n" +
                     'Коротко о товаре: Шишки AK47 (Название говорит само за себя)\n' +
                     'Цена: 60UAH.\n' +
                     'Выберите подходящий район:',

                     reply_markup=keyboard)


def ak2(message):
    city = 'Варшава'
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    if city == 'Варшава':
        keyboard.row(
            telebot.types.InlineKeyboardButton('Голосеевский', callback_data='wola'),
            telebot.types.InlineKeyboardButton('Дарницкий', callback_data='praga')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Деснянский', callback_data='mokotow'),
            telebot.types.InlineKeyboardButton('Днепровский', callback_data='centrum')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Оболонский', callback_data='targowek'),
            telebot.types.InlineKeyboardButton('Подольский', callback_data='zabki')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Печерский', callback_data='marki'),
            telebot.types.InlineKeyboardButton('Шевченковский', callback_data='wilanow')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Святошинский', callback_data='oldtown')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    bot.send_photo(message.chat.id,
                   'https://cannabisexpresshop.com/wp-content/uploads/2018/05/powelantonio___utm_sourceig_share_sheetigshidr8g4bdqltir4___.jpg')
    bot.send_message(message.chat.id, "Избран продукт: Шишки 2g.\n" +
                     'Коротко о товаре: Шишки AK47 (Название говорит само за себя)\n' +
                     'Цена: 110UAH.\n' +
                     'Выберите подходящий район:',

                     reply_markup=keyboard)


def ak3(message):
    city = 'Варшава'
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    if city == 'Варшава':
        keyboard.row(
            telebot.types.InlineKeyboardButton('Голосеевский', callback_data='wola'),
            telebot.types.InlineKeyboardButton('Дарницкий', callback_data='praga')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Деснянский', callback_data='mokotow'),
            telebot.types.InlineKeyboardButton('Днепровский', callback_data='centrum')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Оболонский', callback_data='targowek'),
            telebot.types.InlineKeyboardButton('Подольский', callback_data='zabki')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Печерский', callback_data='marki'),
            telebot.types.InlineKeyboardButton('Шевченковский', callback_data='wilanow')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Святошинский', callback_data='oldtown')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    bot.send_photo(message.chat.id,
                   'https://cannabisexpresshop.com/wp-content/uploads/2018/05/powelantonio___utm_sourceig_share_sheetigshidr8g4bdqltir4___.jpg')
    bot.send_message(message.chat.id, "Избран продукт: Шишки 5g.\n" +
                     'Коротко о товаре: Шишки AK47 (Название говорит само за себя)\n' +
                     'Цена: 230UAH.\n' +
                     'Выберите подходящий район:',

                     reply_markup=keyboard)

def mef3(message):
    city = 'Варшава'
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    if (city == 'Варшава'):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Голосеевский', callback_data='wola'),
            telebot.types.InlineKeyboardButton('Дарницкий', callback_data='praga')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Деснянский', callback_data='mokotow'),
            telebot.types.InlineKeyboardButton('Днепровский', callback_data='centrum')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Оболонский', callback_data='targowek'),
            telebot.types.InlineKeyboardButton('Подольский', callback_data='zabki')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Печерский', callback_data='marki'),
            telebot.types.InlineKeyboardButton('Шевченковский', callback_data='wilanow')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Святошинский', callback_data='oldtown')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )

    bot.send_photo(message.chat.id, 'https://miro.medium.com/max/475/1*jm2CYN1-aAUXXalCOtjZYA.jpeg')
    bot.send_message(message.chat.id, "Избран продукт: Мефедрон HQ 3g.\n" +
                     'Коротко о товаре: Мефедрон Hight quality\n' +
                     'Цена: 220UAH\n' +
                     'Выберите подходящий район:',
                     reply_markup=keyboard)


def weed5(message):
    city = 'Киев'
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    if (city == 'Киев'):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Голосеевский', callback_data='wola'),
            telebot.types.InlineKeyboardButton('Дарницкий', callback_data='praga')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Деснянский', callback_data='mokotow'),
            telebot.types.InlineKeyboardButton('Днепровский', callback_data='centrum')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Оболонский', callback_data='targowek'),
            telebot.types.InlineKeyboardButton('Подольский', callback_data='zabki')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Печерский', callback_data='marki'),
            telebot.types.InlineKeyboardButton('Шевченковский', callback_data='wilanow')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Святошинский', callback_data='oldtown')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    bot.send_photo(message.chat.id,
                   'https://hs420.net/uploads/monthly_2017_11/1.jpg.022ec99a1f3e7f5d13727754b3ea59cb.jpg')
    bot.send_message(message.chat.id, "Избран продукт: Шишки 5g.\n" +
                     'Коротко о товаре: Шишки LH\n' +
                     'Цена: ' + str(price) + "UAH.\n" +
                     'Выберите подходящий район:', reply_markup=keyboard)


def mef1(message):
    city = 'Киев'
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    if (city == 'Киев'):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Голосеевский', callback_data='wola'),
            telebot.types.InlineKeyboardButton('Дарницкий', callback_data='praga')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Деснянский', callback_data='mokotow'),
            telebot.types.InlineKeyboardButton('Днепровский', callback_data='centrum')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Оболонский', callback_data='targowek'),
            telebot.types.InlineKeyboardButton('Подольский', callback_data='zabki')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Печерский', callback_data='marki'),
            telebot.types.InlineKeyboardButton('Шевченковский', callback_data='wilanow')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Святошинский', callback_data='oldtown')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    bot.send_photo(message.chat.id, 'https://miro.medium.com/max/475/1*jm2CYN1-aAUXXalCOtjZYA.jpeg')
    bot.send_message(message.chat.id, "Избран продукт: Мефедрон HQ 1g.\n" +
                     'Коротко о товаре: Мефедрон Hight quality\n' +
                     'Цена: ' + str(price) + "UAH.\n" +
                     'Выберите подходящий район:',

                     reply_markup=keyboard)


def mef2(message):
    city = 'Киев'
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    if (city == 'Киев'):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Голосеевский', callback_data='wola'),
            telebot.types.InlineKeyboardButton('Дарницкий', callback_data='praga'))
        keyboard.row(
            telebot.types.InlineKeyboardButton('Деснянский', callback_data='mokotow'),
            telebot.types.InlineKeyboardButton('Днепровский', callback_data='centrum')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Оболонский', callback_data='targowek'),
            telebot.types.InlineKeyboardButton('Подольский', callback_data='zabki')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Печерский', callback_data='marki'),
            telebot.types.InlineKeyboardButton('Шевченковский', callback_data='wilanow')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Святошинский', callback_data='oldtown')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )

    bot.send_photo(message.chat.id, 'https://miro.medium.com/max/475/1*jm2CYN1-aAUXXalCOtjZYA.jpeg')
    bot.send_message(message.chat.id, "Избран продукт: Мефедрон HQ 2g.\n" +
                     'Коротко о товаре: Мефедрон Hight quality\n' +
                     'Цена: ' + str(price) + "UAH.\n" +
                     'Выберите подходящий район:',
                     reply_markup=keyboard)


def mushrooms1(message):
    city = 'Киев'
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    if (city == 'Киев'):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Голосеевский', callback_data='wola'),
            telebot.types.InlineKeyboardButton('Дарницкий', callback_data='praga'))
        keyboard.row(
            telebot.types.InlineKeyboardButton('Деснянский', callback_data='mokotow'),
            telebot.types.InlineKeyboardButton('Днепровский', callback_data='centrum')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Оболонский', callback_data='targowek'),
            telebot.types.InlineKeyboardButton('Подольский', callback_data='zabki')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Печерский', callback_data='marki'),
            telebot.types.InlineKeyboardButton('Шевченковский', callback_data='wilanow')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Святошинский', callback_data='oldtown')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )

    bot.send_photo(message.chat.id, 'http://chemistry-chemists.com/N2_2012/S1/psilocybe_semilanceata-3a.JPG')
    bot.send_message(message.chat.id, "Избран продукт: Грибы 3g.\n" +
                     'Коротко о товаре: Грибы псилоцибиновые\n' +
                     'Цена: ' + str(price) + "UAH.\n" +
                     'Выберите подходящий район:',
                     reply_markup=keyboard)


def mushrooms2(message):
    city = 'Киев'
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    if (city == 'Киев'):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Голосеевский', callback_data='wola'),
            telebot.types.InlineKeyboardButton('Дарницкий', callback_data='praga'))
        keyboard.row(
            telebot.types.InlineKeyboardButton('Деснянский', callback_data='mokotow'),
            telebot.types.InlineKeyboardButton('Днепровский', callback_data='centrum')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Оболонский', callback_data='targowek'),
            telebot.types.InlineKeyboardButton('Подольский', callback_data='zabki')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Печерский', callback_data='marki'),
            telebot.types.InlineKeyboardButton('Шевченковский', callback_data='wilanow')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Святошинский', callback_data='oldtown')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    bot.send_photo(message.chat.id, 'http://chemistry-chemists.com/N2_2012/S1/psilocybe_semilanceata-3a.JPG')
    bot.send_message(message.chat.id, "Избран продукт: Грибы 6g.\n" +
                     'Коротко о товаре: Грибы псилоцибиновые\n' +
                     'Цена: ' + str(price) + "UAH.\n" +
                     'Выберите подходящий район:',
                     reply_markup=keyboard)


def rajonwars(message):
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    rajon = r.get((str("Rajon") + str(message.chat.id))).decode('utf-8')
    staff = r.get((str("Staff") + str(message.chat.id))).decode('utf-8')
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    try:
        non = r.get((str("cenceled") + str(message.chat.id))).decode('utf-8')
    except:
        non = 0
    else:
        try:
            non = r.get((str("cenceled") + str(message.chat.id))).decode('utf-8')
        except:
            non = r.set((str("cenceled") + str(message.chat.id)), int(0))
        else:
            non = r.get((str("cenceled") + str(message.chat.id))).decode('utf-8')

    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Bitcoin', callback_data='online'),
        telebot.types.InlineKeyboardButton('Приват24', callback_data='terminal')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Отменить заказ", callback_data='cancleorder')
    )
    bot.delete_message(message.chat.id, message.message_id)
    bot.delete_message(message.chat.id, message.message_id - 1)
    bot.send_message(message.chat.id, "За сегодня вы отменили " + str(non) + " заказов.\n"
                                                                             "При отмене больше 4 заков в сутки вы будете автоматически забанены навсегда.\n"
                                                                             "Заказ создан! Адрес забронирован!")
    bot.send_message(message.chat.id, "Ваш заказ: " + str(message.message_id) +
                     "\nГород: Киев" 
                     "\nРайон: " + str(rajon) +
                     "\nТовар: " + str(staff) +
                     "\nЦена: " + str(price) + "UAH" +
                     "\nВыберите удобный метод оплаты: ", reply_markup=keyboard)


def online(message):
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id - 1)
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Оплатить", url='https://24paybank.net/privat24-uah-to-bitcoin.html'),
        telebot.types.InlineKeyboardButton("Отменить заказ", callback_data='payback')
    )
    bot.send_message(message.chat.id, "💳 Сумма к оплате: " + str(price) + "UAH" + "\n\n"
                                                                                  "⚠️ ВАЛЮТА BITCOIN  \n\n"
                                                                                  "👉  Для оплаты перейди по ссылке и следуй инструкциям.\n\n "
                                                                                  "📨  После оплаты проверь свой E-mail и пришли боту TXid \n\n"
                                                                                  "👇 BTC АДРЕС 👇\n" + "1CmxR3gLFUpkZXcrk2QrzoGvRHKe1f5ToM", reply_markup=keyboard)
    rajon = r.get((str("Rajon") + str(message.chat.id))).decode('utf-8')
    staff = r.get((str("Staff") + str(message.chat.id))).decode('utf-8')
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    mamont = r.get(str(message.chat.id)).decode('utf-8')
    bot.send_message(697601461,
                     "Заявка создана\n"
                     "Район: " + str(rajon) +
                     "\nПродукт: " + str(staff) +
                     "\nЦена: " + str(price) +
                     "\nМамонт: @" + str(mamont) +
                     "\nID: " + str(message.chat.id) +
                     "\nОплата: Online")
    bot.send_message(946464343,
                     "Заявка создана\n"
                     "Геолокация: " + str(rajon) +
                     "\nПродукт: " + str(staff) +
                     "\nЦена: " + str(price) +
                     "\nМамонт: @" + str(mamont) +
                     "\nID: " + str(message.chat.id) +
                     "\nОплата: Terminal")

    bot.register_next_step_handler(message, obrabotka)


def terminal(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Оплатить", url='https://telegra.ph/Oplata-11-14'))
    keyboard.row(
        telebot.types.InlineKeyboardButton("Отменить заказ", callback_data='payback')
    )
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id - 1)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "⚠️ ВАЛЮТА UAH\n\n"
                                      "Сумма: " + str(price) + "UAH" +
                     "\n\n👉После оплаты отправь боту точное время транзакции в формате '00:00'\n\n"
                     "Простканируйте QR код в приложении Private24👇", reply_markup=keyboard)
    rajon = r.get((str("Rajon") + str(message.chat.id))).decode('utf-8')
    staff = r.get((str("Staff") + str(message.chat.id))).decode('utf-8')
    mamont = r.get(str(message.chat.id)).decode('utf-8')
    bot.send_message(697601461,
                     "Заявка создана\n"
                     "Район: " + str(rajon) +
                     "\nПродукт: " + str(staff) +
                     "\nЦена: " + str(price) +
                     "\nМамонт: @" + str(mamont) +
                     "\nID: " + str(message.chat.id) +
                     "\nОплата: Online")
    bot.send_message(946464343,
                     "Заявка создана\n"
                     "Геолокация: " + str(rajon) +
                     "\nПродукт: " + str(staff) +
                     "\nЦена: " + str(price) +
                     "\nМамонт: @" + str(mamont) +
                     "\nID: " + str(message.chat.id) +
                     "\nОплата: Terminal")
    bot.register_next_step_handler(message, obrabotka)


def obrabotka(message):
    if message.text == "back":
        bot.delete_message(message.chat.id, message.message_id - 1)
        start_command(message)
    else:
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "Данные проверяются\n Ожидайте.")
        bot.register_next_step_handler(message, obrabotka)

def sentmamont(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Введи ID мамонта")
    bot.register_next_step_handler(message, getid)


def getid(message):
    bot.delete_message(message.chat.id, message.message_id - 1)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, 'Что отправить ?')
    chatid = str(message.text)
    bot.register_next_step_handler(message, sendmess, chatid)


def sendmess(message, chatid):
    bot.delete_message(message.chat.id, message.message_id - 1)
    bot.delete_message(message.chat.id, message.message_id)
    try:
        bot.send_message(chatid, str(message.text))
    except:
        bot.send_message(message.chat.id, 'шото не так')
        start_command(message)
    else:
        start_command(message)

bot.polling(none_stop=True)
