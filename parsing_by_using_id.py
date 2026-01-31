from random import randint
from parsing_id import sorting_html_code
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re

def gen_link_to_match():
    game_id = sorting_html_code()
    id = randint(0,len(game_id))
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
    return chr(game_time)

def choose_character():
    pass

def get_character_items():
    pass


