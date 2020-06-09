ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ', 'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

flights = [(a,b) for a in ports for b in ports]

print(flights)

print('-'*50)

flights = [(a,b) for a in ports for b in ports if a != b]

print(flights)

print('-'*50)

flights = [(a,b) for a in ports for b in ports if a < b]

print(flights)