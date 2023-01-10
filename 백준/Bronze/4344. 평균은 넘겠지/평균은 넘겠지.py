for _ in range(int(input())):
    number=list(map(int,input().split()))
    average=sum(number[1:])/number[0]
    count=0
    for i in number[1:]:
        if i > average:
            count+=1
    print('%.3f' %((count/number[0])*100)+'%')