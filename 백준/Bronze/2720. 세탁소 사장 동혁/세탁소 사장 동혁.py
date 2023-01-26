coin=[25,10,5,1]
for _ in range(int(input())):
    money=int(input())
    for i in coin:
        print(money//i, end=" ")
        money%=i
    print()