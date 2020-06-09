ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ', 'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

#to generate single value from list use expression 'next(flights)'

flights = ((a,b) for a in ports for b in ports)
x=1
for i in flights:
    x+=1
print('We have generated {} elements'.format(x))

print('-'*50)

flights = ((a,b) for a in ports for b in ports if a != b)
x=1
for i in flights:
    x+=1
print('We have generated {} elements'.format(x))

print('-'*50)

x=1
flights = ((a,b) for a in ports for b in ports if a < b)
while True:
    x+=1
    try:
        print(next(flights))
    except StopIteration:
        print('{} values have been generated'.format(x))
        break
