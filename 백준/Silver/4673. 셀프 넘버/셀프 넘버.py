def d(n):
    answer=n
    for i in range(len(str(n))):
        answer+=int(str(n)[i])
    return answer
        

lis=list(range(1,10001))
for n in range(1,10001):
    if d(n) in lis:
        lis.remove(d(n))

for k in lis:
    print(k)
    
# 알고리즘을 짜는 것보다 함수로 변환하는 게 더 어렵다.... 함수로 구현하는 연습해야겠다
