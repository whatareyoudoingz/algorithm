for _ in range(int(input())):
    number=sorted(list(map(int,input().split())),reverse=True)[1:-1]
    print("KIN" if number[0]-number[-1] >=4 else sum(number))