string=[]
for _ in range(5):
    n=input()
    string.append(list(n)+[-1]*(15-len(n)))

for j in range(15):
    for i in range(5):
        if string[i][j] != -1 :
            print(string[i][j],end="")
        else:
            continue