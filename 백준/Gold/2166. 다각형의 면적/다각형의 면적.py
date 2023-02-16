import sys
input = sys.stdin.readline
N = int(input())
x = []
y = []

for i in range(N):
    tempX, tempY = map(int, input().split())
    x.append(tempX)
    y.append(tempY)

x.append(x[0]) #폐곡선을 만들어 줘야 한다. 
y.append(y[0])

result = 0
for i in range(N):
    ccw=x[i]*y[i+1]-x[i+1]*y[i]
    result+=ccw
print(round(abs(result)/2,1))