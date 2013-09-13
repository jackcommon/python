def turtle_crossing(A):
    aset = {(0,0)}
    x, y = 0, 0
    stepscount = 1
    for walk, value in enumerate(A):
        if walk % 4 == 0:
            temp = {(x,y+(i+1)) for i in range(value)}
            y += value
        elif walk % 4 == 1:
            temp = {(x+(i+1),y) for i in range(value)}
            x += value
        elif walk % 4 == 2:
            temp = {(x,y-(i+1)) for i in range(value)}
            y -= value
        elif walk % 4 == 3:
            temp = {(x-(i+1),y) for i in range(value)}
            x -= value
        aset = aset.union(temp)
        stepscount += value
        if (stepscount != len(aset)):
            return(walk+1)
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
