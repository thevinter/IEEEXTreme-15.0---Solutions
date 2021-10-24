R,C,Q = [int(i) for i in input().split(" ")]


def increase(typ, coord):
    (r,c) = coord
    # -> horiz right
    if typ == 0:
        return r,c+1
    # <- horiz left
    if typ == 1:
        return r,c-1
    # ^ vert up
    if typ == 2:
        return r-1,c
    # V vert down
    if typ == 3:
        return r+1,c
    # right up
    if typ == 4:
        return r-1,c+1
    # right down
    if typ == 5:
        return r+1,c+1
    # left down
    if typ == 6:
        return r+1,c-1
    # left up
    if typ == 7:
        return r-1,c-1
        
def fits(typ, leng, coord, sizes):
    (r,c) = coord
    (R,C) = sizes
    # -> horiz right
    if typ == 0:
        return c + leng <= C
    # <- horiz left
    if typ == 1:
        return c - leng >= -1
    # ^ vert up
    if typ == 2:
        return r - leng >= -1
    # V vert down
    if typ == 3:
        return r + leng <= R
    # right up
    if typ == 4:
        return c + leng <= C and r - leng >= -1
    # right down
    if typ == 5:
        return c + leng <= C and r + leng <= R
    # left down
    if typ == 6:
        return c - leng >= -1 and r + leng <= R
    # left up
    if typ == 7:
        return c - leng >= -1 and r - leng >= -1

table = []
initials = {}
for r in range(R):
    row = input()
    table.append(row)
    
    for c,ch in enumerate(row):
        if not ch in initials:
            initials[ch] = []
            
        initials[ch].append((r,c))

# print(initials)
    
for q in range(Q): 
    word = input()
    begin = word[0]
    done = False
    for (sr,sc) in initials[begin]:
        for typ in range(8):
            leng = len(word)
            # print(f"word: {word} ({leng}), in ({sr},{sc}), typ={typ}")
            if not fits(typ, leng, (sr,sc), (R,C)):
                continue
            i = 0
            (r,c) = (sr,sc)
            while word[i] == table[r][c]:
                i += 1
                if i == leng:
                    done = True
                    print(f"{sr} {sc} {r} {c}")
                    break
                r,c = increase(typ, (r,c))
            
            if done:
                break
        if done:
            break
    if not done:
        print(-1)

