from datetime import datetime


def timeSpanM(start, end):
    duration = end - start
    durationInS = duration.total_seconds()
    return divmod(durationInS, 60)[0]


def timeSpanH(start, end):
    duration = end - start
    durationInS = duration.total_seconds()
    return divmod(durationInS, 3600)[0]


def timeSpanD(start, end):
    duration = end - start
    durationInS = duration.total_seconds()
    return divmod(durationInS, 86400)[0]

start = datetime(2019, 1, 1, 0, 0, 0)
end = datetime.now()

print(timeSpanM(start, end))
print(timeSpanH(start, end))
print(timeSpanD(start, end))

print('*'*30)

#the same but with the function returing other function

def createFunction(span):
    if span == 'm':
        sec=60
    elif span == 'h':
        sec=3600
    else:
        sec=86400
    source = '''
def f(start, end):
    duration = end - start
    durationInS = duration.total_seconds()
    return divmod(durationInS, {})[0]    
'''.format(sec)
    exec(source, globals())
    return f

fMinutes = createFunction('m')
fHours = createFunction('h')
fDays = createFunction('d')

print(fMinutes(start, end))
print(fHours(start, end))
print(fDays(start, end))

