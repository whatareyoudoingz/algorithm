n=input()

if len(n)==1:
    n='0'+n

a,b=int(n[0]),int(n[1])
answer=a+b #첫 숫자 a+b
string=0
i=0
while string!=n: #숫자가 입력값과 다를때 반복
    a=b #6
    b=int(str(answer)[-1]) #8
    #문자열 ab
    string=str(a)+str(b) #68
    #숫자 a+b
    answer=a+int(string[-1]) #14
    i+=1

print(i)