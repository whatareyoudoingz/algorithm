for _ in range(int(input())):
    result=0
    m,n=map(int,input().split())
    box=[list(input().split()) for _ in range(m)]
    for j in range(n):
        if box[m-1][j]=='1':
            for i in range(m-1):
                if box[i][j]=='1': 
                    for k in range(i+1,m-1):
                        if box[k][j]=='0': 
                            result+=1
                if box[i][j]=='0': 
                    continue
        else: 
            for i in range(m):
                if box[i][j]=='1': 
                    for k in range(i+1,m):
                        if box[k][j]=='0': 
                            result+=1
                if box[i][j]=='0': 
                    continue
    print(result)