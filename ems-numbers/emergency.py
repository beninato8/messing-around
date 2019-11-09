import json
from pprint import pprint

with open('emergency.json', 'r') as f:
    d = json.load(f)['data']

countries = {x['Country']['Name']:x for x in d}
for x in countries:
    countries[x]['Country'].pop('Name')

# pprint(countries)
keys = ['Ambulance', 'Fire', 'Police', 'Dispatch']
for x in countries:
    for k in keys:
        # print(x)
        if len(countries[x][k][list(countries[x][k].keys())[0]]) != 1:
            # print(x)
            pass


for x in countries:
    if 'All' not in countries[x]['Dispatch'] or len(countries[x]['Dispatch'].keys()) != 1:
        print(x)
