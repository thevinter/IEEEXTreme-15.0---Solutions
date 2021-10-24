T = int(input())

for i in range(T):
    alice = 0
    bob = 0
    ad = [0] 
    an = []
    bobd = [1]
    bobn = []
    dice6 = [0,0]
    N = int(input())
    for i in range(N):
        [a, b] = input().split(" ")
        an.append(int(a))
        bobn.append(int(b))
        alice += int(a)
        bob += int(b)
        if alice != bob:
            ad.append((ad[i] + 1) % 2)
            bobd.append((bobd[i] + 1) % 2)
        else:
            ad.append(ad[i])
            bobd.append(bobd[i])
        if int(a) == 6: dice6[ad[i+1]] += 1
        if int(b) == 6: dice6[bobd[i+1]] += 1

        
    
    print(1 if dice6[0] < dice6[1] else 2)
        
