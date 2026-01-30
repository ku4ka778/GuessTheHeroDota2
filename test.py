from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import os
import re
try:
    os.remove("/html_code.txt")
except:
    pass
driver = webdriver.Chrome()
driver.get("https://www.opendota.com/matches/highMmr")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

try:
    time.sleep(10)

    # Get the complete HTML source code
    html_source = driver.page_source

    # Write the source to a local file with utf-8 encoding
    with open("html_code.txt", "w", encoding='utf-8') as f:
        f.write(html_source)


    print(f"Successfully saved the HTML source")
except:
    print("Error")
finally:
    driver.quit()

with open("html_code.txt", 'r') as f:
    text = f.read()
    search_id = r"/matches/\d+"
    search_dur = r"\d+:\d\d"
    result1 = re.findall(search_id, text)
    result2 = re.findall(search_dur, text)
    games = dict(zip(result1,result2))
    print(games)
f.close()

for i in games.keys():
    if games[i] == "0:00":
        del games[i]

