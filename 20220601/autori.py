author = input().split('-')
short = ""
for letter in author:
    short = short + letter[0]
print(short)