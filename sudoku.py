
class Cell():
    def __init__(self, val=None):
        self.val = val
        if val:
            self.allowed = None
        else:
            self.allowed = set()

    def add_num(self, *num):
        if isinstance(num, int):
            self.allowed.add(num)
        elif isinstance(num, list) or isinstance(num, set) or isinstance(num, tuple):
            for x in num:
                self.allowed.add(x)
    def remove_num(self, num):
        if self.allowed and num in self.allowed:
            self.allowed.remove(num)
            if len(self.allowed) == 1:
                self.val = self.allowed.pop()
                self.allowed = None
    def __str__(self):
        if not self.val and len(self.allowed) == 0:
            return '[None]'
        if self.val:
            return f'[ {self.val} ]'
        else:
            return f'[*{" ".join(str(x) for x in sorted(self.allowed))}*]'
    def __repr__(self):
        return str(self)
    def __eq__(self, num):
        return self.val == num
    def __hash__(self):
        if self.val:
            return hash(self.val)
        return hash(-1)
class p(object):
    """docstring for p"""
    def __init__(self, x, y):
        self.x = x
        self.y = y


square_d = {0: p(0, 0),
                1: p(3, 0),
                2: p(6, 0),
                3: p(0, 3),
                4: p(3, 3),
                5: p(6, 3),
                6: p(0, 6),
                7: p(3, 6),
                8: p(6, 6)}

square_pos = {0: p(0, 0),
              1: p(1, 0),
              2: p(2, 0),
              3: p(0, 1),
              4: p(1, 1),
              5: p(2, 1),
              6: p(0, 2),
              7: p(1, 2),
              8: p(2, 2),
}


class Grid():
    """docstring for Grid"""
    
    def __init__(self):
        self.cells = [[Cell() for i in range(9)] for j in range(9)]
    def __str__(self):
        s = ''
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                s += str(self.cells[i][j])
            s += '\n'
        return s
    def col(self, num):
        l = []
        for i in range(len(self.cells)):
            l.append(self.cells[i][num])
        return l
    def row(self, num):
        return self.cells[num]
    def square(self, num):
        c = self.cells
        x_off = square_d[num].x
        y_off = square_d[num].y
        l = []
        for x in range(0, 3):
            for y in range(0, 3):
                l.append(c[x+x_off][y+y_off])
        return l
    def check_row(self, num):
        r = self.row(num)
        return set(range(1,10)) == set(r)

    def check_col(self, num):
        c = self.col(num)
        return set(range(1, 10)) == set(c)

    def check_square(self, num):
        s = self.square(num)
        return set(range(1, 10)) == set(s)

    def set_row(self, row, *args):
        for col, num in args:
            self.cells[row][col] = Cell(num)

    def set_col(self, col, *args):
        for row, num in args:
            self.cells[row][col] = Cell(num)

    def set_square(self, sq, *args):
        x_off = square_d[sq].x
        y_off = square_d[sq].y
        for pos, num in args:
            x = square_pos[pos].x
            y = square_pos[pos].y
            self.cells[x+x_off][y+y_off] = Cell(num)

        """

        0
        0,0 0,1 0,2
        1,0 1,1 1,2
        2,0 2,1 2,2

        1
        0,3 0,4, 0,5
        1,
        """

x = Grid()
x.cells[7][7].add_num(3, 4, 5)
print(x.cells[7][7])
print()
print(x)
print()
x.set_square(0, (0,1), (1,3))
print(x)

s1 = {1,2,3,4,5}
s2 = {  1, 3, 4}

print(s1, s2)
print(s1 - s2, s2 - s1)
print(s1 | s2, s2 | s1)
print(s1 & s2, s2 & s1)
print(s1 ^ s2, s2 ^ s1)