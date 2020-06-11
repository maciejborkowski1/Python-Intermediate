import math
import time

formulasList = [
    "abs(x**3 - x**0.5)",
    "abs(math.sin(x) * x**2)"
    ]

argumentList = []
for i in range(1000000):
    argumentList.append(i / 10)

for formula in formulasList:
    resultList = []
    print('Expression {} in progress.'.format(formula))
    start = time.time()
    for x in argumentList:
        resultList.append(eval(formula))
    print('Max = {} Min = {}'.format(max(resultList), min(resultList)))
    stop = time.time()
    print ('Total time of operation: {}'.format(stop - start))

print('*'*30)

for formula in formulasList:
    resultList = []
    print('Expression {} in progress.'.format(formula))
    start = time.time()
    compliedFormula = compile(formula, 'Internal expression', 'eval')
    for x in argumentList:
        resultList.append(eval(compliedFormula))
    print('Max = {} Min = {}'.format(max(resultList), min(resultList)))
    stop = time.time()
    print ('Total time of operation: {}'.format(stop - start))

