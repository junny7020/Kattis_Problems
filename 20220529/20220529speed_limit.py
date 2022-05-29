pair = 0
speed = 0
hours = 0
miles = 0
temp = 0
pair_i = []
while(pair != -1):
    pair = int(input())
    for i in range(pair):
        pair_i = list(map(int,input().split()))
        speed = pair_i[0]
        hours = pair_i[1] - temp
        miles = miles + speed * hours
        temp = hours + temp
    temp = 0
    if(pair != -1):
        print(miles,"miles")
    miles = 0