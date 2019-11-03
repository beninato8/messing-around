import requests
import time
import re
from apscheduler.schedulers.background import BackgroundScheduler
from pprint import pprint
from datetime import datetime
import subprocess
import sys
import time
from find_players import main as recent
import contacts

scheduler = BackgroundScheduler()
pipe = subprocess.PIPE
cmd = subprocess.run

def write_it(count, now, lines):
    f = open(f'{count} {now}.txt', 'w+')
    f.write(lines)
    f.close()

def fix_time(t):
    t = t.split(' ')
    t[0] = t[0].replace('-', '/')
    t[1] = t[1].replace('-', ':')
    return ' '.join(t)

def comp(count, old, now):
    count_old = old.split(' ')[0]

    if count == count_old:
        return f'{fix_time(now)}'
    else:
        return f'{fix_time(now)}    {int(count_old)} ==> {int(count)}'
    pass

def do_it():
    # print('hi')
    text = requests.get('https://server.thomaswoodside.com/flask/').text
    # print(text)
    # exit()
    text = re.sub(r'[\t]+', ' ', text)
    lines = []
    for line in text.split('\n'):
        x = line.split(' ')
        if x[-1].isdigit():
            lines.append(x)

    lines = '\n'.join(' '.join(x) for x in lines)+'\n'
    now = datetime.now().strftime('%m-%d %H-%M-%S')
    # subprocess.Popen(f'touch "{now}".txt', shell=True).wait()
    # subprocess.Popen(f'echo "{lines}" > "{now}".txt', shell=True).wait()
    count = lines.count("\n")
    count = f'{count:03}'
    out = subprocess.run(f'ls *.txt', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
    if out == "":
        write_it(count, now, lines)
        return

    text = out.split('\n')
    old = text[0]

    c = comp(count, old, now)
    print(c)
    # print(f'{now} - {old}')
    # exit()
    with open(old, 'r') as f:
        if lines == f.read():
            pass
            return
    # print('write')
    # exit()
    write_it(count, now, lines)

    time.sleep(3)
    print()
    s = recent()
    print(s)
    subs = contacts.subs
    for person in subs:
        p = "$HOME/bin/text"
        cmd(f'{p} {person} "{s}"', shell=True, executable='/bin/zsh', stdout=subprocess.PIPE)
        # print(person, s)
        pass

    print()

if len(sys.argv) == 1:
    do_it()
    exit()
# exit()
# scheduler.add_job(do_it, 'cron', second='0,15,30,45', misfire_grace_time=300, max_instances=3)
scheduler.add_job(do_it, 'cron', minute='0,15,30,45', misfire_grace_time=300, max_instances=3)
scheduler.start()
print('running')

try:
    # This is here to simulate application activity (which keeps the main thread alive).
    while True:
        time.sleep(2)
except (KeyboardInterrupt, SystemExit):
    # Not strictly necessary if daemonic mode is enabled but should be done if possible
    scheduler.shutdown()
