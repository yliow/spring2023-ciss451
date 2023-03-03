# file: numbertheory.py
#
# GCD, EEA, etc..

# file: Zmod.py

class Zmod:
    def __init__(self, x, N):
        self.x = x
        self.N = N
    def __str__(self):
        return "%s mod %s" % (self.x, self.N)

    def __add__(self, b):
        """ b can be a Zmod object or an int """
        if isinstance(b, int):
            return Zmod((self.x + b) % self.N, self.N)
        elif isinstance(b, Zmod):
            if self.N != b.N:
                raise ValueError
            return Zmod((self.x + b.x) % self.N, self.N)
        else:
            raise TypeError("b is %s is neither int nor Zmod" % b)
    def __radd__(self, b):
        return self + b

    def __neg__(self):
        return Zmod((-self.x) % self.N, self.N)
    def __sub__(self, b):
        return self + (-b)
    def __rsub__(self, b):
        return (-self) + b

    def __mul__(self, b):
        """ b can be a Zmod object or an int """
        if isinstance(b, int):
            return Zmod((self.x * b) % self.N, self.N)
        elif isinstance(b, Zmod):
            if self.N != b.N:
                raise ValueError
            return Zmod((self.x * b.x) % self.N, self.N)
        else:
            raise TypeError("b is %s is neither int nor Zmod" % b)
    def __rmul__(self, b):
        return self * b
    
if __name__ == '__main__':
    a = Zmod(9, 10)
    print(a)
    b = Zmod(2, 10)
    print(b)
    c = a + b
    print(c)
    d = a + 1
    print(d)
    #a + "s"

    e = 2 + a
    print(e)

    print(a)
    a += 1 #  python will call a = a + 1
    print(a)

    a += 3
    print(-a)
    print(a, b)
    c = a - b
    print(c)

    a = Zmod(2, 10)
    b = Zmod(3, 10)
    print(a * b)
    b = Zmod(8, 10)
    print(a * b)
    a = Zmod(2, 10)
    print(a * 3)
    print(3 * a)
