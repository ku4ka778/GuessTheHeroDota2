from parsing_id import creating_links
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
import shutil

url = []
def selenium(i):
    global url
    url = creating_links()
    print(url[i])
    print("Parsing...")
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(url[i])
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    try:
        time.sleep(10)
        html_source = driver.page_source
        with open("html_code.txt", "w", encoding='utf-8') as f:
            f.write(html_source)
        f.close()
        print("Html source saved successfully")
    except Exception as e:
        print(e)
        print("Error")
    finally:
        driver.quit()
    return url

def get_match_length():
    with open("html_code.txt", 'r', encoding='utf-8') as f:
        text = f.read()
        search_id = r"<div><span>\d+:\d+"
        result = re.findall(search_id, text)
        game_time = result[0][11:]
    f.close()
    return game_time

def characters():
    with open("html_code.txt", 'r') as f:
        text = f.read()
        search_id = r"/dota_react/heroes/\w+"
        result = re.findall(search_id, text)
        heroes = list(dict.fromkeys(result))
        heroes = [heroes[19:] for heroes in heroes]
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
    return items

def neutral_item():
    with open("html_code.txt", 'r') as f:
        text = f.read()
        search_id = r'<div class="inflictorWithValue neutral" data-tip="true" data-for="....................."><img src="https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/items/\w+'
        neutral_items = re.findall(search_id, text)
        neutral_items = [neutral_items[173:] for neutral_items in neutral_items]
    f.close()
    return neutral_items

def agan():
    with open("html_code.txt", 'r') as f:
        text = f.read()
        search_id = r'</div></div></div><img src="/assets/images/dota2/scepter_\d+'
        aghanim = re.findall(search_id, text)
        aghanim = [aghanim[57:] for aghanim in aghanim]
    f.close()
    return aghanim

def shard():
    with open("html_code.txt", 'r') as f:
        text = f.read()
        search_id = r'data-for="scepter" currentitem="false"><img src="/assets/images/dota2/shard_\d+'
        ag_shard = re.findall(search_id, text)
        ag_shard = [ag_shard[76:] for ag_shard in ag_shard]
    f.close()
    return ag_shard

def creating_full_heroes_info():
    heroes = characters()
    items = characters_items()
    neutral_items = neutral_item()
    aghanim = agan()
    ag_shard = shard()
    game_heroes = [heroes, items, neutral_items, aghanim, ag_shard]
    print(game_heroes)
    return game_heroes








