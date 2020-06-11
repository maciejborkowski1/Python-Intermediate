def double(x):
    return 2 * x

def root(x):
    return x ** 2

def negative(x):
    return -x

def div2(x):
    return x / 2

number = 8

transformations=[double, root, negative, div2]

tempReturnValue = number

for trans in transformations:
    tempReturnValue = trans(tempReturnValue)
    print("Temp result of {} is {} ".format(trans.__name__, tempReturnValue))