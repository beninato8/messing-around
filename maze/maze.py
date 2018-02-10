"""
Copied from https://code.activestate.com/recipes/578356-random-maze-generator/
Modified by Nicholas Beninato
 - specifing maze size using command line args
 - fixing issue with image dimensions
 - commenting out code that requires PIL for use on a computer with little python features installed
"""
# Random Maze Generator using Depth-first Search
# http://en.wikipedia.org/wiki/Maze_generation_algorithm
# FB36 - 20130106
import random
# from PIL import Image
import copy
import sys

args = sys.argv
if len(args) == 3:
    maze_width = int(args[1])
    maze_height = int(args[2])
elif len(args) == 5:
    min_cols = int(args[1])
    max_cols = int(args[2])
    min_rows = int(args[3])
    max_rows = int(args[4])
    maze_height = random.randrange(min_rows, max_rows)
    maze_width = random.randrange(min_cols, max_cols)
else:
    maze_width = 10; maze_height = 10 # width and height of the maze

print(maze_width, maze_height)

# imgx = int(50*(maze_width+2)); imgy = int(50*(maze_height+2))
# image = Image.new("RGB", (imgx, imgy))
# pixels = image.load()
maze = [[0 for x in range(maze_width)] for y in range(maze_height)]
dx = [0, 1, 0, -1]; dy = [-1, 0, 1, 0] # 4 directions to move in the maze
color = [(0, 0, 0), (255, 255, 255)] # RGB colors of the maze
# start the maze from a random cell
cx = random.randint(0, maze_width - 1); cy = random.randint(0, maze_height - 1)
maze[cy][cx] = 1; stack = [(cx, cy, 0)] # stack element: (x, y, direction)

while len(stack) > 0:
    (cx, cy, cd) = stack[-1]
    # to prevent zigzags:
    # if changed direction in the last move then cannot change again
    if len(stack) > 2:
        if cd != stack[-2][2]: dirRange = [cd]
        else: dirRange = range(4)
    else: dirRange = range(4)

    # find a new cell to add
    nlst = [] # list of available neighbors
    for i in dirRange:
        nx = cx + dx[i]; ny = cy + dy[i]
        if nx >= 0 and nx < maze_width and ny >= 0 and ny < maze_height:
            if maze[ny][nx] == 0:
                ctr = 0 # of occupied neighbors must be 1
                for j in range(4):
                    ex = nx + dx[j]; ey = ny + dy[j]
                    if ex >= 0 and ex < maze_width and ey >= 0 and ey < maze_height:
                        if maze[ey][ex] == 1: ctr += 1
                if ctr == 1: nlst.append(i)

    # if 1 or more neighbors available then randomly select one and move
    if len(nlst) > 0:
        ir = nlst[random.randint(0, len(nlst) - 1)]
        cx += dx[ir]; cy += dy[ir]; maze[cy][cx] = 1
        stack.append((cx, cy, ir))
    else: stack.pop()

maze.insert(0, list([0 for x in range(len(maze[0]))]))
maze.append(list([0 for x in range(len(maze[0]))]))
for i in range(len(maze)):
    maze[i].insert(0, 0)
    maze[i].append(0)

maze[0][1] = 1
maze[-1][-2] = 1

my_dict = {1:' ', 0:'#'}
maze2 = copy.deepcopy(maze)
for i in range(len(maze2)):
    for j in range(len(maze2[i])):
        maze2[i][j] = my_dict[maze2[i][j]]

# print(maze2)
fh = open("Maze_" + str((maze_width+2)) + "x" + str((maze_height+2)) + ".txt", "w")
lines_of_text = []
myline = ""
for line in maze2:
    for character in line:
        myline += character
    lines_of_text.append(myline + '\n')
    myline = ""
fh.writelines(lines_of_text)
fh.close()

# paint the maze
# for ky in range(imgy):
#     for kx in range(imgx):
#         pixels[kx, ky] = color[maze[int((maze_height+2) * ky / imgy)][int((maze_width+2) * kx / imgx)]]
# image.save("Maze_" + str((maze_width+2)) + "x" + str((maze_height+2)) + ".png", "PNG")
