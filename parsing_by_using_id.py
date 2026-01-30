from random import randint
from parsing_id import sorting_html_code

def gen_link_to_match():
    game_id = sorting_html_code()
    id = randint(0,len(game_id))
    game_id = game_id[id][9:]
    url = f"https://www.opendota.com/matches/{game_id}"
    print(url)



def parse_html():
    pass

def choose_character():
    pass

def get_character_items():
    pass

def get_match_lenght():
    pass

gen_link_to_match()