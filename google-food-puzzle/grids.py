import marisa_trie

with open('../../english-words/words_alpha.txt', 'r') as f:
    data = set(f.read().split('\n'))

trie = marisa_trie.Trie(data)

min_size = 5

def get_words(base, visited, board, i, j, limit=10):
    if limit < 0:
        return []
    if len(trie.keys(base)) == 0:
        return []
    nearby = get_adjacent(i, j) - visited
    out = []
    if base in data and len(base) > min_size:
        out.append(base)
    for (y, x) in nearby:
        new_word = base + board[y][x]
        # print(new_word, limit)
        if new_word in data and len(new_word) > min_size:
            out.append(new_word)
        if len(trie.keys(new_word)) == 0:
            continue
        current = get_words(base + board[y][x], visited | set([(y,x)]), board, y, x, limit=limit-1)
        for x in current:
            out.append(x)
    # print(out)
    # exit()
    return set(out)

def get_adjacent(i, j):
    out = set()
    for a in range(-1, 2):
        if i + a >= 8 or i + a < 0:
            continue
        for b in range(-1, 2):
            if j + b >= 6 or j + b < 0:
                continue
            out.add((i+a, j+b))
    return out

board = ['vbaysa', 'aelade', 'niertr', 'aeaswh', 'rv?aih', 'csofca', 'shyead', 'aksbla']
board = ['doodas', 'cpsmin', 'astre?', 'deteps', 'acacta', 'rsuoai', 'dtrdgd', 'boahan']
board = ['ygsine', 'dslogr', 'ne?bao', 'yoldyp', 'hferhb', 'cfitaa', 'izceod', 'ursoyk']
board = ['yg___e', 'dslo__', 'ne?b__', 'yoldy_', '_ferhb', '_fitaa', '__ceod', '__soyk']

# board = ['idrmis', 'cleagy', 'soo?aq', 'irclsa', 'etnaom', 'uiretm', 'qzigni', 'ernaub']
board = ['duocoe', 'amlenb', 'pibtuy', 'slliuo', 'rdnaoc', 'iosu?h', 'drearo', 'splyem']

# board = ['psgnil', 'iupmbw', 'ckncao', 'lognim', 'ebstib', 'gallrl', 'lopoac', 'f?ecnd']
# board = ['_s____', '_up___', '__nca_', '_o____', '__st__', '___r__', '__po__', '_s____']
board = [list(x) for x in board]

count = 0
out = set()
for i in range(8):
    for j in range(6):
        start = board[i][j]
        visited = set([(i,j)])
        for x in get_words(start, visited, board, i, j, limit=12):
            out.add(x)
        count += 1
        # exit()
        # if count > 10:
        #     exit()
        # print(board[i][j])

# print(get_adjacent(1, 1))
for x in sorted(out, key=len):
    print(x)
# print(out)