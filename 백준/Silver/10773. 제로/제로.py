total=[]
for _ in range(int(input())):
    money=int(input())
    if money != 0:
        total.append(money)
    else:
        total.pop()
print(sum(total))