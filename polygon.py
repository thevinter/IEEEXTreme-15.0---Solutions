# a simple parser for python. use get_number() and get_word() to read

def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

import math


def main():
    tests = get_number()
    for _ in range(tests):
        do_test()

def do_test():
    N = get_number()
    poly = [None] * N
    for i in range(N):
        x = get_number()
        y = get_number()
        z = get_number()
        poly[i] = x,y,z
    nondeg = find_nondeg(poly)
    ar = area(poly,nondeg)
    cpn = coprime_normal(poly[nondeg],poly[nondeg+1],poly[nondeg+2])
    k = magic_constant(*cpn)
    b = on_edge(poly)
    # print(f'area {ar}, cpn: {cpn}, k={k}, edge points: {b}')
    interiors = round(ar/k - b/2) + 1
    print(interiors)

def find_nondeg(poly):
    for i,v in enumerate(poly):
        u = poly[(i+1) % len(poly)]
        w = poly[(i+2) % len(poly)]
        if any(normal(v,u,w)):
            return i


def on_edge(poly):
    count = 0
    for i,v in enumerate(poly):
        u = poly[(i+1) % len(poly)]
        count += gcd3(*diff(u,v))
    return count


def magic_constant(a,b,c):
    # abs(a)*(a*a + b*b)*
    return math.sqrt(a*a + b*b + c*c)

def det(a):
    return a[0][0]*a[1][1]*a[2][2] + a[0][1]*a[1][2]*a[2][0] + a[0][2]*a[1][0]*a[2][1] - a[0][2]*a[1][1]*a[2][0] - a[0][1]*a[1][0]*a[2][2] - a[0][0]*a[1][2]*a[2][1]

def diff(a,b):
    return a[0] - b[0], a[1] - b[1], a[2] - b[2]

def normal(a, b, c):
    return cross(diff(a,b), diff(b,c))

def coprime_normal(a,b,c):
    x,y,z = normal(a,b,c)
    g = gcd3(x,y,z)
    return x // g, y // g, z // g

def unit_normal(a,b,c):
    x,y,z = normal(a,b,c)
    magnitude = math.sqrt(x**2 + y**2 + z**2)
    return (x/magnitude, y/magnitude, z/magnitude)

def dot(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def cross(a, b):
    x = a[1] * b[2] - a[2] * b[1]
    y = a[2] * b[0] - a[0] * b[2]
    z = a[0] * b[1] - a[1] * b[0]
    return (x, y, z)

def area(poly,nondeg):
    if len(poly) < 3:
        return 0
    total = [0, 0, 0]
    a = poly[-1]
    for i in range(len(poly)-2):
        b = poly[i]
        c = poly[i+1]
        u = diff(a,b)
        v = diff(a,c)
        prod = cross(u,v)
        total[0] += prod[0]
        total[1] += prod[1]
        total[2] += prod[2]
    result = dot(total, unit_normal(poly[nondeg], poly[nondeg+1], poly[nondeg+2]))
    return abs(result/2)

def gcd(a,b):
    a = -a if a < 0 else a
    b = -b if b < 0 else b
    while a>0:
        a,b = b%a, a
    return b

def gcd3(a,b,c):
    return gcd(gcd(a,b),c)

main()


