def box_checker(a):
    global i,j,result
    for i in range(a):
        if box[i][j]=='1': 
            for k in range(i+1,a):
                if box[k][j]=='0': 
                    result+=1
        if box[i][j]=='0': 
            continue

for _ in range(int(input())):
    result=0
    m,n=map(int,input().split())
    box=[list(input().split()) for _ in range(m)]
    for j in range(n):
        if box[m-1][j]=='1':
            box_checker(m-1)
        else: 
            box_checker(m)
    print(result)