import json
from pprint import pprint
import string

keys = list(string.ascii_lowercase)
vals = ['.-',
        '-...',
        '-.-.',
        '-..',
        '.',
        '..-.',
        '--.',
        '....',
        '..',
        '.---',
        '-.-',
        '.-..',
        '--',
        '-.',
        '---',
        '.--.',
        '--.-',
        '.-.',
        '...',
        '-',
        '..-',
        '...-',
        '.--',
        '-..-',
        '-.--',
        '--..',
]
keys2 = [x + ' word' for x in keys]
vals2 = ['Archery',
         'Banjo',
         'Candy',
         'Dog',
         'Eye',
         'Firetruck',
         'Giraffe',
         'Hippo',
         'Insect',
         'Jet',
         'Kite',
         'Laboratory',
         'Mustache',
         'Net',
         'Orchestra',
         'Paddle',
         'Quarterback',
         'Robot',
         'Submarine',
         'Tape',
         'Unicorn',
         'Vacuum',
         'Wand',
         'X-ray',
         'Yard',
         'Zebra',
]
d = {keys[i]:vals[i] for i in range(len(keys))}
d = {**d, **{keys2[i]:vals2[i] for i in range(len(keys))}}

with open('morse.json', 'w') as f:
    json.dump(d, f)