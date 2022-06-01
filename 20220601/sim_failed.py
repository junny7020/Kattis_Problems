num = int(input())
for i in range(num):
    user_input = list(input().strip(" "))

    temp = []
    answer = []
    x = ""
    i = 0
    open_brak = []
    # print(user_input)
    # print(user_input[1], user_input.pop(1),user_input[1])
    # print(user_input)
    while(user_input != []):
        x = user_input[i]
        if(x == "<"):
            if(temp != []):
                temp.pop()
            elif(temp == [] and answer != []):
                answer.pop()
            user_input.pop(i)
        
        elif(x == "["):
            answer = answer + temp + open_brak
            open_brak = answer
            answer = []
            temp = []
            user_input.pop(i)
        
        elif(x == "]"):
            if(answer != "" or open_brak != []):
                answer = answer + temp + open_brak
                open_brak = []
                temp = []
            user_input.pop(i)
        
        elif(x == " "):
            temp.append(" ")
            user_input.pop(i)

        else:
            temp.append(user_input[i])
            user_input.pop(i)
    answer = answer + temp
    str_answer = ''.join(answer)
    # print(answer)
    print(str_answer)
    # print(list(str_answer.strip()))
# for i in range(len(user_input)):
#     if(user_input[i] == "<"):
#         if(user_input[i-1] != ""):
#             user_input.pop(i-1)
#             i = i - 1
#         user_input.pop(i)
#         i = i - 1
    
#     elif(user_input[i] == "["):
#         temp = temp + user_input[:i]
#         user_input.pop(i)
#         i = i - 1

#     elif(user_input[i] == "]"):
#         if(temp != ""):
#             answer = temp + answer
#             temp = ""
        