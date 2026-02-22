import telebot
from random import randint
from telebot import types
import json

bot = telebot.TeleBot('8352806479:AAGfL8EmnsbV-RHqHthM_l7lriI25O8e1K8')
games_base = dict()

game_start = 0
game_index = 0
game_round = 0
answer = 0
def Parsing():
    with open('data.json', 'r', encoding='utf-8') as f:
        games_base = json.load(f)
        print(games_base)
    return games_base

def game(message):
    global game_index
    global game_round
    global game_start
    global answer
    if game_round <= 3:
        games_base = Parsing()
        game = games_base[game_index]
        game_keys = list(game.keys())
        game_info = game.get(game_keys[0], 'Unknown')
        if game_info[1] != '0:00':
            hero_info = game_info[2]
            heroes = hero_info[0]
            items = hero_info[1]
            num2 = len(heroes) - 1
            rand_num = randint(0, num2)
            answer = heroes[rand_num]
            hero_items = items[rand_num]
            hero_items_replace = str(hero_items)
            hero_items_replace = hero_items_replace.replace('A', '_')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton(heroes[0])
            btn2 = types.KeyboardButton(heroes[1])
            btn3 = types.KeyboardButton(heroes[2])
            btn4 = types.KeyboardButton(heroes[3])
            btn5 = types.KeyboardButton(heroes[4])
            btn6 = types.KeyboardButton(heroes[5])
            btn7 = types.KeyboardButton(heroes[6])
            btn8 = types.KeyboardButton(heroes[7])
            btn9 = types.KeyboardButton(heroes[8])
            btn10 = types.KeyboardButton(heroes[9])
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
            print(f"Ответ {answer}")
            bot.send_message(message.chat.id, f"Угадай героя по этим предметам: {hero_items_replace}".format(message.from_user),reply_markup=markup)
            game_start = 1
    else:
        game_index+=1
        game_round=0
        start(message)
        game_start = 0
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("КОММЕНТ ГРЫШКИ ШЫШКИ")
    btn2 = types.KeyboardButton("НАЧАТЬ ИГРАТЬ!!№!№!№!№!!!!№!№!")
    btn3 = types.KeyboardButton("СКОК ИГР ДОСТУПНО")
    markup.add(btn1, btn2,btn3)
    bot.send_message(message.chat.id, f"КУ!, {message.from_user.first_name} Т.к я бомж ебучи вот те калобот для угадывания чаров из доты:)))DSFKLSD:FSDJKLFASHFJSAFASFKJSAGFASGFk".format(message.from_user),reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    global answer
    global game_round
    global game_start
    if game_start == 1:
        if message.text == answer:
            bot.send_message(message.chat.id, "Вау как ты крут как же ты угадал кончи в меня")
        else:
            bot.send_message(message.chat.id, f"ХАХАХА БЕСТОЛОЧЬ! ОТВЕТ:{answer}")
        game_round +=1
        game(message)
    elif game_start == 0:
        if (message.text == "КОММЕНТ ГРЫШКИ ШЫШКИ"):
            bot.send_message(message.chat.id, text="я эту хуйню за 10 часов написал хдхдхдхдхдхдхдхдхд В случае багов ИДИ НАХУЙ Я НЕ БУДУ ФИКСИТЬ. Кста напиши чет в чат ради смешнявки")
        elif (message.text == "НАЧАТЬ ИГРАТЬ!!№!№!№!№!!!!№!№!"):
            markup = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, "Все доступные игры начнутся нескончаемым потоком", reply_markup=markup)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('НАЗАД НАХУЙ НАЗААААД')
            btn2 = types.KeyboardButton('ВПЕРЕД НАХУЙ ВПЕРЕЕЕЕЕД')
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, "РЕДИ??", reply_markup=markup)
        elif (message.text == 'НАЗАД НАХУЙ НАЗААААД'):
                start(message)
        elif (message.text == 'ВПЕРЕД НАХУЙ ВПЕРЕЕЕЕЕД'):
            if len(Parsing())-game_index == 0:
                bot.send_message(message.chat.id, 'еблан ты уже сыграл дохуя иди поспи(чек скок игр доступно')
            else:
                game(message)
        elif (message.text == "СКОК ИГР ДОСТУПНО"):
            bot.send_message(message.chat.id, f'{len(Parsing())-game_index} ЕБАТЬ!(если их 0 - напиши мне или подожди минут 5)')
        else:
            bot.send_message(message.chat.id, text="ИДИ НАХУЙ НЕПИШИ ХУЙНЮ МРАЗЬ")


bot.infinity_polling()
