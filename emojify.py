#!/usr/bin/env python

'''
emojify_python_script.py

# Description
Obfuscate your python script by converting an input script to an output script
that functions the same (hopefully) but encodes the code as emoji icons, currently emoticons.

# Usage
python emojify_python_script.py -h
python emojify_python_script.py --input input_script.py --output output_script.py

# Disclaimer
Not tested on complex scripts, so don't rely on this script to work,
not guaranteed to work at all, and it is probably easy to break.
One case it will fail is with non-unicode characters.

Also note if you want to securely protect your code from the eyes of others,
this is NOT a good way, so find another way.

# License
Copyright (c) 2017-2018, Chris Rands.
Redistribution and use of this code, with or without modification, are permitted,
provided that the the above copyright notice is included.
'''

import argparse
from collections import OrderedDict
from pprint import pformat

__author__ = 'Chris Rands'
__copyright__ = 'Copyright (c) 2017-2018, Chris Rands'

try:
    range = xrange
except NameError:
    pass  # Python 3

EMOTICONS = [':)', ':D', ':P', ':S', ':(', '=)', '=/', ':/', ':{', ';)']
# TODO: Add other alphabets as options including real emojis
MAX_STR_LEN = 70


def run_argparse():
    """User arguments"""
    parser = argparse.ArgumentParser(description='''
    Obfuscate your python script by converting an input script to an output script
    that functions the same (hopefully) but encodes the code as emoji icons, currently emoticons.
    -- Chris Rands, 2017-2018''')
    parser.add_argument('-i', '--input', required=True, help='input python script name')
    parser.add_argument('-o', '--output', required=True, help='output python script name')
    return parser.parse_args()


def chunk_string(in_s, n):
    """Chunk string to max length of n"""
    return '\n'.join('{}\\'.format(in_s[i:i+n]) for i in range(0, len(in_s), n)).rstrip('\\')


def encode_string(in_s, alphabet):
    """Convert input string to encoded output string with the given alphabet"""
    # Using OrderedDict to guarantee output order is the same
    # Note Python 2 and 3 inputs differ slightly due to pformat()
    d1 = OrderedDict(enumerate(alphabet))
    d2 = OrderedDict((v, k) for k, v in d1.items())
    return ('from collections import OrderedDict\n'
            'exec("".join(map(chr,[int("".join(str({}[i]) for i in x.split())) for x in\n'
            '"{}"\n.split("  ")])))\n'.format(pformat(d2), chunk_string('  '.join(
            ' '.join(d1[int(i)] for i in str(ord(c))) for c in in_s), MAX_STR_LEN)))


def main(in_file, out_file):
    """Read input and write output file"""
    with open(in_file) as in_f, open(out_file, 'w') as out_f:
        # This assumes it's ok to read the entire input file into memory
        out_f.write(encode_string(in_f.read(), EMOTICONS))


if __name__ == '__main__':
    args = run_argparse()
    main(args.input, args.output)