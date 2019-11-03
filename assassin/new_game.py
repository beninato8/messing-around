from pprint import pprint

import subprocess
pipe = subprocess.PIPE
cmd = subprocess.run


out = cmd(f'ls *.txt', shell=True, stdout=pipe, stderr=pipe).stdout.decode('utf-8')
if out == "":
    exit()

out = cmd(f'ls -d */', shell=True, stdout=pipe, stderr=pipe).stdout.decode('utf-8')

latest = '0'
for x in out.split('\n')[:-1]:
    if x[:5] == 'round':
        latest = x.split('_')[-1][:-1]

cmd(f'mkdir round_{int(latest)+1}', shell=True)
cmd(f'mv *.txt round_{int(latest)+1}', shell=True)