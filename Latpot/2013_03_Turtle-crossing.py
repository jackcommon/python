def turtle_crossing(A):
    alist = []
    alist.append([0,0])
    x = 0
    y = 0
##    print('fefes')
    for step, value in enumerate(A):
        if step % 4 == 0:
            for i in range(value):
                y = y+1
                if [x,y] in alist:
                    return step+1
                else:
                    alist.append([x,y])
        elif step % 4 == 1:
            for i in range(value):
                x = x+1
                if [x,y] in alist:
                    return step+1
                else:
                    alist.append([x,y])
        elif step % 4 == 2:
            for i in range(value):
                y = y-1
                if [x,y] in alist:
                    return step+1
                else:
                    alist.append([x,y])
        elif step % 4 == 3:
            for i in range(value):
                x = x-1
                if [x,y] in alist:
                    return step+1
                else:
                    alist.append([x,y])
    return 0


##-------------------------------
def teotimeit(repeat, func, *args, **kwargs):
    from datetime import datetime
    start = datetime.now()
    for i in range(repeat):
        func(*args, **kwargs)
    end = datetime.now()
    return end - start
##================================
A = [1,3,2,
     5,4,4,
     6,3,2]

print(teotimeit(100000,turtle_crossing,(A)))


##x = {(2,i) for i in range(5)}
##y = set()
##y.add((2,6))
##x = x.union(y)
##print(x)
##print(y)
