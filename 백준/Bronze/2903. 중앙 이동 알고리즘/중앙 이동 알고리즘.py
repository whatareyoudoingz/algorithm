init=2
for i in range(int(input())):
    init+=init-1
print(init**2)