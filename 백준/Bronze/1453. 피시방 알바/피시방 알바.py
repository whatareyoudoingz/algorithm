seat=list(range(1,101))
n, total=int(input()) , 0
numbers=list(map(int,input().split()))
for number in numbers:
    if number in seat:
        seat.remove(number)
    else:
        total+=1
print(total)