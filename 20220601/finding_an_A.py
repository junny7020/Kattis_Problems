text = list(input().strip(" "))

found_a = 0
ans = ""
for i in text:
    if(i == "a"):
        found_a = 1
    if(found_a == 1):
        ans = ans + i
print(ans)