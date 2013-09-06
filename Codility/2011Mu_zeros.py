def solution(n):
    x = int(n)
    print(x)
    
    result = 0
    for i in range(x+1):
        string = str(i)
        for j in string:
            if j == '0':
                result += 1
    
    return result
print(solution('99'))
