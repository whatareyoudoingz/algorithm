massage=input()
lis=[]
while True:
    massage=input()
    if "고무오리 디버깅 끝"==massage:
        break
    if massage == '문제':
        lis.append(massage)
    else:
        if lis: 
            lis.pop()
        else:
            lis.extend(["문제","문제"])
print("고무오리야 사랑해" if len(lis)==0 else "힝구")