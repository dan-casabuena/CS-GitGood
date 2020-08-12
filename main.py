from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

esl_site = 'https://pro.eslgaming.com/csgo/proleague/statistics/'

client = urlopen(esl_site)
html_raw = client.read()
print(html_raw)