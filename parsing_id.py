import time
import re
from selenium import webdriver
import os


def selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.opendota.com/matches/highMmr")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    return driver

def saving_code(driver):
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

def sorting_html_code():
    saving_code(selenium())
    with open("html_code.txt", 'r') as f:
        text = f.read()
        search_id = r"/matches/\d+"
        search_dur = r"\d+:\d\d"
        result1 = re.findall(search_id, text)
        result2 = re.findall(search_dur, text)
        games = dict(zip(result1, result2))
        print(games)
    f.close()
    return games

def games_id(games):
    for i in games.keys():
        if games[i] == "0:00":
            del games[i]
    os.remove("/html_code.txt")
    return games

