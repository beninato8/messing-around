import re

def is_double(s):
    return re.match(r'^[+-]?\d*\.?\d+$', s)

def grammar(b):
    return 'is' if b else 'isn\'t'

l = [1,
     2,
     '1.',
     '.2',
     '+3',
     2.2,
     '.333'
     '0.1.2'
     '',
     ' ',
     'adsf',
     '123a',
     '-.9',
     '+2.',
     '-22.3',
     '+2']
l = [str(x) for x in l]

for x in l:
    print('\'%s\' %s a double' % (x, grammar(is_double(x))))