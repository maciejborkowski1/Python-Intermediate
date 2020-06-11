def calculatePaint (efficencyLtrPerM2, *paint):
    paintQuantity = 0
    roomList = paint
    for i in roomList:
        temp = efficencyLtrPerM2 * i
        paintQuantity+=temp
    return 'To paint all rooms you need to have {} liters of paint.'.format(paintQuantity)

print (calculatePaint(1, 5, 50, 25))
print ('*'*30)

roomsToPaint = [30, 25, 74, 22]

print(calculatePaint(3, *roomsToPaint))

print ('*-*'*30)

def logIt (*logs):
    path = r'C:\Python intermediate\temp\log_it.txt'
    file = open(path, 'a')
    for i in logs:
        file.write('"'+i+'"')
        file.write(' ')
    file.write('\n')
    file.close()
    print("'{}' was uploaded by {} new arguments.".format(path, len(logs)))

logIt('Starting processing forecasting')
logIt('ERROR', 'Not enough data', 'invoices', '2020')


