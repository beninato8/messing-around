import sys

def bordered(text):
    if not text:
        return ''
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    c = {'tl':'╭', 'tr':'╮', 'br':'╯', 'bl':'╰'}
    # c = {'tl':'┌', 'tr':'┐', 'br':'┘', 'bl':'└'}
    res = [c['tl'] + '─' * (width + 4) + c['tr']]
    res.append('│' + ' ' * (width + 4) + '│')
    for s in lines:
        res.append('│  ' + (s + ' ' * width)[:width] + '  │')
    res.append('│' + ' ' * (width + 4) + '│')
    res.append(c['bl'] + '─' * (width + 4) + c['br'])
    return '\n'.join(res)

args = sys.argv
print(bordered('\n'.join(args[1:])))