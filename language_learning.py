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



def main():
    tests = get_number()
    for _ in range(tests):
        print(do_test())

def do_test():
    n = get_number()
    k = get_number()
    words = [None] * n
    for i in range(n):
        words[i] = get_word()
    return sentences(words,k,n)


def stupid_sentences(words, k, n):
    sentences_from = [ [] for _ in range(n+2)]
    sentences_from[-1] = []
    sentences_from[-2] = ['']
    lookahead = make_lookahead(words, n, k)
    for i in range(n):
        j = n - i - 1
        sentences_from[j] += sentences_from[j+1]
        starting = min(j+k+1,n)
        edge = lookahead[j] or n+1
        sentences_from[j] += [words[j] + ' ' + w for w in sentences_from[starting] if w not in sentences_from[edge]]

    for l in (sentences_from):
        print(l)
    return len(sentences_from[0]) - 1

def sentences(words, k, n):
    m = 1_000_000_007
    sentences_from = [0] * (n + 2)
    sentences_from[-2] = 1
    lookahead = make_lookahead(words, n, k)
    for i in range(n):
        j = n - i - 1
        sentences_from[j] += sentences_from[j+1] % m
        starting = min(j+k+1,n)
        edge = lookahead[j] or n+1
        sentences_from[j] += sentences_from[starting] - sentences_from[edge]
        sentences_from[j] %= m
        
    # print(sentences_from)
    num = sentences_from[0] - 1
    while num < 0:
        num += m
    return num

def make_lookahead(words, n, k):
    table = {}
    lookahead = [None] * n
    for i in range(n):
        j = n - i - 1
        current = words[j]
        if current in table:
            lookahead[j] = min(n, table[current] + k + 1)
        table[current] = j
    # print(lookahead)
    return lookahead

main()


