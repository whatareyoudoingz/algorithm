a,b=list(map(int,input().split()))
c=int(input())

top=c//60
if top <=0:
	b+=c
else:
    a+=top
    bot=60*top
    b+=c-bot

if b >= 60:
    a+=b//60
    b%=60

if a >= 24:
    a-=24
print(a,b)