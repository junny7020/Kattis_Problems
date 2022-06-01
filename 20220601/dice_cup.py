dice1, dice2 = list(map(int,input().split()))
if(dice1 > dice2):
    MIN = dice2 + 1
    MAX = dice1 + 1
else:
    MAX = dice2 + 1
    MIN = dice1 + 1

for i in range(MIN,MAX + 1):
    print(i)