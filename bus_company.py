#!/usr/bin/env pypy3

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

def get_city():
    return get_number() - 1

import random
import math
import logging
from dataclasses import dataclass
from collections import defaultdict
from typing import Optional

import sys

sys.setrecursionlimit(100000)

logging.basicConfig(level=logging.DEBUG)

def main():
    tree = read_initial_tree()
    #logging.debug('initial tree:\n%s\n', tree.dbg())
    queries = get_number()
    for _ in range(queries):
        handle_query(tree)

def read_initial_tree(randomized=True):
    cities = get_number()
    owner = [None] * cities
    for i in range(cities):
        owner[i] = get_number()
    adjacency = [[] for _ in range(cities)]
    for _ in range(cities - 1):
        a = get_city()
        b = get_city()
        adjacency[a].append(b)
        adjacency[b].append(a)
    start = random.randrange(cities) if randomized else 0
    return build_tree(start, adjacency, owner)


@dataclass
class Node:
    value: int
    owner: int
    parent: Optional['Node']
    paths: list# [(int,int)]

    def is_child_of(self, other:int):
        parent = self.parent
        while parent is not None:
            if parent.value == other:
                return True
            parent = parent.parent
        return False


    def make_root(self):
        if self.parent is None: # already root
            return
        self.parent.make_root() # ensure we're the first child
        oldparent = self.parent
        for team in (0,1): # fix paths
            mypaths = self.paths[team]
            parentpaths = oldparent.paths[team]
            parentpaths.count -= mypaths.count
            parentpaths.total_distance -= mypaths.total_distance + mypaths.count
            mypaths.count += parentpaths.count
            mypaths.total_distance += parentpaths.total_distance + parentpaths.count
        # invert the link
        oldparent.parent = self
        self.parent = None

    def direction_from_root(self):
        node = self
        while node.parent.parent is not None:
            node = node.parent
        return node.value


    def paths_distances_with_count(self, team):
        path = self.paths[team]
        return path.total_distance, path.count


    def flip(self):
        old_owner = self.owner
        new_owner = 1 - self.owner
        node = self
        distance = 0
        while node is not None:
            node.paths[new_owner].count += 1
            node.paths[new_owner].total_distance += distance
            node.paths[old_owner].count -= 1
            node.paths[old_owner].total_distance -= distance
            distance += 1
            node = node.parent
        self.owner = new_owner

    def build(self, adjacency: list, owner: list, nodelist: list):
        nodelist[self.value] = self
        self.paths = [Pathcount(0,0),Pathcount(0,0)]
        self.paths[self.owner].count = 1
        for x in adjacency[self.value]:
            if self.parent is not None and x == self.parent.value:
                continue
            childnode = Node(x, owner[x], self, None)
            childnode.build(adjacency, owner, nodelist)
            for o,childpc in enumerate(childnode.paths):
                self.paths[o].count += childpc.count
                self.paths[o].total_distance += childpc.total_distance + childpc.count

@dataclass
class Pathcount:
    count: int
    total_distance: int


@dataclass
class Tree:
    root: Node
    nodes: list

    def flip(self, city):
        target = self.nodes[city]
        target.flip()

    def winner(self, a:int, b:int) -> Optional[int]:
        exclude = None
        nodea = self.nodes[a]
        nodeb = self.nodes[b]
        if nodea.is_child_of(b):
            self.make_root(b)
            exclude = nodea.direction_from_root()
        elif nodeb.is_child_of(a):
            self.make_root(a)
            exclude = nodeb.direction_from_root()
        a_score = self.score_of(0,a,b,exclude)
        b_score = self.score_of(1,a,b,exclude)
        if a_score == b_score:
            return 'TIE'
        elif a_score is None:
            return 'B'
        elif b_score is None or a_score < b_score:
            return 'A'
        else:
            return 'B'

    def score_of(self, team:int, a:int, b:int, exclude:Optional[int]):
        suma, counta = self.nodes[a].paths_distances_with_count(team)
        sumb, countb = self.nodes[b].paths_distances_with_count(team)
        if exclude is not None:  # exclude from count paths passing through excluded node
            exclnode = self.nodes[exclude]
            exclsum, exclcount = exclnode.paths_distances_with_count(team)
            if exclnode.parent.value == a:
                suma -= exclsum + exclcount
                counta -= exclcount
            elif exclnode.parent.value == b:
                sumb -= exclsum
                countb -= exclcount
            else:
                raise Exception()
        if counta == 0 or countb == 0: # no paths :(
            return None
        return suma / counta + sumb / countb


    def make_root(self, city: int):
        newroot = self.nodes[city]
        self.root = newroot
        newroot.make_root()

    def dbg(self):
        return f'root node: {self.root.value}, nodes:\n' + "\n".join(map(dbg, self.nodes))


def dbg(node: Node):
    p = node.parent and node.parent.value
    return f'Node {node.value}: parent {p}, owner {node.owner}, paths {node.paths}'

def handle_query(tree: Tree):
    type = get_number()
    if type == 1:
        city = get_city()
        #logging.debug('applying flip to %d', city)
        tree.flip(city)
    elif type == 2:
        u = get_city()
        v = get_city()
        #logging.debug('contest with %d %d', u, v)
        print(tree.winner(u, v))
    #logging.debug('tree after operation:\n%s\n', tree.dbg())


def build_tree(start: int, adjacency: list, owner: list) -> Tree:
    nodes: list = [None] * len(adjacency)
    root = Node(start, owner[start], None, None)
    root.build(adjacency, owner, nodes)
    return Tree(root, nodes)

def test():
    pass

if __name__ == '__main__':
    main()


