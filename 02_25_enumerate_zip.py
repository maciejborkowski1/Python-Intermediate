projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for i, (j, z) in enumerate(zip(projects, leaders)):
    print('The leader of {} is {}.'.format(j, z))

print ('-'*50)

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for i, (j, z, x) in enumerate(zip(projects, dates, leaders)):
    print('The leader of {}, started {}, is {}.'.format(j, z, x))

for i, (j, z, x) in enumerate(zip(projects, dates, leaders)):
    print('{}: The leader of {}, started {}, is {}.'.format(i+1, j, z, x))