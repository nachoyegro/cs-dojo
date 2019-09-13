"""
    Problem:
        cons(a, b) constructs a pair, and car(pair) and cdr(pair) 
        returns the first and last element of that pair. 
        For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

        Implement car and cdr.
"""

def car(pair):
    def fst(a, b):
        return a
    return pair(fst)

def cdr(pair):
    def snd(a, b):
        return b
    return pair(snd)

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

if __name__ == '__main__':
    assert car(cons(2, 3)) == 2
    assert cdr(cons(2, 3)) == 3