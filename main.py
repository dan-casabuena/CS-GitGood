from bs4 import BeautifulSoup as soup
from selenium import webdriver
import csv

esl_site = 'https://pro.eslgaming.com/csgo/proleague/statistics/'

# Use Selenium to load up unfiltered list of players and their stats
driver = webdriver.Chrome()
driver.get(esl_site)

parsed_html = soup(driver.page_source, 'html.parser')
driver.close()
players_raw = parsed_html.findAll('div', {"class":"playerbadge ng-scope"})

with open('players.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['player_name', 'KillDeathRatio', 'HeadshotRatio'])
    for player in players_raw:
        nick = player.findAll('div', {"class":"name"})[0].contents[1].text
        stats = player.findAll('div', {"class":"value ng-binding"})
        kdr = stats[0].text
        hs = float(stats[1].text[:-1]) / 100
        writer.writerow([nick, hs, kdr])
