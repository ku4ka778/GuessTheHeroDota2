import telebot
from random import randint
import random
from telebot import types
import json
from collections import defaultdict
import time

bot = telebot.TeleBot('8352806479:AAGfL8EmnsbV-RHqHthM_l7lriI25O8e1K8')

user_sessions = defaultdict(lambda: {
    'game_start': 0,
    'game_index': 0,
    'game_round': 0,
    'answer': 0,
    'win': 0,
    'lose': 0
})

games_base = []


def load_games():
    global games_base
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            games_base = json.load(f)
        print(f"Loaded {len(games_base)} games")
    except Exception as e:
        print(f"Error with games_base: {e}")
        games_base = []
    return games_base

load_games()

def game(message):
    load_games()
    user_id = message.from_user.id
    session = user_sessions[user_id]

    if session['game_round'] <= 3:
        if not games_base:
            bot.send_message(message.chat.id, "Саси база игр не загружена")
            return

        if session['game_index'] >= len(games_base):
            bot.send_message(message.chat.id, "Игр нет - иди нахуй и жди")
            return

        game_data = games_base[session['game_index']]
        game_keys = list(game_data.keys())
        game_info = game_data.get(game_keys[0], 'Unknown')

        if game_info[1] != '0:00':
            hero_info = game_info[2]
            heroes = hero_info[0]
            items = hero_info[1]
            num2 = len(heroes) - 1
            rand_num = randint(0, num2)
            session['answer'] = heroes[rand_num]
            hero_items = items[rand_num]
            hero_items_replace = str(hero_items).replace('A', '_')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for i in range(0, len(heroes), 5):
                row = heroes[i:i + 5]
                markup.add(*[types.KeyboardButton(hero) for hero in row])

            print(f"User {user_id}, answer: {session['answer']}")
            bot.send_message(message.chat.id,
                             f"Угадай героя по этим предметам: {hero_items_replace}",
                             reply_markup=markup)
            session['game_start'] = 1
    else:
        session['game_index'] += 1
        session['game_round'] = 0
        session['game_start'] = 0
        start(message)


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("КОММЕНТ ГРЫШКИ ШЫШКИ")
    btn2 = types.KeyboardButton("НАЧАТЬ ИГРАТЬ!!№!№!№!№!!!!№!№!")
    btn3 = types.KeyboardButton("СКОК ИГР ДОСТУПНО")
    btn4 = types.KeyboardButton("ВИНРЕЙТ НАХУ")
    markup.add(btn1, btn2, btn3, btn4)

    welcome_text = (f"КУ!, {message.from_user.first_name}!\n"
                    f"Тк бомж ебучи, вот те калобот для угадывания чаров из доты:)))")

    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

@bot.message_handler(commands=['reset'])
def reset_user(message):
    user_id = message.from_user.id
    user_sessions[user_id] = {
        'game_start': 0,
        'game_index': 0,
        'game_round': 0,
        'answer': 0,
        'win': 0,
        'lose': 0
    }
    bot.send_message(message.chat.id, "Прогресс сброшен КАК МАТЬ С ОКНА ХАХАХАХАХА")


@bot.message_handler(commands=['reload'])
def reload_games(message):
    user_id = message.from_user.id
    if message.from_user.username == "Thashimaotrue":
        load_games()
        bot.send_message(message.chat.id, "Base of games reloaded")
    else:
        bot.send_message(message.chat.id, "Access error")

@bot.message_handler(content_types=['text'])
def func(message):
    user_id = message.from_user.id
    session = user_sessions[user_id]

    if session['game_start'] == 1:
        if message.text == session['answer']:
            bot.send_message(message.chat.id, "🎉 Вау как ты крут как же ты угадал кончи в меня")
            session['win'] += 1
        else:
            bot.send_message(message.chat.id, f"❌ ХАХАХА БЕСТОЛОЧЬ! ОТВЕТ: {session['answer']}")
            session['lose'] += 1

        session['game_round'] += 1
        game(message)

    elif session['game_start'] == 0:
        if message.text == "КОММЕНТ ГРЫШКИ ШЫШКИ":
            bot.send_message(message.chat.id,
                             text="я эту хуйню за 10 часов написал хдхдхдхдхдхдхдхдхд\n"
                                  "В случае багов ИДИ НАХУЙ Я НЕ БУДУ ФИКСИТЬ.\n"
                                  "Кста напиши чет в чат ради смешнявки\n"
                                  "(/reset чтоб заново сыграть, по сути тут рандом модуль и мб ты нью чаров с нью сборками встретишь)\n")

        elif message.text == "НАЧАТЬ ИГРАТЬ!!№!№!№!№!!!!№!№!":
            load_games()
            if session['game_index'] >= len(games_base):
                session['game_index'] = 0
                session['game_round'] = 0

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('НАЗАД НАХУЙ НАЗААААД')
            btn2 = types.KeyboardButton('ВПЕРЕД НАХУЙ ВПЕРЕЕЕЕЕД')
            markup.add(btn1, btn2)

            bot.send_message(message.chat.id, "РЕДИ??", reply_markup=markup)

        elif message.text == 'НАЗАД НАХУЙ НАЗААААД':
            start(message)

        elif message.text == 'ВПЕРЕД НАХУЙ ВПЕРЕЕЕЕЕД':
            load_games()
            if session['game_index'] >= len(games_base):
                bot.send_message(message.chat.id,
                                 'еблан ты уже сыграл дохуя! Иди поспи (чек "СКОК ИГР ДОСТУПНО")')
            else:
                session['game_start'] = 0
                session['game_round'] = 0
                game(message)

        elif message.text == "СКОК ИГР ДОСТУПНО":
            load_games()
            games_left = len(games_base) - session['game_index']
            if games_left < 0:
                games_left = 0
            bot.send_message(message.chat.id,
                             f'{games_left} ЕБАТЬ! (если их 0 - напиши мне или подожди минут 5)')

        elif message.text == "ВИНРЕЙТ НАХУ":
            bot.send_message(message.chat.id,
                             f'правильных: *_{session['win']}_*, НЕПРАВИЛЬНЫХ ОТВЕТОВ АЗЩЫВЗАВЗЩЫА: *_{session['lose']}_*', parse_mode='MarkdownV2')
        else:
            funny_responses = [
                "ИДИ НАХУЙ НЕПИШИ ХУЙНЮ МРАЗЬ",
                "ТЫ ЧЕ ТУПОЙ? НА КНОПКИ ЖМИ!(смешное сообщение нейронки я хз нахуя оно тут но мне понравилось)",
                "НАХУ ТЫ ПИШЕШЬ ЭТО",
                "САСИ ГАВНО",
                "ХРЮХРЮХРЮХРЮРХЮРХР",
                "Хотел бв Чтобы ночью Ко мне пришла Чика Из фнафа И дала съесть Прокладки Исполтщованные Чтобы потом отшлепать меня Газетой за 45 год С новостью о растреле Гитлера Ну Самоубийстве Ты птн Пон И чтобы Параллельно она шепиала Шептала Мне на ухо Что 1к ПТС игроки тоже люди И что я Нормальный игрок Что просто не везёт с командрй"
            ]
            bot.send_message(message.chat.id, text=random.choice(funny_responses))


if __name__ == '__main__':
    print("Bot ready to work")
    bot.infinity_polling()
    
