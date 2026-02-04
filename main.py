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
            json_file.write("\n")
            print(f"Dictionary {i} successfully  saved to data.json")
        json_file.close()
        os.remove('html_code.txt')
        os.remove('html_code(replaced).txt')
        time.sleep(120)

def auto_git_push(repo_path, commit_message):
    try:
        repo = git.Repo(repo_path)
        repo.git.add(update=True)
        repo.index.commit(commit_message)
        origin = repo.remote(name='origin')
        origin.push()
        print('Successfully added, committed, and pushed changes.')
    except Exception as e:
        print(f'Error: {e}')

def timer():
    total_minutes = 600
    while total_minutes > 0:
        print(f"{total_minutes} minutes left")
        total_minutes -= 1
        time.sleep(60)
    print("The hour is over")

if __name__ == "__main__":
    while True:
        parsing_all_matches()
        timer()
        auto_git_push(REPO_DIR, COMMIT_MESSAGE)
