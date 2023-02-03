for i in range(int(input())):
    n,m=map(int,input().split())
    graph=[list(map(int,input().split())) for _ in range(n)] 

    total=0
    answer=[]
    for a in range(n-m+1): 
        for b in range(n-m+1):
            total=0
            for x in range(m):
                for y in range(m):
                    total+=graph[a+x][b+y]
            answer.append(total)
        
    print(f"#{i+1} {max(answer)}")