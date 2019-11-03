#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup as bs4
import re

colleges = ["Duke","North Dakota St","VCU","UCF","Mississippi St","Liberty","Virginia Tech","Saint Louis","Maryland","Belmont","LSU","Yale","Louisville","Minnesota","Michigan State","Bradley","Gonzaga","F. Dickinson","Syracuse","Baylor","Marquette","Murray State","Florida St","Vermont","Buffalo","Arizona State","Texas Tech","N Kentucky","Nevada","Florida","Michigan","Montana","Virginia","Gardner-Webb","Ole Miss","Oklahoma","Wisconsin","Oregon","Kansas State","UC Irvine","Villanova","Saint Mary's","Purdue","Old Dominion","Cincinnati","Iowa","Tennessee","Colgate","North Carolina","Iona","Utah State","Washington","Auburn","New Mexico St","Kansas","Northeastern","Iowa State","Ohio State","Houston","Georgia State","Wofford","Seton Hall","Kentucky","Abil Christian"]

human_headers = { "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                    "accept-language" : "en-US,en;q=0.9",
                    "accept-encoding" : "gzip, deflate, br",
                    "upgrade-insecure-requests" : "1",
                    "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.183 Safari/537.36 Vivaldi/1.96.1147.64"
                }

base = "https://searchenginesmarketer.com/company/resources/university-college-list/"
soup = bs4(requests.get(f'{base}', headers=human_headers).text, 'html.parser')
i = 0
for row in soup.find_all('tr'):
    if i != 0:
        j = 0
        for cell in row.find_all('td'):
            if j < 2:
                if 'http' in str(cell.contents[0]):
                    print(cell.find('a').contents[0])
                else:
                    print(cell.contents[0])
            j += 1
        print()
    i+=1