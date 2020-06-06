def displayOptions (options):
    for i in range (len(options)):
        print('{} - {}'.format(i+1, options[i]))
    choice = input('Provide your choose number: ')
    return choice


options=['load data', 'export data', 'analyze & predict']
choice = 'x'

while choice:
    choice = displayOptions(options)

    #we do it only if 'choice' not empty
    if choice:
        try:
            choice_num = int(choice)-1
            if choice_num >= 0 and choice_num < len(options):
                print('You choose a {} - {}'.format(choice_num+1, options[choice_num]))
            else:
                print('You have provided wrong number')
        except:
            print("You haven't provided number")
    else:
        print('BYE')
