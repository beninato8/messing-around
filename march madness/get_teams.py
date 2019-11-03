#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup as bs4
import re

# url = 'http://fantasy.espn.com/tournament-challenge-bracket/2019/en/bracket'
# soup = bs4(requests.get(url).text, 'html.parser')
# for x in soup.find_all('span', {'class':'abbrev'}):
#     print(x.next_sibling.contents[0])

colleges = ["Duke","North Dakota St","VCU","UCF","Mississippi St","Liberty","Virginia Tech","Saint Louis","Maryland","Belmont","LSU","Yale","Louisville","Minnesota","Michigan State","Bradley","Gonzaga","F. Dickinson","Syracuse","Baylor","Marquette","Murray State","Florida St","Vermont","Buffalo","Arizona State","Texas Tech","N Kentucky","Nevada","Florida","Michigan","Montana","Virginia","Gardner-Webb","Ole Miss","Oklahoma","Wisconsin","Oregon","Kansas State","UC Irvine","Villanova","Saint Mary's","Purdue","Old Dominion","Cincinnati","Iowa","Tennessee","Colgate","North Carolina","Iona","Utah State","Washington","Auburn","New Mexico St","Kansas","Northeastern","Iowa State","Ohio State","Houston","Georgia State","Wofford","Seton Hall","Kentucky","Abil Christian"]

base = "https://www.google.com/search?q="
for c in colleges:
    soup = bs4(requests.get(f'{base}{c}').text, 'html.parser')
    for x in soup.find_all('a', {'href':re.compile('.*')}):
        print(x)
