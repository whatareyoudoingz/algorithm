T=int(input())
room=[list(input()) for _ in range(T)]
width,length=0,0
for i in range(T):
    a=0 
    for j in range(T):
        if room[i][j]=='.' :  
                a+=1
        elif room[i][j]=='X': 
            if a > 1: 
                width+=1
            a=0
        if j==T-1:
            if a > 1: 
                width+=1
for j in range(T):
    a=0 
    for i in range(T):
        if room[i][j]=='.' :  
                a+=1
                room[i][j]=0
        elif room[i][j]=='X': 
            if a > 1:
                length+=1
            a=0
        if i==T-1:
            if a > 1:
                length+=1
print(width, length)