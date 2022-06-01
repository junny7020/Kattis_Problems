def return_string(uer_input):
    cursor = 0
    result = []
    for letter in user_input:
        
        if(letter == '<'):
            if(cursor != 0):
                cursor = cursor -1
                result.pop(cursor)
            continue
        
        elif(letter == '['):
            cursor = 0
            continue
        
        elif(letter == ']'):
            cursor = len(result)
            continue
        
        else:
            result.insert(cursor,letter)
            cursor = cursor + 1
            continue
        # print(result)
    str_result = ''.join(result)
    return str_result


num = int(input())

str_result =""
for i in range(num):
    user_input = list(input().strip(" "))
    str_result = return_string(user_input)
    print(str_result)