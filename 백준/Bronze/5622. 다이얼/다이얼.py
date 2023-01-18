n=input()
answer=0
dic={2:['A','B','C'],3:['D','E','F'],4:['G','H','I'],5:['J','K','L'],6:['M','N','O'],7:['P','Q','R','S'],8:['T','U','V'],9:['W','X','Y','Z']}
for i in n:
    if i == 1:
        answer+=2
    elif i == 0 :
        answer+=11
    else:
        for idx,value in dic.items():
            if i in value:
                answer+=idx+1
print(answer)

## 다른 풀이 (출처 : 백준, 아이디 : rogerchoo)
word = input()
time = 0
for char in word:
    time += (ord(char) + 1) // 3 - 19 
    if char in 'SVYZ': time -= 1
print(time)
