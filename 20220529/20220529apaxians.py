s = input()
ans = s[0]
for i in range(len(s)):
    if(ans[-1] == s[i]):
        continue
    else:
        ans = ans + s[i]
print(ans)