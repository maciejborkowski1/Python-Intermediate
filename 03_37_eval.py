import math

argumentList = []

for i in range (100):
    argumentList.append(i/10)

formula = input("Provide math formula using 'x' as argument: ")

for x in argumentList:
    print('for x = {0:3.1f} result is: {1:6.2f}'.format(x, eval(formula)))



