from random import randint
from parsing_id import sorting_html_code
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
import shutil
import os

def gen_link_to_match(id):
    game_id = sorting_html_code()
    print(len(game_id), "ready to be parsed")
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
    return game_time

def characters():
    with open("html_code.txt", 'r') as f:
        text = f.read()
        search_id = r"/dota_react/heroes/\w+"
        result = re.findall(search_id, text)
        heroes = list(dict.fromkeys(result))
        heroes = [heroes[19:] for heroes in heroes]
        print(heroes)
    f.close()
    return heroes

def characters_items():
    shutil.copy("html_code.txt", "html_code(replaced).txt")
    items = list()
    with open("html_code(replaced).txt", 'r') as f:
        filedata = f.read()
        filedata = filedata.replace("_", "A")
        f.close()
    with open("html_code(replaced).txt", 'w') as f:
        f.write(filedata)
    f.close()
    with open("html_code(replaced).txt", 'r') as f:
        updated = filedata.replace('.png" alt="" height="27px" width="37px"><div class="tooltip">',"")
    f.close()
    with open("html_code(replaced).txt", 'w') as f:
        f.write(updated)
    f.close()
    found_lines = []
    with open("html_code(replaced).txt", 'r') as file:
        for line in file:
            if '<div class="sc-tilXH gfboHN">' in line:
                found_lines.append(line.strip())
    for y in range(10):
        search_id = r'<div class="inflictorWithValue " data-tip="true" data-for="....................."><img src="https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dotaAreact/items/\w+'
        text = found_lines[y]
        item = re.findall(search_id, text)
        while len(item) > 6:
            item.pop()
        item = [item[166:] for item in item]
        items.append(item)

    for i in range(len(items)):
        items = str(items)
        items = items.replace('A', '_')
    print(items)
    return items

def neutral_item():
    with open("html_code.txt", 'r') as f:
        text = f.read()
        search_id = r'<div class="inflictorWithValue neutral" data-tip="true" data-for="....................."><img src="https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/items/\w+'
        neutral_items = re.findall(search_id, text)
        neutral_items = [neutral_items[173:] for neutral_items in neutral_items]
        print(neutral_items)
    f.close()
    return neutral_items

def agan_shard():
    with open("html_code.txt", 'r') as f:
        text = f.read()
        search_id = r'data-for="scepter" currentitem="\w+'
        agan = re.findall(search_id, text)
        agan = [agan[32:] for agan in agan]
        search_id = r'data-for="shard" currentitem="\w+'
        shard = re.findall(search_id, text)
        shard = [shard[30:] for shard in shard]
        print(agan, "\n",  shard)
    f.close()
    return agan,shard

def creating_full_heros_info(match_id, heroes, items, neutral, agan, shard):
    os.remove("html_code(replaced).txt")
    os.remove("html_code.txt")
    heroes_inf = {}
    #{hero, [items], neutral, agan, shard}

selenium(gen_link_to_match(0))
get_match_lenght()
characters()
characters_items()
neutral_item()
agan_shard()