r1, r2 = list(map(int,input().split()))
s1 = 0
if(r1>=r2):
   s1 = r2 - (r1 - r2)
else:
    s1 = r2 + (r2 - r1)

print(s1)