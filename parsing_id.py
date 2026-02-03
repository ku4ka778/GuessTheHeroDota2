import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


def selenium():
    print("Parsing...")
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.opendota.com/matches/highMmr")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)
    html_source = driver.page_source
    with open("html_code.txt", "w", encoding='utf-8') as f:
        f.write(html_source)
    print("Html source saved successfully")
    driver.quit()

def sorting_html_code():
    selenium()
    with open("html_code.txt", 'r') as f:
        text = f.read()
        search_id = r"/matches/\d+"
        result = re.findall(search_id, text)
        games = list(result)
    f.close()
    os.remove("html_code.txt")
    return games

def gen_matches_id():
    game_id = sorting_html_code()
    print(len(game_id), "ready to be parsed")
    game_id = [game_id[9:] for game_id in game_id]
    print(game_id)
    return game_id

def creating_links():
    games_links = list()
    games_id = gen_matches_id()
    for i in range(len(games_id)):
        games_links.append(f"https://www.opendota.com/matches/{games_id[i]}")
    print(games_links)
    return games_links
