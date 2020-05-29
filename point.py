class Point:

    label = '-'

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return 0

    def __repr__(self):
        return f'{self.label}({self.x}, {self.y})'


class Hash(Point):

    label = '#'

    def __init__(self, x: int, y: int):
        super(Hash, self).__init__(x, y)


class Dot(Point):

    label = '.'

    def __init__(self, x: int, y: int):
        super(Dot, self).__init__(x, y)


class Start(Point):

    label = 'S'

    def __init__(self, x: int, y: int):
        super(Start, self).__init__(x, y)


class Joni(Point):

    label = 'X'

    def __init__(self, x: int, y: int):
        super(Joni, self).__init__(x, y)
