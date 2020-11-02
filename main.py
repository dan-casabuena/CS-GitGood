from bs4 import BeautifulSoup as soup
from selenium import webdriver
import csv
import time

esl_site = 'https://pro.eslgaming.com/csgo/proleague/statistics/'

driver = webdriver.Chrome()     #Using Chrome Webdriver, available for download on Chrome Website
driver.get(esl_site)
time.sleep(5)

tables = []

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

for _ in range(4):
    table = driver.find_element_by_class_name("statstable")
    tables.append(soup(table.get_attribute('innerHTML'), 'html.parser'))
    driver.find_element_by_css_selector("div[ng-click='nextpage()']").click()

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['player_name', 'HeadshotRatio', 'AvgDistance', 'Aces', 'KillDeathRatio'])
    for table in tables:
        players_raw = table.findAll('div', {"class":"row ng-scope"})
        for player in players_raw:
            try:
                nick = player.findAll('div', {"class":"columnfield tier1 name ng-binding"})[0].strip()
            except TypeError:
                nick = player.findAll('div', {"class":"columnfield tier1 name ng-binding"})[0].contents[1].strip()
            kdr = player.findAll('div', {"class":"columnfield tier1 kd ng-binding active"})[0].text
            hsr = float(player.findAll('div', {"class":"columnfield tier2 headshotrate ng-binding"})[0].text[:-1])/100
            distance = player.findAll('div', {"class":"columnfield tier3 avgkilldistance ng-binding"})[0].text
            aces = player.findAll('div', {"class":"columnfield tier3 aces ng-binding"})[0].text
            writer.writerow([nick, hsr, distance, aces, kdr])
            