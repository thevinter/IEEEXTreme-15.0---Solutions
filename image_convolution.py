def match(img, pos, pattern, ppos):
    (r,c) = pos
    (X,Y) = ppos
    
    ok = True
    for x in range(X):
        for y in range(Y):
            ch = pattern[x][y]
            if ch == "?":
                continue
            
            if ch != img[r+x][c+y]:
                ok = False
                break
        if not ok:
            break
    
    return ok
    

T = int(input())

for t in range(T):
    R,C = [int(i) for i in input().split(" ")]
    
    image = []
    for r in range(R):
        image.append(input())
    
    X,Y = [int(i) for i in input().split(" ")]
    
    pattern = []
    for r in range(X):
        pattern.append(input())
    
    
    cnt = 0
    for r in range(R - X + 1):
        for c in range(C - Y + 1):
            if match(image, (r,c), pattern, (X,Y)):
                cnt += 1
                # print(r,c)
    print(cnt)
    
    
