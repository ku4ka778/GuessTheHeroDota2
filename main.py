import time
from parsing_by_using_id import selenium, creating_full_heroes_info, get_match_length
import json
import os
import git

REPO_DIR = 'C:/Users/unki/PycharmProjects/GuessTheHeroDota2'
COMMIT_MESSAGE = 'Added_New_Matches'

def creating_match_info(i):
    url = selenium(i)
    games_id = url
    games_id = [games_id[33:] for games_id in games_id]
    games_url = url
    games_time = get_match_length()
    heroes = creating_full_heroes_info()
    games_info= {}
    games_info[games_id[i]] = [games_url[i], games_time, heroes]
    print(games_info)
    return games_info

def parsing_all_matches():
    for i in range(100):
        with open('data.json', 'a') as json_file:
            data = creating_match_info(i)
            json.dump(data, json_file, indent=4)
            print(f"Dictionary {i} successfully  saved to data.json")
        json_file.close()
        os.remove('html_code.txt')
        os.remove('html_code(replaced).txt')
        time.sleep(120)

if __name__ == "__main__":
    while True:
        parsing_all_matches()

