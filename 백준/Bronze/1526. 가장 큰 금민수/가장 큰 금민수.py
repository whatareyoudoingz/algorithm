T=int(input())
top=0
for i in range(T+1):
    call=set(str(i))-set(('4','7'))
    if len(call)==0 and top <  i <= T+1:
        top=i
print(top)