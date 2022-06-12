from turtle import pu


puzzle = []
row = []

for i in range(4):
    row = list(map(int,input().split()))
    puzzle.append(row)

move = int(input())

if(move == 0):
    # move left
    print(puzzle[0])
# elif(move == 1):
#     move up
# elif(move == 2):
#     move right
# elif(move == 3):
#     move down

print(puzzle)