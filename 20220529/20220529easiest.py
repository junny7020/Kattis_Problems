ans = 0
def digitSum(n):
    digit_sum = 0
    temp = n
    while(temp != 0):
        if(temp == 0):
            break
        digit_sum += temp % 10
        temp = temp // 10
    return digit_sum

def find_p(n):
    p = 11
    check = digitSum(n)
    while (check != digitSum(n*p)):
        p = p + 1
    return p

while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(find_p(n))