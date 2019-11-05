from subprocess import Popen as cmd
from tqdm import tqdm
from itertools import product

s = '0123456789abcdef'

l = list(product(s, repeat=4))
l = [''.join(x) for x in l]
# print(l)
# exit()
for x in tqdm(l):
# for x in l:
    cmd(f'echo -e {x} "\\u{x}" >> hex.txt', shell=True,  executable="/bin/zsh").wait()