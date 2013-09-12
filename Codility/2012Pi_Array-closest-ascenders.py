import sys

INF = 1000000123

def left_closest_ascenders(A):
    N = len(A)
    if (N == 0): return A
    ret = [0] * N
    stack = [0] * N
    stack_size = 0
    for I in range(N):
        while (stack_size > 0) and (A[stack[stack_size-1]] <= A[I]):
            stack_size -= 1
        if (stack_size == 0):
            ret[I] = INF
        else:
            ret[I] = I - stack[stack_size-1]
##            import pdb; pdb.set_trace()
        stack[stack_size] = I
        stack_size += 1
        print(str(I) + ' : ' + str(stack_size))
    return ret

def array_closest_ascenders(A):
    N = len(A)
    left = left_closest_ascenders(A)
    sys.stdout.write('left')
    print(left)
    A.reverse()
    right = left_closest_ascenders(A)
    right.reverse()
    sys.stdout.write('right')
    print(right)
    ret = [0] * N
    for I in range(N):
        ret[I] = min(left[I], right[I])
        if ret[I] == INF:
            ret[I] = 0
    return ret
##==================================================

A = [4,3,1,
     4,-1,2,
     1,5,7]
print(A)
print(array_closest_ascenders(A))
