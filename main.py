import requests
from bs4 import BeautifulSoup as bs
import random

def creating_link():
    get_rand_id = random.randint(1111,9999)
    url = f"https://ru.dotabuff.com/matches/866768{get_rand_id}"
    return str(url)

# def parsing(url):
def parsing():
    url = "https://ru.dotabuff.com/matches/8667684671"
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    players_sheet = soup.find(class_="team-results")
    print(players_sheet)


if __name__ == "__main__":
    # parsing(creating_link())
    parsing()
