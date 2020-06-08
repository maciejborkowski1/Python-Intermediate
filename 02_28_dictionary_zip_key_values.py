banknotesCoins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
counter = []

for i in range (len(banknotesCoins)):
    counter.append(0)

dictDenominations = dict(zip(banknotesCoins, counter))

dictDenominations[100] += 1
dictDenominations[20] += 1
dictDenominations[5] += 1
dictDenominations[0.5] += 1

dictDenominations[50] += 1
dictDenominations[20] += 2
dictDenominations[5] += 1
dictDenominations[2] += 2

dictDenominations[100] += 1
dictDenominations[50] += 1
dictDenominations[2] += 1

for key in dictDenominations:
    print('Denominate:{0:6.2f} - amount:{1:5}'.format(key, dictDenominations[key]))







