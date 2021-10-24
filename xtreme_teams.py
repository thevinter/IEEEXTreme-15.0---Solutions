
T = int(input())
for i in range(T):
    N, M = input().split(" ")
    N = int(N)
    M = int(M)
    students = []
    for j in range(N):
        x = input()
        students.append([True if c == "y" else False for c in x])
    
    arr = [x for x in range(3)]
    cnt = 0
    finished = 0;
    while True:
        subj = [False]*M
        for j in range(3):
            res = students[arr[j]]
            subj = [a or b for (a,b) in zip(subj, res)]
        if False in subj: 
            pass
        else:
            cnt += 1
            
            
        if arr[0] == N - 3:
            break
        n = 2
        while True:
            arr[n] += 1
            maxLimit = N-3+n
            if(arr[n] > maxLimit):
                n-=1
            else:
                for x in range(n+1, 3):
                    arr[x] = arr[x-1]+1
                break
        
    print(cnt)
    



