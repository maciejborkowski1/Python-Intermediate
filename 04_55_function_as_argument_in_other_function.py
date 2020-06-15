def double(x):
    return 2 * x

def root(x):
    return x ** 2

def negative(x):
    return -x

def div2(x):
    return x / 2

def generateValues(equation, xTable):
    resultList = []
    for x in xTable:
        resultList.append(equation(x))
    return resultList


xTable = list(range(11))

print(generateValues(double, xTable))
print(generateValues(root, xTable))
print(generateValues(negative, xTable))
print(generateValues(div2, xTable))