loop = int(input())
nums = []

for i in range(loop):
    nums.append(input())

for i in range(loop):
    print(nums[loop - i - 1])