# CS:Git_Good: What is Important for Getting Kills in CS:GO?
## Analysing basic professional level CS:GO statistics

###### Have you ever wondered how people have such HIGH Kill/Death ratios in professional CS:GO matches?

No? Well don't fret, because I'm still going to show my findings to you anyways.

Language: Python
Libraries Used: Selenium, BeautifulSoup, pandas, numpy, scikitlearn, statsmodels


###### A Little backstory:
One day I decided to hop on CS:GO and play a couple competitive matches with my friends, to eventually lose all 5 games that we've played. I was so distraught as to why things happened this way, and I wanted to figure out a way that I could improve my CS:GO skills. Until this day, I am still pretty trash, but I have found some interesting data that shows some inconsistencies in my mental game.

So I decided to create a small little web scraper using the python libraries selenium and beautifulsoup to grab *professional* CS:GO player statistics on the [ESL Progaming Website](https://pro.eslgaming.com/csgo/proleague/statistics/). Unfortunately, the only available data of each player listed on the website were *Kill/Death Ratios*, *Headshot Ratios*, *Average **Distance** of each kill*, and *Number of Aces*. As for other websites, webscraping was not allowed, so the ESL ProGaming website had to do for now.

###### **PLEASE NOTE: THIS IS A SIDE PROJECT; IT IS NOT 100% COMPLETE AND MAY INCLUDE ERRORS THAT I MAY HAVE NOT FORSEEN. PAY ATTENTION AND READ *AT YOUR OWN RISK*.**