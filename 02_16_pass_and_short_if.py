import datetime

price = 123
bonus = 23
bonusGranted = True
rating = 5

#this is two samples of shorter version if loop
print(price - bonus) if bonusGranted else print('False')
print('very good') if rating == 5 else print ('good') if rating == 4 else print ('weak')

#check what is the day today, and assign to correct string from list
todayString = datetime.datetime.today().strftime('%A')


#another sample of short loop expression
print('Workday - go to the office.') if todayString == 'Monday' or todayString == 'Tuesday' or todayString == 'Wednesday' or \
    todayString == 'Thursday' or todayString == 'Friday' else print('Weekday - free time!')


