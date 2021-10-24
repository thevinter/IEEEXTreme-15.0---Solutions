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

def get_spy():
    data = get_word()
    # print(data)
    color = 0 if data[0] == 'R' else 1
    return color, int(data[1:]) - 1


def main():
    tests = get_number()
    for _ in range(tests):
        do_test()

def do_test():
    reds = get_number()
    blues = get_number()
    instructions = get_number()
    red_spies = [None] * reds
    blue_spies = [None] * blues
    spies = [red_spies, blue_spies]
    for i in range(1,reds):
        superior = get_spy()
        red_spies[i] = superior
    for i in range(1,blues):
        superior = get_spy()
        blue_spies[i] = superior
    # print(f'reds: {red_spies}')
    # print(f'blues: {blue_spies}')
    for _ in range(instructions):
        event = get_word()
        if event == 'c':
            spy = get_spy()
            superior = get_spy()
            spies[spy[0]][spy[1]] = superior
        elif event == 'w':
            x = get_spy()
            y = get_spy()
            do_warthing(spies, x, y)
        else:
            raise ValueError(f"the fuck is {event}")

def do_warthing(spies, x, y):
    outcome_x = find_count(spies, x)
    outcome_y = find_count(spies, y)
    if outcome_x is None and outcome_y is None:
        print('NONE')
    elif outcome_x is None:
        count, col = outcome_y
        print(f'{"BLUE" if col else "RED"} {count}')
    elif outcome_y is None:
        count, col = outcome_x
        print(f'{"BLUE" if col else "RED"} {count}')
    else:
        count_x, col_x = outcome_x
        count_y, col_y = outcome_y
        if col_x == col_y:
            print(f'{"BLUE" if col_x else "RED"} {min(count_x,count_y)}')
        elif count_x < count_y:
            print(f'{"BLUE" if col_x else "RED"} {count_x}')
        elif count_x > count_y:
            print(f'{"BLUE" if col_y else "RED"} {count_y}')
        else:
            print(f'TIE {count_x}')


def find_count(spies, x):
    # print(f'starting at {x}')
    count_x = 0
    seen = set()
    while x is not None and x not in seen:
        if x[1] == 0:
            break
        seen.add(x)
        x = spies[x[0]][x[1]]
        count_x += 1
    else: # cycle
        # print('found cycle')
        return None
    # print('arrived at {x}')
    return count_x, x[0]

main()


