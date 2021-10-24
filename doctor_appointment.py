T = int(input())
for t in range(T):
    l = []
    N = int(input())
    for n in range(N):
        x,y = (int(i) for i in input().split(" "))
        positions = (y-x+1, x, y, n+1)
        l.append(positions)
        l.sort()
    res = []
    for p in l:
        res.append((0,0,0,0))
    while l:
        patient = l[0]
        #print(patient[1])
        
        l = l[1:]
        slot = 0
        for i in range(patient[1], patient[2]+1):
            if res[i-1] == (0,0,0,0):
                res[i-1] = patient
                slot = i
                break
        if slot != 0:
            y = []
            for p in l:
                if p[1] <= slot <= p[2]:
                    y.append((p[0]-1,p[1],p[2],p[3]))
                else:
                    y.append(p)
            y.sort()
            l = y
    out = ""
    for p in res:
        if p[3] == 0:
            out = "impossible "
            break
        out+=str(p[3]) + " "
    print(out[:-1])    


