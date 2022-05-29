nums = int(input())
sum = 0
pow = 0
x = 0
for i in range(nums):
    n = int(input())
    pow = n % 10
    x = n // 10
    sum = sum + x ** pow
print(sum)