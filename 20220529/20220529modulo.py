mod = []
count = 0
temp = 0
for i in range(10):
    n = int(input())
    temp = n % 42
    if (temp not in mod):
        count += 1
        mod.append(temp)
    else:
        continue
print(count)