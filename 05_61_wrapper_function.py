import functools
import time

def getSequenceWithWrapper(func):
    def funcWrapper(*args, **kwargs):
        start = time.time()
        v = func(*args, **kwargs)
        stop = time.time()
        print("Function {} was made in {} second".format(func.__name__, stop - start))
        return v
    return funcWrapper

@getSequenceWithWrapper
def getSequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (getSequence(i - 1) + getSequence(i)) / 2
        return v

#wrapperGetSequence = getSequenceWithWrapper(getSequence)
#print (wrapperGetSequence(18))

print(getSequence(18))