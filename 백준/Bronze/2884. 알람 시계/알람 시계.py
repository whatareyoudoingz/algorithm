h,m=map(int,input().split())

start=h*60+m
new=start-45
h=new//60
m=new%60

if h < 0:
    h = 24 + h

print(h, m)