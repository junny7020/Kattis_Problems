nums = int(input())
sum = 0

for i in range(nums):
    r1, r2 = list(map(float,input().split()))
    sum = sum + r1 * r2
    # print(sum)
print(sum)