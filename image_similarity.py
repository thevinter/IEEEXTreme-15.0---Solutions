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

# numpy and scipy are available for use
import numpy as np
import itertools as it
from numpy.typing import *


def main():
    tests = get_number()
    for _ in range(tests):
        print(do_test())

def do_test():
    im_a = read_image()
    im_b = read_image()
    # print(im_a)
    # print(im_b)
    maxsim = 0
    for a in rotations(im_a):
        a_rows, a_cols = a.shape
        b_rows, b_cols = im_b.shape
        canvas_rows = 2*a_rows + b_rows
        canvas_cols = 2*a_cols + b_cols
        canvas = np.zeros((canvas_rows,canvas_cols), dtype=np.uint8)
        canvas[a_rows:a_rows+b_rows, a_cols:a_cols+b_cols] = im_b
        sim = similarity(a,canvas)
        if sim > maxsim:
            maxsim = sim
    return maxsim


def read_image():
    rows = get_number()
    cols = get_number()
    # print(f'reading {rows},{cols}')
    img = np.zeros((rows,cols), dtype=np.uint8)
    for i in range(rows):
        row = get_word()
        # print(f'reading {row}')
        for j,c in enumerate(row):
            if c == '#':
                img[i,j] = 1
    return img

def rotations(image):
    yield image
    yield image.T
    rot1 = np.rot90(image)
    yield rot1
    yield rot1.T
    rot2 = np.rot90(rot1)
    yield rot2
    yield rot2.T
    rot3 = np.rot90(rot2)
    yield rot3
    yield rot3.T


def similarity(a: ArrayLike, canvas: ArrayLike):
    a_rows, a_cols = a.shape
    c_rows, c_cols = canvas.shape
    maxsim = 0
    for i in range(c_rows-a_rows):
        for j in range(c_cols-a_cols):
            intersection = a * canvas[i:i+a_rows, j:j+a_cols]
            sim = np.sum(intersection)
            if sim > maxsim:
                maxsim = sim
    return maxsim

main()


