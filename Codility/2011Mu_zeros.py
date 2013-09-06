def solution(S):
    N = int(S)
    i = 0
    while N >= 0:
        i += str(N).count('0')
        N -= 1
    return i


print(solution('219'))
