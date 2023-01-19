score=input()
dic={}
t=0
for i in ['A','B','C','D','F']:
    if i == 'F':
        dic[i]=0.0
        continue
    tt=0
    for j in ['+','0','-']:
        dic[i+j]=round(4.3-t-(0.3)*tt,2)
        tt+=1
    t+=1
print(dic[score])