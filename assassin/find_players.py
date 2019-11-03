import subprocess
from pprint import pprint

def main(): 
    cmd = subprocess.run
    pipe = subprocess.PIPE
    out = cmd('ls *.txt', shell=True, stdout=pipe).stdout.decode('utf-8').split('\n')[:-1]
    # print(out)
    old = out[1]
    new = out[0]
    # print(old, new)
    c = cmd(f'diff "{old}" "{new}"', shell=True, stdout=pipe).stdout.decode('utf-8').split('\n')
    c = [x for x in c if any(y in x for y in ['<','>'])]

    # print(c)
    winners = [x[2:] for x in c if x[0] == '>']

    losers = [x[2:] for x in c if x[0] == '<']
    losers = [x for x in losers if all(x[:-1] != y[:-1] for y in winners)]

    winners2 = {}
    losers2 = {}
    for x in winners:
        winners2[x[:x.rfind(' ')]] = x[x.rfind(' ')+1:]
    for x in losers:
        losers2[x[:x.rfind(' ')]] = x[x.rfind(' ')+1:]

    w = ' and '.join(winners2.keys())
    l = ' and '.join(losers2.keys())

    count = new[:new.find(' ')]

    time = new.split(' ')[1:]
    time[-1] = time[-1].split('.')[0]
    time[-1] = time[-1].replace('-', ':')
    time[0] = time[0].replace('-','/')

    s1 = f"{w} killed {l} as of {' on '.join(time[::-1])}."
    s2 = f'There are {int(count)} players remaining.'
    return s1 + '\n' + s2

if __name__ == '__main__':
    s = main()
    print(s)
