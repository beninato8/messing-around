import os

path = './log/'
name = 'test.txt'
s = 'hey'

os.system('touch ' + path + name)
os.system('echo \"' + s + '\" >> ' + path + name)