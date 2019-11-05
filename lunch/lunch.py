#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import os
authenticate = __import__('better-sheets').authenticate
write = __import__('better-sheets').write
from apscheduler.schedulers.background import BackgroundScheduler
import time
import pandas as pd
import numpy as np
import sys

def camel(s):
    if re.sub(r'[\n\t\s ]+', '', s) == '':
        return ''
    l = s.split(' ')
    for i,x in enumerate(l):
        l[i] = x[0].upper() + ''.join(y.lower() for y in x[1:])
    return ' '.join(l)

def dishes(item):
    # print([type(x) for x in item])
    title = item[0]
    options = item[1]
    dishes = []
    for dish in options.find_all('div', {'class':'item item-week'}):
        dishes.append(dish.text.strip())
    return {title:dishes}

def menu_print(d):
    s = []
    for k in d:
        s.append(k)
        for x in d[k]:
            s.append('    ' + x)
    return '\n'.join(s)

def csv_format(s):
    s = s.replace('    ', '')
    s = s.replace('Soup\n', '(')
    s = s.replace('\nEntree\n', ')\n(')
    s = s.replace('\nVeggie\n', ')\n(')
    s = s.replace('\nSides\n', ')\n(')
    s = s.replace('\nPizza\n', ')\n(')
    s += ')'
    s = s.replace('\n', ', ')
    s = s.replace('), (', ') (')
    return s

def main(single=False):
    path = os.path.dirname(__file__) + '/'
    last_date = pd.read_csv(f'{path}lunch/lunch.csv', names = ['date', 'menu']).tail(1).values.tolist()[0][0]
    today = datetime.now().strftime('%Y-%m-%d')
    print(today)
    page = requests.get('https://myschooldining.com/menlo')
    soup = BeautifulSoup(page.text, 'html.parser')

    foods = []
    for table in soup.find_all('table', {'id':'table_calendar_week'}):
        for cell in table.find_all('td', {'day_no':today}):
            for menu in cell.find_all('div', {'id':'menlodining_lunch'}):
                soup = menu.find('div', {'id':'menlodining_lunch_soup'})
                entree = menu.find('div', {'id':'menlodining_lunch_entree'})
                veggie = menu.find('div', {'id':'menlodining_lunch_vegetarianentree'})
                sides = menu.find('div', {'id':'menlodining_lunch_sides'})
                pizza = menu.find('div', {'id':'menlodining_lunch_pizza'})
    menu = [('Soup', soup), ('Entree', entree), ('Veggie', veggie), ('Sides', sides), ('Pizza', pizza)]
    menu = [x for x in menu if x[1]]
    d = dict()
    for x in menu:
        d = {**d, **dishes(x)}

    display = menu_print(d)
    # print(csv_format(display))
    # exit()
    # last_date = 'asdf'
    if single:
        print(display)
        return
    write(authenticate(), 1, 1, display)
    if last_date != today:
        print(display)
        print()
        l = [today, csv_format(display)]
        df = pd.DataFrame(np.array(l).reshape(1,2))
        df.to_csv(f'{path}lunch/lunch.csv', mode='a', header=False, index=False)
    
    # seth = '6502245471'
    # me = '6509967590'
    # os.system(f'osascript ~/bin/text.scpt {me} "{display}"')

def x():
    print('asdf')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(single=True)
        exit()
    # main()
    # exit()
    # write(authenticate(), 1, 1, '')
    scheduler = BackgroundScheduler()
    # https://apscheduler.readthedocs.io/en/latest/modules/triggers/cron.html
    # scheduler.add_job(main, 'cron', minute=27, misfire_grace_time=20000)
    scheduler.add_job(main, 'cron', day_of_week='mon-fri', hour='0-11', minute='0,15,30,45', misfire_grace_time=300)
    scheduler.start()
    print('running')

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()