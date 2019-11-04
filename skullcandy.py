#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup as bs4
import re
from datetime import datetime

html = requests.get('https://www.skullcandy.com/shop/earbuds/bluetooth-earbuds/method-wireless').text
price = re.findall(r'(?<=withoutTax">\$)[^<]+', html)[0]
price = float(price)
if price != 59.99:
    print(price)
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))