from random import randint
from parsing_id import sorting_html_code
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re

def gen_link_to_match(id):
    game_id = sorting_html_code()
    game_id = game_id[id][9:]
    url = f"https://www.opendota.com/matches/{game_id}"
    print(url)
    return url

def selenium(url):
    print("Parsing...")
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    try:
        time.sleep(10)
        html_source = driver.page_source

        with open("html_code.txt", "w", encoding='utf-8') as f:
            f.write(html_source)
        f.close()
        print("Html source saved successfully")
    except:
        print("Error")
    finally:
        driver.quit()
    return driver

def get_match_lenght():
    with open("html_code.txt", 'r') as f:
        text = f.read()
        search_id = r"<div><span>\d+:\d+"
        result = re.findall(search_id, text)
        game_time = result[0][11:]
        print(game_time)
    f.close()
    return chr(game_time)

def characters():
    with open("html_code.txt", 'r') as f:
        text = f.read()
        search_id = r"/dota_react/heroes/\w+"
        result = re.findall(search_id, text)
        heroes = list(dict.fromkeys(result))
        print(heroes)
    f.close()
    return heroes

def characters_items():
    pass

def neutral_item():
    with open("html_code.txt", 'r') as f:
        text = f.read()
        search_id = r'<div class="inflictorWithValue neutral" data-tip="true" data-for="....................."><img src="https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/items/\w+'
        neutral_items = re.findall(search_id, text)
        print(neutral_items)
    f.close()
    return neutral_items

def agan_shard():
    with open("html_code.txt", 'r') as f:
        text = f.read()
        search_id = r'data-for="scepter" currentitem="\w+'
        agan = re.findall(search_id, text)
        search_id = r'data-for="shard" currentitem="\w+'
        shard = re.findall(search_id, text)
        print(agan, "\n",  shard)
    f.close()
    return agan,shard

def creating_full_heros_info(heroes, items, neutral, agan, shard):
    heroes_inf = {}
    #{hero, [items], neutral, agan, shard}

#selenium(gen_link_to_match(0))
characters()
agan_shard()
neutral_item()