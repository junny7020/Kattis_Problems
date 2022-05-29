# import numpy as np
n = 1
Xs = []
Ys = []
# A1 = 0
# A2 = 0
area = 0

# def get_A1(n):
#     global A1
#     A1 = 0
#     for i in range(n):
#         if(i < n - 1):
#             A1 = A1 + Xs[i] * Ys[i + 1]
#         else:
#             A1 = A1 + Xs[n-1] * Ys[0]

# def get_A2(n):
#     global A2
#     A2 = 0
#     for i in range(n):
#         if(i < n - 1):
#             A2 = A2 + Ys[i] * Xs[i + 1]
#         else:
#             A2 = A2 + Ys[n-1] * Xs[0]

def get_area(n):
    global Xs, Ys
    # global A1, A2
    a = 0
    # get_A1(n)
    # get_A2(n)
    for i in range(n):
        if(i < n -1):
            a = a + Xs[i] * Ys[i+1] - Ys[i] * Xs[i+1]
        else:
            a = a + Xs[n-1] * Ys[0] - Ys[n-1] * Xs[0]
    Xs.clear()
    Ys.clear()
    a = a / 2
    return a

# def get_direction(n):
#     global Xs, Ys
#     d = 0
#     for i in range(n):
#         if (i < n-1):
#             d = d + (Xs[i+1] - Xs[i]) * (Ys[i+1] + Ys[i])
#         else:
#             d = d + (Xs[0] - Xs[n-1]) * (Ys[0] + Ys[n-1])
#     if d>0:
#         return "CW"
#     elif d<0:
#         return "CCW"
#     else:
#         return "not a polygon"


while True:
    n = int(input())

    if(n == 0):
        break
    for i in range(n):
        coor = list(map(int, input().split()))
        Xs.append(coor[0])
        Ys.append(coor[1])

    # di = get_direction(3)

    area = get_area(n)
    if (area > 0):
        print("CCW",area)
    else:
        print("CW",-area)