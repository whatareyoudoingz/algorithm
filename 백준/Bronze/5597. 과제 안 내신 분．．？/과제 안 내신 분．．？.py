total=[i for i in range(1,31)]
for _ in range(28):
    total.remove(int(input()))
    sorted(total)
print(total[0])
print(total[1])