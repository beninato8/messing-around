import requests
from bs4 import BeautifulSoup
import re
import operator

brawlers = ["Barley", "Bo", "Brock", "Bull", "Colt", "Crow", "Darryl", "Dynamike", "El Primo", "Frank", "Jessie", "Leon", "Mortis", "Nita", "Pam", "Penny", "Piper", "Poco", "Ricochet", "Shelly", "Spike", "Tara"]

base = 'http://brawlstars.wikia.com/wiki/'
speeds = {}
for b in brawlers:
    page = requests.get(base + b).text
    soup = BeautifulSoup(page, 'html.parser')
    for x in soup(text=re.compile(r'Movement speed')):
        speed = x.parent.next_element.next_element.next_element.contents[0]
        speeds[b] = speed

speeds = sorted(speeds.items(), key=operator.itemgetter(1), reverse=True)
for a, b in speeds:
    print(a, b)
