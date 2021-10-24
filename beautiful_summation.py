#!/usr/bin/env python3

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

import logging
import math

def main():
    p = get_number()
    q = get_number()
    n = get_number()
    m = get_number()

    total = solve(p,q,n,m)
    print(total)

def solve(p,q,n,m):
    # if p == 0:
    #     return 0
    # if m == 1:
    #     return 0
    # if n == 1:
    #     return p
    # if q == 0:
    #     num = fastpow(p, n+1, m) - p
    #     while num < 0:
    #         num += m
    #     common_fac = gcd(p-1,m)
    #     assert num % common_fac == 0
    #     return num // common_fac * mod_inverse((p-1)//common_fac,m) % m

    p_period_list, coefficients = base_polynomial(p,m,n)

    # print(f'initial coefficients: {coefficients}')
    if len(coefficients) > 2:
        for i in range(q):
            do_derivative(coefficients, m)
            # print(f'after {i+1}th derivative: {coefficients}')

    total = 0
    for c, ppow in zip(coefficients, p_period_list):
        total += c * ppow % m
        total = total % m
    while total < 0:
        total += m
    return total

def base_polynomial(p,m,n):
    if is_prime(m):
        return [1,p%m], [0,1]
    p_period_list, p_period_start = exp_period(p, m)
    # print(f'the period list of {p} is {p_period_list} (starts repeating at {p_period_start})')
    l = len(p_period_list)
    coefficients = [0] * l
    for i in range(1,l):
        if i <= n:
            coefficients[i] = 1
    for r in range(p_period_start, l):
        k = (n - r) // (l - p_period_start) # denominator is period length
        # print(f'considering {r}: found {k} powers of p={p} less than p^{n} congruent to p^{r}')
        coefficients[r] += max(k, 0)
    return p_period_list, coefficients

def do_derivative(coeffs, mod):
    for i in range(1, len(coeffs)):
        coeffs[i] = coeffs[i] * i % mod


def exp_period(base: int, mod: int) -> (list, int):
    seen = {}
    exp = 1
    pow = base
    powlist = [1]
    while pow not in seen:
        # logging.warn(f'reached exp={exp} in period finding')
        seen[pow] = exp
        powlist.append(pow)
        pow = pow * base % mod
        exp += 1
    return powlist, seen[pow]

def exp2pow(base,mod):
    pow = base
    while 1:
        yield pow
        pow = pow * pow % mod

def fastpow(base, exp, mod):
    result = 1
    for pow in exp2pow(base,mod):
        if exp == 0:
            break
        if exp & 1:
            result *= pow
        exp = exp >> 1
    return result

def gcd(a,b):
    while a > 0:
        a, b = b%a, a
    return b

def mod_inverse(a, mod):
    m = mod
    y = 0
    x = 1

    if (m == 1):
        return 0

    while (a > 1):

        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y

        # Update x and y
        y = x - q * y
        x = t

    # Make x positive
    if (x < 0):
        x = x + mod

    return x

def is_prime(a):
    if a < 2: return False
    for x in range(2, int(math.sqrt(a)) + 1):
        if a % x == 0:
            return False
    return True

main()


