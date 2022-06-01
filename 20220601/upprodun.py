import math


N = int(input())
M = int(input())
# N_ceil = math.ceil(M/N)
N = M/N
count = N
# print(N_ceil,N)
for i in range(M):
    print("*", end='')
    count -= 1
    if(count <= 0):
        count = count + N
        print()