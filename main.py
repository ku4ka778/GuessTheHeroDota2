import time
from parsing_by_using_id import selenium, creating_full_heroes_info, get_match_length
import os
import json


def creating_match_info(i):
    url = selenium(i)
    games_id = url
    games_id = [games_id[33:] for games_id in games_id]
    games_url = url
    games_time = get_match_length()
    heroes = creating_full_heroes_info()
    games_info= {}
    games_info[games_id[i]] = [games_url[i], games_time, heroes]
    return games_info

def parsing_all_matches():
    data = list()
    for i in range(100):
        data.append(creating_match_info(i))
        os.remove('html_code.txt')
        os.remove('html_code(replaced).txt')
        print(data[i])
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        time.sleep(300)

if __name__ == "__main__":
    while True:
        parsing_all_matches()
