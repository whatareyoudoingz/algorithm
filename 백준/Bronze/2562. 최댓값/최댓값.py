number=[int(input()) for _ in range(9)]
a=sorted(number)[-1]
print(a,number.index(a)+1,sep="\n")