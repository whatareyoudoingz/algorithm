n=int(input())
ans=[' ' for _ in range(2*n-1)]
for i in range(2*n-1):
    s=(2*n-1)//2
    if i<=s:
        ans[s]='*'
        ans[s-i]='*'
        ans[s+i]='*'
    else:
        k=(2*n-1)-i
        ans[s-k]=' '
        ans[s+k]=' '
    print("".join(ans).rstrip(),end="\n")
        