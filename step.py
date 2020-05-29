class Step:
    x = 0
    y = 0

    def __eq__(self, other):
        return str(other) == str(self)


class A(Step):
    x = 0
    y = 1

    def __repr__(self):
        return 'A'


class B(Step):
    x = 1
    y = 0

    def __repr__(self):
        return 'B'


class C(Step):
    x = 0
    y = -1

    def __repr__(self):
        return 'C'
