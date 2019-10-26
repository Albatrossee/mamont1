import telebot
from emoji import emojize
import  redis
from redis import StrictRedis
r = redis.from_url('redis://h:pc31dfa87bd081058099cf9822fb3f008108e69b45b00998978db346fd936b190@ec2-52-51-17-151.eu-west-1.compute.amazonaws.com:29109')

TOKEN = '1027125386:AAGJEha1Q6NJcKn2g8XMc8gDZpDd7OOqub4'
bot = telebot.TeleBot(TOKEN)
value = 0
price = 0
cenceled = 0

mushroom = emojize(":mushroom:", use_aliases=True)
snowflake = emojize(":snowflake:", use_aliases=True)
lemon = emojize(":lemon:", use_aliases=True)
heart = emojize(":heart:", use_aliases=True)






@bot.message_handler(commands=['start'])
def start_command(message):
    if (cenceled == 0):
        print(message.message_id)
        bot.delete_message(message.chat.id, message.message_id)
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Варшава', callback_data='Warsaw'),
            telebot.types.InlineKeyboardButton('Краков', callback_data='Krakow')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Гданськ', callback_data='Gdansk'),
            telebot.types.InlineKeyboardButton('Лодзь', callback_data='Lodz')
        )

        bot.send_message(
            message.chat.id,
            'Приветствуем в магазине: "Две дороги"\n'+
            'Две дороги", а какую выберешь ты ?"\n'+
            'Оператор: @dve_dorogi_supp\n',
            reply_markup=keyboard
        )
    else:
        non = r.get((str("cenceled") + str(message.chat.id))).decode('utf-8')
        if(non == str(5)):
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(message.chat.id, "Хорошая попытка.")
        else:
            print(message.message_id)
            bot.delete_message(message.chat.id, message.message_id)
            keyboard = telebot.types.InlineKeyboardMarkup()
            keyboard.row(
                telebot.types.InlineKeyboardButton('Варшава', callback_data='Warsaw'),
                telebot.types.InlineKeyboardButton('Краков', callback_data='Krakow')
            )
            keyboard.row(
                telebot.types.InlineKeyboardButton('Гданськ', callback_data='Gdansk'),
                telebot.types.InlineKeyboardButton('Лодзь', callback_data='Lodz')
            )

            bot.send_message(
                message.chat.id,
                'Приветствуем Вас в магазине HUJ.\n' +
                'Оператор: @dve_dorogi_supp\n'
                '',
                reply_markup=keyboard
            )





@bot.message_handler(content_types=['text'])
def dellmess(message):
    bot.delete_message(message.chat.id, message.message_id - 1)
    if (cenceled == 0):
        non = r.set((str("cenceled") + str(message.chat.id)), 1)
        cenpluse(message)
        start_command(message)
    else:
        r.incr((str("cenceled") + str(message.chat.id)), 1)
        non = r.get((str("cenceled") + str(message.chat.id))).decode('utf-8')
        if(non == str(5)):
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(message.chat.id, "Вы забанены!!!")
            bot.register_next_step_handler(message, antiban)
        else:
            start_command(message)

def antiban(message):
    if(message.text == 'antiban'):
        r.set((str("cenceled") + str(message.chat.id)), int(0))
        cenceled = 0
        start_command(message)
    else:
        bot.send_message(message.chat.id, "Вы забанены!!!")
        bot.register_next_step_handler(message, antiban)




def cenpluse(message):
    global cenceled
    cenceled += 1


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
    if data.startswith('Krakow'):
        bot.answer_callback_query(query.id)
        city = "Краков"
        krakow(query.message)
    if data.startswith('Gdansk'):
        bot.answer_callback_query(query.id)
        city = "Гданьск"
        gdansk(query.message)
    if data.startswith('Lodz'):
        bot.answer_callback_query(query.id)
        city = "Лодзь"
        lodz(query.message)
    if data.startswith('getBack'):
        bot.answer_callback_query(query.id)
        start_command(query.message)
    if data.startswith('getBack2'):
        bot.answer_callback_query(query.id)
        dellmess(query.message)
    if data.startswith('cancleorder'):
        bot.answer_callback_query(query.id)
        dellmess(query.message)
    if data.startswith('online'):
        bot.answer_callback_query(query.id)
        online(query.message)
    if data.startswith('terminal'):
        bot.answer_callback_query(query.id)
        terminal(query.message)

    if data.startswith('amf1'):
        bot.answer_callback_query(query.id)
        r.set((str("Staff") + str(query.message.chat.id)), "Амф 1г")
        r.set((str("Price") + str(query.message.chat.id)), "60")
        amf1(query.message)
    if data.startswith('amf2'):
        bot.answer_callback_query(query.id)
        r.set((str("Staff") + str(query.message.chat.id)), "Амф 2г")
        r.set((str("Price") + str(query.message.chat.id)), "110")
        amf2(query.message)
    if data.startswith('weed1'):
        bot.answer_callback_query(query.id)
        r.set((str("Staff") + str(query.message.chat.id)), "Шишки 1г")
        r.set((str("Price") + str(query.message.chat.id)), "50")
        weed1(query.message)
    if data.startswith('weed2'):
        bot.answer_callback_query(query.id)
        r.set((str("Staff") + str(query.message.chat.id)), "Шишки 2г")
        r.set((str("Price") + str(query.message.chat.id)), "90")
        weed2(query.message)
    if data.startswith('mef1'):
        bot.answer_callback_query(query.id)
        r.set((str("Staff") + str(query.message.chat.id)), "Мефедрон 1г")
        r.set((str("Price") + str(query.message.chat.id)), "90")
        mef1(query.message)
    if data.startswith('mef2'):
        bot.answer_callback_query(query.id)
        r.set((str("Staff") + str(query.message.chat.id)), "Мефедрон 2г")
        r.set((str("Price") + str(query.message.chat.id)), "160")
        mef2(query.message)
    if data.startswith('mushrooms1'):
        bot.answer_callback_query(query.id)
        r.set((str("Staff") + str(query.message.chat.id)), "Грибы 3г")
        r.set((str("Price") + str(query.message.chat.id)), "100")
        mushrooms1(query.message)
    if data.startswith('mushrooms2'):
        bot.answer_callback_query(query.id)
        r.set((str("Staff") + str(query.message.chat.id)), "Грибы 6г")
        r.set((str("Price") + str(query.message.chat.id)), "200")
        mushrooms2(query.message)



    if data.startswith('wola'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Воля")
        rajonwars(query.message)
    if data.startswith('praga'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Прага")
        rajonwars(query.message)
    if data.startswith('centrum'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Центрум")
        rajonwars(query.message)
    if data.startswith('mokotow'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Мокотов")
        rajonwars(query.message)


    if data.startswith('Grzegorzki'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Grzegorzki")
        rajonwars(query.message)
    if data.startswith('Stare'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Stare miasto")
        rajonwars(query.message)
    if data.startswith('Podgorze'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Podgorze")
        rajonwars(query.message)
    if data.startswith('Czyzyny'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Czyzyny")
        rajonwars(query.message)


    if data.startswith('Przymorze'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Przymorze")
        rajonwars(query.message)
    if data.startswith('Wrzeszcz'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Wrzeszcz")
        rajonwars(query.message)
    if data.startswith('Oliwa'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Oliwa")
        rajonwars(query.message)




    if data.startswith('Srodmiescie'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Srodmiescie")
        rajonwars(query.message)
    if data.startswith('Polesie'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Polesie")
        rajonwars(query.message)
    if data.startswith('Widziew'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Widziew")
        rajonwars(query.message)
    if data.startswith('Gorna'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Gorna")
        rajonwars(query.message)
    if data.startswith('Baluty'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Baluty")
        rajonwars(query.message)




def warszawa(message):
    r.set(message.chat.id, "Варшава")
    bot.delete_message(message.chat.id, message.message_id)
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
        telebot.types.InlineKeyboardButton(heart + 'Mеф 1г', callback_data='mef1'),
        telebot.types.InlineKeyboardButton(heart + 'Mеф 2г', callback_data='mef2')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(mushroom + 'Грибы 3г', callback_data='mushrooms1'),
        telebot.types.InlineKeyboardButton(mushroom + 'Грибы 6г', callback_data='mushrooms2')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Назад', callback_data='getBack')
    )
    bot.send_photo(message.chat.id, 'https://34travel.me/media/posts/5d556a4d41e0d-wawa-pan.jpg',
    reply_markup=keyboard)

def krakow(message):
    bot.delete_message(message.chat.id, message.message_id)
    r.set(message.chat.id, "Краков")
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
        telebot.types.InlineKeyboardButton(heart + 'Mеф 1г', callback_data='mef1'),
        telebot.types.InlineKeyboardButton(heart + 'Mеф 2г', callback_data='mef2')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(mushroom + 'Грибы 3г', callback_data='mushrooms1'),
        telebot.types.InlineKeyboardButton(mushroom + 'Грибы 6г', callback_data='mushrooms2')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Назад', callback_data='getBack')
    )
    bot.send_photo(message.chat.id, 'https://traveller-eu.ru/sites/default/files/inline-images/krakow3.jpg',



    reply_markup=keyboard)

def gdansk(message):
    bot.delete_message(message.chat.id, message.message_id)
    r.set(message.chat.id, "Гданськ")
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
        telebot.types.InlineKeyboardButton(heart + 'Mеф 1г', callback_data='mef1'),
        telebot.types.InlineKeyboardButton(heart + 'Mеф 2г', callback_data='mef2')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(mushroom + 'Грибы 3г', callback_data='mushrooms1'),
        telebot.types.InlineKeyboardButton(mushroom + 'Грибы 6г', callback_data='mushrooms2')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Назад', callback_data='getBack')
    )
    bot.send_photo(message.chat.id, 'https://www.moyaeuropa.com.ua/wp-content/uploads/2015/06/Gdansk-%D0%93%D0%B4%D0%B0%D0%BD%D1%81%D1%8C%D0%BA-%D0%BF%D0%B0%D0%BD%D0%BE%D1%80%D0%B0%D0%BC%D0%B0-%D0%BD%D0%B0%D0%B1%D0%B5%D1%80%D0%B5%D0%B6%D0%BD%D0%BE%D1%97-1024x707.jpg',

    reply_markup=keyboard)

def lodz(message):
    bot.delete_message(message.chat.id, message.message_id)
    r.set(message.chat.id, "Лодзь")
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
        telebot.types.InlineKeyboardButton(heart + 'Mеф 1г', callback_data='mef1'),
        telebot.types.InlineKeyboardButton(heart + 'Mеф 2г', callback_data='mef2')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(mushroom + 'Грибы 3г', callback_data='mushrooms1'),
        telebot.types.InlineKeyboardButton(mushroom + 'Грибы 6г', callback_data='mushrooms2')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Назад', callback_data='getBack')
    )
    bot.send_photo(message.chat.id, 'https://34travel.me/media/posts/5c654b28a04f3-lodz-pan.jpg',



    reply_markup=keyboard)


def amf1(message):
    city = r.get(message.chat.id).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    if(city == 'Варшава'):
        keyboard.row(
        telebot.types.InlineKeyboardButton('Wola', callback_data='wola'),
        telebot.types.InlineKeyboardButton('Praga', callback_data='praga')
    )
        keyboard.row(
        telebot.types.InlineKeyboardButton('Mokotow', callback_data='mokotow'),
        telebot.types.InlineKeyboardButton('Centrum', callback_data='centrum')
    )
        keyboard.row(
        telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
    )
    if (city == "Краков"):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Grzegorzki', callback_data='Grzegorzki'),
            telebot.types.InlineKeyboardButton('Stare miasto', callback_data='Stare')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Podgorze', callback_data='Podgorze'),
            telebot.types.InlineKeyboardButton('Czyzyny', callback_data='Czyzyny')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    if (city == "Гданськ"):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Przymorze', callback_data='Przymorze')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Wrzeszcz', callback_data='Wrzeszcz'),
            telebot.types.InlineKeyboardButton('Oliwa', callback_data='Oliwa')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    if (city == "Лодзь"):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Srodmiescie', callback_data='Srodmiescie'),
            telebot.types.InlineKeyboardButton('Polesie', callback_data='Polesie')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Widziew', callback_data='Widziew'),
            telebot.types.InlineKeyboardButton('Gorna', callback_data='Gorna')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Baluty', callback_data='Baluty')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )


    bot.send_photo(message.chat.id,'https://antikor.com.ua/foto/articles_foto/2018/11/18/270228.jpg')
    bot.send_message(message.chat.id, "Избран продукт: Амф HQ 1g.\n" +
                                    'Коротко о товаре: Амфетамин Hight quality\n' +
                                    'Цена: 60zl.\n' +
                                    'Выберите подходящий район:',



    reply_markup=keyboard)

def amf2(message):
    city = r.get(message.chat.id).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    price = 100
    if (city == "Варшава"):
        keyboard.row(
        telebot.types.InlineKeyboardButton('Wola', callback_data='wola'),
        telebot.types.InlineKeyboardButton('Praga', callback_data='praga')
    )
        keyboard.row(
        telebot.types.InlineKeyboardButton('Mokotow', callback_data='mokotow'),
        telebot.types.InlineKeyboardButton('Centrum', callback_data='centrum')
    )
        keyboard.row(
        telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
    )
    if (city == "Краков"):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Grzegorzki', callback_data='Grzegorzki'),
            telebot.types.InlineKeyboardButton('Stare miasto', callback_data='Stare')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Podgorze', callback_data='Podgorze'),
            telebot.types.InlineKeyboardButton('Czyzyny', callback_data='Czyzyny')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    if (city == "Гданськ"):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Przymorze', callback_data='Przymorze')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Wrzeszcz', callback_data='Wrzeszcz'),
            telebot.types.InlineKeyboardButton('Oliwa', callback_data='Oliwa')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    if (city == "Лодзь"):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Srodmiescie', callback_data='Srodmiescie'),
            telebot.types.InlineKeyboardButton('Polesie', callback_data='Polesie')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Widziew', callback_data='Widziew'),
            telebot.types.InlineKeyboardButton('Gorna', callback_data='Gorna')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Baluty', callback_data='Baluty')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    bot.send_photo(message.chat.id,'https://antikor.com.ua/foto/articles_foto/2018/11/18/270228.jpg')
    bot.send_message(message.chat.id, "Избран продукт: Амф HQ 2g.\n" +
                                    'Коротко о товаре: Амфетамин Hight quality\n' +
                                    'Цена: 100zl\n' +
                                    'Выберите подходящий район:',



    reply_markup=keyboard)


def weed1(message):
    city = r.get(message.chat.id).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    if (city == "Варшава"):
        keyboard.row(
        telebot.types.InlineKeyboardButton('Wola', callback_data='wola'),
        telebot.types.InlineKeyboardButton('Praga', callback_data='praga')
    )
        keyboard.row(
        telebot.types.InlineKeyboardButton('Mokotow', callback_data='mokotow'),
        telebot.types.InlineKeyboardButton('Centrum', callback_data='centrum')
    )
        keyboard.row(
        telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
    )
    if(city == "Краков"):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Grzegorzki', callback_data='Grzegorzki'),
            telebot.types.InlineKeyboardButton('Stare miasto', callback_data='Stare')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Podgorze', callback_data='Podgorze'),
            telebot.types.InlineKeyboardButton('Czyzyny', callback_data='Czyzyny')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    if (city == "Гданськ"):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Przymorze', callback_data='Przymorze')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Wrzeszcz', callback_data='Wrzeszcz'),
            telebot.types.InlineKeyboardButton('Oliwa', callback_data='Oliwa')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    if (city == "Лодзь"):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Srodmiescie', callback_data='Srodmiescie'),
            telebot.types.InlineKeyboardButton('Polesie', callback_data='Polesie')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Widziew', callback_data='Widziew'),
            telebot.types.InlineKeyboardButton('Gorna', callback_data='Gorna')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Baluty', callback_data='Baluty')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )


    bot.send_photo(message.chat.id,'https://hs420.net/uploads/monthly_2017_11/1.jpg.022ec99a1f3e7f5d13727754b3ea59cb.jpg')
    bot.send_message(message.chat.id, "Избран продукт: Шишки 1g.\n" +
                                    'Коротко о товаре: Шишки LH\n' +
                                    'Цена: 50zl.\n' +
                                    'Выберите подходящий район:',



    reply_markup=keyboard)


def weed2(message):
    city = r.get(message.chat.id).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    price = 90
    if (city == "Варшава"):
        keyboard.row(
        telebot.types.InlineKeyboardButton('Wola', callback_data='wola'),
        telebot.types.InlineKeyboardButton('Praga', callback_data='praga')
    )
        keyboard.row(
        telebot.types.InlineKeyboardButton('Mokotow', callback_data='mokotow'),
        telebot.types.InlineKeyboardButton('Centrum', callback_data='centrum')
    )
        keyboard.row(
        telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
    )
    if (city == "Краков"):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Grzegorzki', callback_data='Grzegorzki'),
            telebot.types.InlineKeyboardButton('Stare miasto', callback_data='Stare')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Podgorze', callback_data='Podgorze'),
            telebot.types.InlineKeyboardButton('Czyzyny', callback_data='Czyzyny')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    if (city == "Гданськ"):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Przymorze', callback_data='Przymorze')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Wrzeszcz', callback_data='Wrzeszcz'),
            telebot.types.InlineKeyboardButton('Oliwa', callback_data='Oliwa')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    if (city == "Лодзь"):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Srodmiescie', callback_data='Srodmiescie'),
            telebot.types.InlineKeyboardButton('Polesie', callback_data='Polesie')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Widziew', callback_data='Widziew'),
            telebot.types.InlineKeyboardButton('Gorna', callback_data='Gorna')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Baluty', callback_data='Baluty')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    bot.send_photo(message.chat.id,'https://hs420.net/uploads/monthly_2017_11/1.jpg.022ec99a1f3e7f5d13727754b3ea59cb.jpg')
    bot.send_message(message.chat.id, "Избран продукт: Шишки 2g.\n" +
                                    'Коротко о товаре: Шишки LH\n' +
                                    'Цена: 90zl\n' +
                                    'Выберите подходящий район:',



    reply_markup=keyboard)

def mef1(message):
    city = r.get(message.chat.id).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    price = 90
    if (city == "Варшава"):
        keyboard.row(
        telebot.types.InlineKeyboardButton('Wola', callback_data='wola'),
        telebot.types.InlineKeyboardButton('Praga', callback_data='praga')
    )
        keyboard.row(
        telebot.types.InlineKeyboardButton('Mokotow', callback_data='mokotow'),
        telebot.types.InlineKeyboardButton('Centrum', callback_data='centrum')
    )
        keyboard.row(
        telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
    )
    if (city == "Краков"):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Grzegorzki', callback_data='Grzegorzki'),
            telebot.types.InlineKeyboardButton('Stare miasto', callback_data='Stare')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Podgorze', callback_data='Podgorze'),
            telebot.types.InlineKeyboardButton('Czyzyny', callback_data='Czyzyny')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    if (city == "Гданськ"):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Przymorze', callback_data='Przymorze')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Wrzeszcz', callback_data='Wrzeszcz'),
            telebot.types.InlineKeyboardButton('Oliwa', callback_data='Oliwa')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    if (city == "Лодзь"):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Srodmiescie', callback_data='Srodmiescie'),
            telebot.types.InlineKeyboardButton('Polesie', callback_data='Polesie')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Widziew', callback_data='Widziew'),
            telebot.types.InlineKeyboardButton('Gorna', callback_data='Gorna')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Baluty', callback_data='Baluty')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    bot.send_photo(message.chat.id,'https://miro.medium.com/max/475/1*jm2CYN1-aAUXXalCOtjZYA.jpeg')
    bot.send_message(message.chat.id, "Избран продукт: Мефедрон HQ 1g.\n" +
                                    'Коротко о товаре: Мефедрон Hight quality\n' +
                                    'Цена: 90zl\n' +
                                    'Выберите подходящий район:',



    reply_markup=keyboard)


def mef2(message):
    city = r.get(message.chat.id).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    price = 160
    if (city == "Варшава"):
        keyboard.row(
        telebot.types.InlineKeyboardButton('Wola', callback_data='wola'),
        telebot.types.InlineKeyboardButton('Praga', callback_data='praga')
    )
        keyboard.row(
        telebot.types.InlineKeyboardButton('Mokotow', callback_data='mokotow'),
        telebot.types.InlineKeyboardButton('Centrum', callback_data='centrum')
    )
        keyboard.row(
        telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
    )
    if (city == "Краков"):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Grzegorzki', callback_data='Grzegorzki'),
            telebot.types.InlineKeyboardButton('Stare miasto', callback_data='Stare')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Podgorze', callback_data='Podgorze'),
            telebot.types.InlineKeyboardButton('Czyzyny', callback_data='Czyzyny')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    if (city == "Гданськ"):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Przymorze', callback_data='Przymorze')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Wrzeszcz', callback_data='Wrzeszcz'),
            telebot.types.InlineKeyboardButton('Oliwa', callback_data='Oliwa')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    if (city == "Лодзь"):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Srodmiescie', callback_data='Srodmiescie'),
            telebot.types.InlineKeyboardButton('Polesie', callback_data='Polesie')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Widziew', callback_data='Widziew'),
            telebot.types.InlineKeyboardButton('Gorna', callback_data='Gorna')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Baluty', callback_data='Baluty')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    bot.send_photo(message.chat.id,'https://miro.medium.com/max/475/1*jm2CYN1-aAUXXalCOtjZYA.jpeg')
    bot.send_message(message.chat.id, "Избран продукт: Мефедрон HQ 2g.\n" +
                                    'Коротко о товаре: Мефедрон Hight quality\n' +
                                    'Цена: 160zl\n' +
                                    'Выберите подходящий район:',
    reply_markup=keyboard)

def mushrooms1(message):
    city = r.get(message.chat.id).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    price = 160
    if (city == "Варшава"):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Wola', callback_data='wola'),
            telebot.types.InlineKeyboardButton('Praga', callback_data='praga')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Mokotow', callback_data='mokotow'),
            telebot.types.InlineKeyboardButton('Centrum', callback_data='centrum')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    if (city == "Краков"):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Grzegorzki', callback_data='Grzegorzki'),
            telebot.types.InlineKeyboardButton('Stare miasto', callback_data='Stare')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Podgorze', callback_data='Podgorze'),
            telebot.types.InlineKeyboardButton('Czyzyny', callback_data='Czyzyny')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    if (city == "Гданськ"):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Przymorze', callback_data='Przymorze')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Wrzeszcz', callback_data='Wrzeszcz'),
            telebot.types.InlineKeyboardButton('Oliwa', callback_data='Oliwa')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    if (city == "Лодзь"):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Srodmiescie', callback_data='Srodmiescie'),
            telebot.types.InlineKeyboardButton('Polesie', callback_data='Polesie')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Widziew', callback_data='Widziew'),
            telebot.types.InlineKeyboardButton('Gorna', callback_data='Gorna')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Baluty', callback_data='Baluty')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    bot.send_photo(message.chat.id, 'http://chemistry-chemists.com/N2_2012/S1/psilocybe_semilanceata-3a.JPG')
    bot.send_message(message.chat.id, "Избран продукт: Грибы 3g.\n" +
                     'Коротко о товаре: Грибы псилоцибиновые\n' +
                     'Цена: 100zl\n' +
                     'Выберите подходящий район:',
    reply_markup=keyboard)

def mushrooms2(message):
    city = r.get(message.chat.id).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    price = 160
    if (city == "Варшава"):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Wola', callback_data='wola'),
            telebot.types.InlineKeyboardButton('Praga', callback_data='praga')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Mokotow', callback_data='mokotow'),
            telebot.types.InlineKeyboardButton('Centrum', callback_data='centrum')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    if (city == "Краков"):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Grzegorzki', callback_data='Grzegorzki'),
            telebot.types.InlineKeyboardButton('Stare miasto', callback_data='Stare')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Podgorze', callback_data='Podgorze'),
            telebot.types.InlineKeyboardButton('Czyzyny', callback_data='Czyzyny')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    if (city == "Гданськ"):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Przymorze', callback_data='Przymorze')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Wrzeszcz', callback_data='Wrzeszcz'),
            telebot.types.InlineKeyboardButton('Oliwa', callback_data='Oliwa')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    if (city == "Лодзь"):
        keyboard.row(
            telebot.types.InlineKeyboardButton('Srodmiescie', callback_data='Srodmiescie'),
            telebot.types.InlineKeyboardButton('Polesie', callback_data='Polesie')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Widziew', callback_data='Widziew'),
            telebot.types.InlineKeyboardButton('Gorna', callback_data='Gorna')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Baluty', callback_data='Baluty')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='getBack2')
        )
    bot.send_photo(message.chat.id, 'http://chemistry-chemists.com/N2_2012/S1/psilocybe_semilanceata-3a.JPG')
    bot.send_message(message.chat.id, "Избран продукт: Грибы 6g.\n" +
                     'Коротко о товаре: Грибы псилоцибиновые\n' +
                     'Цена: 200zl\n' +
                     'Выберите подходящий район:',
    reply_markup=keyboard)





def rajonwars(message):
    city  = r.get(message.chat.id).decode('utf-8')
    rajon = r.get((str("Rajon") + str(message.chat.id))).decode('utf-8')
    staff = r.get((str("Staff") + str(message.chat.id))).decode('utf-8')
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    if(cenceled == 0):
        non = 0
    else:
        non = r.get((str("cenceled") + str(message.chat.id))).decode('utf-8')
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('ON-LINE', callback_data='online'),
    telebot.types.InlineKeyboardButton('ТЕРМИНАЛ', callback_data='terminal')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Отменить заказ", callback_data='cancleorder')
    )
    bot.delete_message(message.chat.id, message.message_id)
    bot.delete_message(message.chat.id, message.message_id - 1)
    bot.send_message(message.chat.id,"За сегодня вы отменили " + str(non) + " заказов.\n"
                                    "При отмене больше 4 заков в сутки вы будете автоматически забанены навсегда.\n"
                                      "Заказ создан! Адрес забронирован!")
    bot.send_message(message.chat.id, "Ваш заказ: " + str(message.message_id) +
                         "\nГород: " + str(city) +
                            "\nРайон: " + str(rajon) +
                            "\nТовар: " + str(staff) +
                            "\nЦена: "  + str(price) + "zl"
                     "\nВыберите удобный метод оплаты:",

    reply_markup=keyboard)


def online(message):
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id - 1)
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Назад', callback_data='getBack')
    )
    bot.send_message(message.chat.id, "💳 Сумма к оплате: " + str(price) + "zl" + "\n\n"
                                      "⚠️ ВАЛЮТА BITCOIN  \n\n"
                                      "👉  Для оплаты перейди по ссылке и следуй инструкциям.\n\n "
                                      "🔗 4coins.pl (https://www.4coins.pl/ru/)\n\n"
                                      "⚠️ УБЕРИ галочку \n"
                                      "(☑️ Выплата на мой кошелек\n)"
                                      "Для того что бы появилось поле для ввода BTC адреса указанного ниже.\n\n"
                                      "📨  После оплаты проверь свой E-mail и пришли мне TXid \n\n"
                                      "👇 BTC АДРЕС 👇")
    bot.send_message(message.chat.id, 'bc1qgyxa9avxagxr752qkmfz3uzsc34cjz04ny8ayw')
    bot.register_next_step_handler(message, obrabotka)

def terminal(message):
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id - 1)
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Назад', callback_data='getBack')
    )
    bot.send_message(message.chat.id, "⚠️ ВАЛЮТА BTC\n\n"
                                      "Сумма: " + str(price) + "zl" +
                                      "\n\n👉 Инструкция оплаты (https://telegra.ph/OPLATA-10-21)\n\n"
                                      "👇 После оплаты отправь время\n\n")
    bot.register_next_step_handler(message, obrabotka)


def obrabotka(message):
    if(message.text == "back"):
        bot.delete_message(message.chat.id, message.message_id - 2)
        bot.delete_message(message.chat.id, message.message_id - 1)
        start_command(message)
    else:
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "Ваш ответ был выслан на проверку.\n Ожидайте!!!")
        bot.register_next_step_handler(message, obrabotka)






bot.polling(none_stop=True)
