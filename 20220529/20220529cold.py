n = int(input())
temps = list(map(int,input().split()))
count = 0
for i in range(n):
    if(temps[i] < 0):
        count = count + 1
print(count)