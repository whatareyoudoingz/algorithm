s=input().upper()
total=0 # 최대 카운트 수
tt=[] # 최대 문자
for i in set(s): #하나씩 살펴보자
    if total < s.count(i) : #문자 카운트 수가 최대보다 크면
        total = s.count(i) #최대 카운트 수를 바꾸자
        tt.clear()
        tt.append(i) # 최대 문자
    elif total == s.count(i):
        tt.append(i) # 최대 문자

if len(tt)==1:
    print(tt[0])
else:
    print("?")
    
# 다른 풀이 (출처 : 백준 , 아이디 : jun0woong)
s=input().upper()
total=0 # 최대 카운트 수
tt=[] # 최대 문자
for i in set(s): #하나씩 살펴보자
    if total < s.count(i) : #문자 카운트 수가 최대보다 크면
        total = s.count(i) #최대 카운트 수를 바꾸자
        tt.clear()
        tt.append(i) # 최대 문자
    elif total == s.count(i):
        tt.append(i) # 최대 문자

if len(tt)==1:
    print(tt[0])
else:
    print("?")
