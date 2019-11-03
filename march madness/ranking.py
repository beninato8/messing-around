#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup as bs4
import re

human_headers = { "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                    "accept-language" : "en-US,en;q=0.9",
                    "accept-encoding" : "gzip, deflate, br",
                    "upgrade-insecure-requests" : "1",
                    "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.183 Safari/537.36 Vivaldi/1.96.1147.64"
                }

with open('alexa_rank.txt', 'r') as f:
    colleges = f.read()
colleges = [''] + colleges.split('\n')
colleges2 = []
for i, x in enumerate(colleges):
    if x == '':
        colleges2.append([colleges[i+1], colleges[i+2]])
for x in colleges2:
    x[1] = re.sub(r'https?://(www\.)?', '' , x[1])
    x[1] = re.sub(r'/', '' , x[1])
# print(colleges2)
base = "https://www.alexa.com/siteinfo/"
college_rank = {}
for x in colleges2:
    soup = bs4(requests.get(f'{base}{x[1]}', headers=human_headers).text, 'html.parser')
    y = soup.find('strong', {'class':"metrics-data align-vmiddle"})
    rank = int(y.contents[-1].rstrip().strip().replace(',',''))
    college_rank[x[0]] = rank
    print(x[0], rank)